from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from ui.UI import Ui_MainWindow

class Frm_Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_components.setRowCount(1)
        self.tbl_components.setColumnCount(4)
        self.tbl_components.setHorizontalHeaderLabels(["Host","Hostname", "User", "Device-Type"])
        self.tbl_components.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_components.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_components.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        
        self.tbl_components_2.setRowCount(1)
        self.tbl_components_2.setColumnCount(4)
        self.tbl_components_2.setHorizontalHeaderLabels(["Host","Hostname", "User", "Device-Type"])
        self.tbl_components_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_components_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_components_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
  

    def show_devices(self, data):
        self.tbl_components.setRowCount(len(data))
        for row in range(len(data)):
            item_host = QTableWidgetItem(data[row][0])
            item_host_name = QTableWidgetItem(data[row][1])
            item_user = QTableWidgetItem(data[row][2])
            item_type= QTableWidgetItem(data[row][3])
            self.tbl_components.setItem(row, 0, item_host)
            self.tbl_components.setItem(row, 1, item_host_name)
            self.tbl_components.setItem(row, 2, item_user)
            self.tbl_components.setItem(row, 3, item_type)
        self.tbl_components.show()

