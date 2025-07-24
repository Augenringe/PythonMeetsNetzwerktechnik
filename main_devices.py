import sys
import argparse
from devices import Devices

def main_devices(simulation: bool, filename: str):

    # create instance of Devices
    my_devices: Devices = Devices(simulation, filename)
    data_read, successful = my_devices.load_data()
    if not successful: 
        print(data_read)

if __name__ == "__main__":
    # Kommandozeilen Argumente verarbeiten
    parser = argparse.ArgumentParser(description="Netzwerkmanagement")
    parser.add_argument('--simulation', action='store_true', help="Enable simulation mode (= sample data, without netmiko calls)")
    parser.add_argument('filename', type=str, nargs='?', default='devices.json', help="Path to the components' file (default: devices.json)")
    args = parser.parse_args()
    
    main_devices(args.simulation, args.filename)