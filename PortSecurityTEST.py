from netmiko import ConnectHandler
import customtkinter as ctk
from datetime import datetime

# GUI-Konfiguration
def show_violation_gui(mac, port):
    ctk.set_appearance_mode("system")  # "light", "dark", or "system"
    root = ctk.CTk()
    root.geometry("800x800")
    root.title("⚠️ Port-Security Violation")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"⚠️ Port-Security-Verstoß erkannt!\n\n🕒 {timestamp}\n🔌 Port: {port}\n🔐 MAC: {mac}"

    label = ctk.CTkLabel(root, text=msg, font=("Arial", 16), justify="left", wraplength=400)
    label.pack(padx=20, pady=20)

    button = ctk.CTkButton(root, text="OK", command=root.destroy)
    button.pack(pady=10)

    root.mainloop()


# Violation-Formatierung
def parse_violation_output(raw_output):
    lines = raw_output.strip().splitlines()
    violations = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            mac = parts[0]
            intf = parts[1]
            violations.append((mac, intf))
    return violations


# Port-Security Konfiguration und Prüfung
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

        # Prüfen auf Violations
        output = conn.send_command("show port-security address | include SecureViolation")
        violations = parse_violation_output(output)

        for mac, port in violations:
            show_violation_gui(mac, port)


# Hauptausführung
if __name__ == "__main__":
    deploy_port_security("192.168.1.1", "admin", "pass", "Gig1/0/1-10")
