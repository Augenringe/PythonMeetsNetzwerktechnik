from simple_view import Simple_Main
from devices import Devices
from Native_Command import Native_Command


class Simple_Controller:
    def __init__(self, view: Simple_Main, simulation: bool, filename: str):
        super().__init__()

        self.gui_view = view
        self.simulation = simulation
        self.filename = filename
        self.model_native_command = Native_Command()

        # create data model for components and load data/components
        self.data_model = Devices(self.simulation, filename)
        data_read, successful = self.data_model.load_data()

        self.gui_view.show_message(data_read)
        title = "Befehle an Cisco-Netzwerkkomponenten senden"
        if self.simulation:
            self.gui_view.setWindowTitle(title + " - SIMULATION (= ohne netmiko, mit Beispieldaten)")
        else:
            self.gui_view.setWindowTitle(title)

        # register my eventhandler at the View
        self.gui_view.register_native_command_slot(self.execute_native_command)

    def execute_native_command(self):

        device_idx = self.gui_view.get_selected_device()

        # show componetn data
        component = self.data_model.get_device_data_as_str(device_idx)

        self.gui_view.clear_native_command(component)

        # execute command
        print("execute")
        success = False

        if self.simulation:
            # just show some sample/ nonsense data
            result = "simulation result"
            success = True
        else:
            result, success = self.model_native_command.do_command (self.data_model, device_idx, self.gui_view.get_native_command())

        print("back from command execution, success = ", success)

        # show result
        self.gui_view.setResult_native_command(result)


