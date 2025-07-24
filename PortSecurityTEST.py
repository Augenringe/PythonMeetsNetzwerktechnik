from netmiko import ConnectHandler
import requests
from datetime import datetime

# Telegram-Konfiguration
TELEGRAM_TOKEN = ""  # Bot-Token
TELEGRAM_CHAT_ID = ""  # Chat-ID

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def format_violation_output(raw_output):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = raw_output.strip().splitlines()
    if not lines:
        return None

    formatted = f"⚠️ *Port-Security Violation erkannt!*\n\n🕒 *Zeitpunkt:* `{timestamp}`\n"
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            mac = parts[0]
            intf = parts[1]
            formatted += f"\n🔌 *Port:* `{intf}`\n🔐 *MAC:* `{mac}`\n"
    return formatted

def deploy_port_security(host, user, pwd, intfs):
    dev = {
        "device_type": "cisco_ios",
        "host": host,
        "username": user,
        "password": pwd,
    }
    cmd_list = [
        f"interface range {intfs}",
        "switchport mode access",
        "switchport port-security",
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security mac-address sticky",
    ]

    with ConnectHandler(**dev) as conn:
        conn.enable()
        print(conn.send_config_set(cmd_list))
        conn.save_config()

        # Prüfen auf Violations (nur betroffene MACs mit Status "SecureViolation")
        violation_data = conn.send_command("show port-security address | include SecureViolation")

        if violation_data.strip():
            message = format_violation_output(violation_data)
            if message:
                send_telegram_alert(message)

if __name__ == "__main__":
    deploy_port_security("192.168.1.1", "admin", "pass", "Gig1/0/1-10")
