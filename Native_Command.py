from netmiko import ConnectHandler, NetmikoTimeoutException, NetMikoAuthenticationException
from devices import Devices


class Native_Command ():
    """ The class is the model around ios-interfaces for a native command to one network component

    """

    def __init__(self):

        super().__init__()

    def do_command(self, device_data: Devices, device_idx: int, command: str):
        """ method returns dtaa retrieved from netmiko if command was successfully executed, 
        otherwise an error message
        returns a tuple of (result successful: bool)
        """
        result = ""
        rc_ok = True

        try:
            print("INFO: netmiko calling, pls. wait...")
            net_connect = ConnectHandler(
                host=device_data.get_host(device_idx),
                device_type=device_data.get_type(device_idx),
                username=device_data.get_user(device_idx),
                password=device_data.get_password(device_idx),
                secret='geheim')

            net_connect.enable()
            result = net_connect.send_command(command)

            net_connect.disconnect()

        except NetmikoTimeoutException:
            result = "Connection timed out..."
            rc_ok = False
            # no Retry logic here
        except NetMikoAuthenticationException:
            result = "Authentication failed, please check credentials."
            rc_ok = False
        except Exception as e:
            result = f"An unexpected error occurred: {str(e)}"
            rc_ok = False

        print(f"INFO: data retrieved from netmiko call=\n{result}")

        return str(result), rc_ok
