from devices import Devices
from Native_Command import Native_Command
from main_view import Frm_Main
import PortSecurityTEST

class Controller():
     def __init__(self, gui_view: Frm_Main, simulation: bool, filename: str): 

        self.simulation = simulation 
        self.gui_view = gui_view

        self.filename = filename  
        self.model_native_command = Native_Command()

        self.data_model = Devices(self.simulation, self.filename)

        data_read, successful = self.data_model.load_data()

        # register my eventhandler at the View       
        #todo

        #aufruf portsecurityTest bei bedarf (in Evnthandlern)

















