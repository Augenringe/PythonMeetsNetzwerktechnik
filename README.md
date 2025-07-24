# PythonMeetsNetzwerktechnik
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/Augenringe/PythonMeetsNetzwerktechnik)

This repository contains a Python-based network management tool with a graphical user interface (GUI). It is designed to connect to network devices, load their configurations, and perform health checks. The application is built using PySide6 for the GUI and is intended to use Netmiko for network automation tasks.

## Features

*   **Graphical User Interface**: An intuitive GUI built with PySide6 for managing network devices.
*   **Device Inventory**: Loads network device information from a `devices.json` file.
*   **Device Management**: Displays device details such as Host, Hostname, User, and Device Type in a table view.
*   **Network Health Checks**: Includes functionality to perform health checks, such as verifying software versions and uptime.
*   **Configuration Management**: The UI includes components for configuring devices and running security tests.
*   **Soon Port Security Features for a Cisco Router**

## Setup and Installation

### Prerequisites
*   Python 3

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Augenringe/PythonMeetsNetzwerktechnik.git
    cd PythonMeetsNetzwerktechnik
    ```

2.  **Set up the environment:**

    a. **On Windows**, you can run the provided batch script which creates a virtual environment and installs the necessary packages:
    ```
    setup_environment.bat
    ```

    b. **Manual setup (for other operating systems or if you prefer):**
    
    *   Create and activate a virtual environment:
        ```bash
        # Create the virtual environment
        python -m venv venv

        # Activate on Windows
        .\venv\Scripts\activate

        # Activate on Linux/macOS
        source venv/bin/activate
        ```
    *   Install the required dependencies:
        ```bash
        pip install netmiko PySide6
        ```

## Configuration

The application loads its device list from the `devices.json` file. You can modify this file to include your own network devices. The file requires a specific JSON structure:

```json
{
  "devices": [
    {
      "host": "172.16.0.2",
      "hostname": "CSR1",
      "username": "admin",
      "password": "geheim",
      "device_type": "cisco_xe",
      "secret": "geheim"
    },
    {
      "host": "172.16.0.2",
      "hostname": "S1",
      "username": "admin",
      "password": "geheim",
      "device_type": "cisco_ios",
      "secret": "geheim"
    }
  ]
}
```

## Usage

1.  Ensure you have activated the virtual environment:
    ```bash
    # On Windows
    .\venv\Scripts\activate

    # On Linux/macOS
    source venv/bin/activate
    ```

2.  Run the main application:
    ```bash
    python GUI_Main.py
    ```
This will launch the PySide6 GUI window.

## Project Structure

*   `GUI_Main.py`: The main entry point to start the GUI application.
*   `main_view.py`: Contains the `Frm_Main` class which defines the application's main window and its logic.
*   `devices.py`: A class for loading and managing the network device list from `devices.json`.
*   `devices.json`: The default configuration file for the device inventory.
*   `main_devices.py`: A command-line script to load devices, supporting a simulation mode.
*   `setup_environment.bat`: A batch script for easy setup on Windows.
*   `ui/`: A directory containing the Qt Designer UI files and the generated Python UI code.
    *   `MainUI.ui`: The Qt Designer file defining the GUI layout.
    *   `UI.py`: The Python code generated from `MainUI.ui`.