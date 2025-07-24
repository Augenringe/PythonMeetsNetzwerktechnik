import netmiko
import PySide6

result = "Cisco IOS XE Software, Version 16.09.05\n Cisco IOS Software..."
# Finde die Startposition des Wortes "Version"
start = result.find("Version") + len("Version ")
# Extrahiere die Version bis zum nächsten Zeilenumbruch
end = result.find("\n", start)
version = result[start:end]
print("Extrahierte Version:", version)