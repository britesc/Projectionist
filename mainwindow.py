
from PySide6.QtWidgets import (
    QMainWindow
) 

from ui_mainwindow import Ui_MainWindow

from classes._j2_settings import J2_Settings
from classes import setupclass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)
        self.app = app

## We need to check here if the project folder has been set
#  We need to check here that the required apps have been added to the .ini file
##
        vJ2S = J2_Settings("J2Casa", "Projectionist")
        vJ2S.setDefaults()
        vPFLocation = vJ2S.getSetting("Project/Folder", False)
        vPFApps = vJ2S.getSetting("Applications", False)

        
        if not vPFLocation:
            print("False - vPFLocation Not Set")
        else:
            print(vPFLocation)    

        if not vPFApps:
            print("False - vPFApps Not Set")
        else:
            print(vPFApps)    

        if not vPFLocation or not vPFApps:
            print("False - Only One or Neither of them set")
            setupclass.SetupClass(self, self.toolBarPrimary, self.tabWidgetCentral)
        else:
            print("True - Both of them set")
            setupclass.SetupClass(self, self.toolBarPrimary, self.tabWidgetCentral)
        
        
        
        
        