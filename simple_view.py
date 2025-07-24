from PySide6.QtWidgets import QMainWindow
from ui.UI import Ui_MainWindow

class Simple_Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectedDevice = 0


    def show_message(self, message: str):
        print(message)
        self.lbl_message.setText(message)

    def register_native_command_slot(self, event_handler):
        self.btn_command_go.clicked.connect(event_handler)
 
    def get_selected_device(self)->int:
        device_index: int = 0
        try:
            device_index = int(self.edt_component_id.text())
        except ValueError:
            print(f"Eingabe {ValueError} konnte nicht in einen Index gewandelt werden")
            device_index = 0

        return device_index

    def get_native_command(self) -> str:
        return self.edt_command.text()
    
    def clear_native_command(self, component: str):
        #self.ted_output.clear()
        self.lbl_component_native_command.setText(component)
    
    def setResult_native_command(self, result : str):
        self.ted_output.setText(result)



 