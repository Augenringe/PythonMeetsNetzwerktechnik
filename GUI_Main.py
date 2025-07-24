from PySide6.QtWidgets import QApplication
from main_view import Frm_Main             # View-Klasse importieren


def main():

    # create GUI Application
    app = QApplication()
    frm_main = Frm_Main()
    
    frm_main.show()
    app.exec()

if __name__ == "__main__":
        
    main()