from netmiko import ConnectHandler

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

if __name__ == "__main__":
    deploy_port_security("192.168.1.1", "admin", "pass", "Gig1/0/1-10")
