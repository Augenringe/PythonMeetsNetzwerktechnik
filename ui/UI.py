# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGroupBox,
    QHeaderView, QLabel, QListView, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 541))
        self.Datei = QWidget()
        self.Datei.setObjectName(u"Datei")
        self.pushButton_3 = QPushButton(self.Datei)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 10, 75, 24))
        self.pushButton_4 = QPushButton(self.Datei)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(100, 10, 75, 24))
        self.pushButton_5 = QPushButton(self.Datei)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(190, 10, 75, 24))
        self.tabWidget.addTab(self.Datei, "")
        self.TypeHere = QWidget()
        self.TypeHere.setObjectName(u"TypeHere")
        self.tableView = QTableView(self.TypeHere)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(50, 20, 256, 21))
        self.label = QLabel(self.TypeHere)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 71, 31))
        self.pushButton = QPushButton(self.TypeHere)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 480, 75, 24))
        self.buttonBox = QDialogButtonBox(self.TypeHere)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(630, 480, 161, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.tabWidget.addTab(self.TypeHere, "")
        self.Konfigurator = QWidget()
        self.Konfigurator.setObjectName(u"Konfigurator")
        self.pushButton_2 = QPushButton(self.Konfigurator)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 100, 75, 24))
        self.groupBox = QGroupBox(self.Konfigurator)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 240, 761, 231))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 71, 16))
        self.tableView_3 = QTableView(self.groupBox)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setGeometry(QRect(80, 20, 256, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 71, 16))
        self.tableView_4 = QTableView(self.groupBox)
        self.tableView_4.setObjectName(u"tableView_4")
        self.tableView_4.setGeometry(QRect(80, 60, 256, 21))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 60, 71, 16))
        self.pushButton_10 = QPushButton(self.groupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(160, 100, 75, 24))
        self.listView_2 = QListView(self.groupBox)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(480, 30, 256, 192))
        self.pushButton_6 = QPushButton(self.Konfigurator)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 480, 75, 24))
        self.pushButton_7 = QPushButton(self.Konfigurator)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(100, 480, 75, 24))
        self.pushButton_8 = QPushButton(self.Konfigurator)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(180, 480, 91, 24))
        self.pushButton_9 = QPushButton(self.Konfigurator)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(280, 480, 75, 24))
        self.progressBar = QProgressBar(self.Konfigurator)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(260, 160, 251, 23))
        self.progressBar.setValue(24)
        self.tbl_components = QTableWidget(self.Konfigurator)
        self.tbl_components.setObjectName(u"tbl_components")
        self.tbl_components.setGeometry(QRect(0, 20, 256, 192))
        self.listView = QListView(self.Konfigurator)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(530, 10, 256, 192))
        self.tabWidget.addTab(self.Konfigurator, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tbl_components_2 = QTableWidget(self.tab)
        self.tbl_components_2.setObjectName(u"tbl_components_2")
        self.tbl_components_2.setGeometry(QRect(0, 0, 791, 511))
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Datei), QCoreApplication.translate("MainWindow", u"Datei", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TypeHere), QCoreApplication.translate("MainWindow", u"TypeHere", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Health-Check", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soll Version:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max Uptime: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stunden", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u" Check ->", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u00c4ndern", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"AutoKonfig", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"CyberSec Test", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Konfigurator), QCoreApplication.translate("MainWindow", u"Konfigurator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Ger\u00e4te im Netz", None))
    # retranslateUi

