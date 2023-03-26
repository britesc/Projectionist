
from PySide6.QtWidgets import (
    QMainWindow
) 

from PySide6 import (
    QtCore,
    QtCore,
    QtGui
)

from ui_mainwindow import Ui_MainWindow

from classes import setupclass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)
        self.app = app

        
        setupclass.SetupClass(self, self.toolBarPrimary, self.tabWidgetCentral)
        
        
        
        
        