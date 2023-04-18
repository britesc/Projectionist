
import sys
import traceback
import qdarktheme

from PySide6.QtCore import (
    QSize,
    QObject,
    QSettings,
    QPoint
    
)    

from PySide6.QtGui import (
    QAction,
    QActionGroup,
    QIcon,
    QWindow
)    
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QToolBar,
    QPushButton,
    QStatusBar,
    QWidget,
    QTabWidget,
    QLabel,
    QMessageBox,
    QPushButton,
    QDialog,
    QMenuBar
)

from mainwindow_ui import Ui_MainWindow
from dialogs.aboutdialog import AboutDialog

import tabs.tab1setup
import tabs.tab2setup

from classes import (
    j2_settings,
)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self) # type: ignore
        self.app = app

        # print("")
        # print("1. mainwindow.py self.__dict__")
        # print(dir(self))
        # print("")
        # print("")        
        # exit()
        self.jSettings = j2_settings.J2_Settings()
        self.pfLocation = self.jSettings.getSetting("Project/Folder", "")
        self.pfApps =  self.jSettings.getSetting("Applications", "")
        self.aboutDialog = AboutDialog()
        self.qttheme = self.jSettings.getSetting("Window/Theme", "auto")
        self.tab1 = tabs.tab1setup.Tab1()
        self.tab2 = tabs.tab2setup.Tab2()
        self.Geometry = QWindow()
        self.Settings = QSettings()
        
        self.resize(self.Settings.value("Window/Size", QSize(630, 500))) # type: ignore

        
        
        # define the theme group
        self.themeGroup =  QActionGroup(self)
        self.themeGroup.addAction(self.action_Auto)
        self.themeGroup.addAction(self.action_Light)
        self.themeGroup.addAction(self.action_Dark)
        
        # define the main features of the window

        self.action_Toggle_Theme.triggered.connect(self.function_Toggle_Theme) # type: ignore

        self.action_Auto.triggered.connect(self.function_Auto_Theme) # type: ignore
        self.action_Light.triggered.connect(self.function_Light_Theme) # type: ignore
        self.action_Dark.triggered.connect(self.function_Dark_Theme) # type: ignore
        
        self.action_Contents.triggered.connect(self.function_Contents) # type: ignore
        
        self.action_About.triggered.connect(self.function_About) # type: ignore
        self.action_About_Qt.triggered.connect(self.function_About_Qt) # type: ignore
        
        self.action_Exit.triggered.connect(self.function_Exit)         # type: ignore
        
        # Decide if we show config or project windows
        #if not self.project_folder_defined() or not self.apps_quantity_found():
        self.tabWidgetCentral.addTab(self.tab1, "Information")
        self.tabWidgetCentral.addTab(self.tab2, "Configuration")

    def function_Toggle_Theme(self) -> None:
        
        # vMWTheme = V2JS.getSetting(self, "Window/Theme", "auto")
        match self.qttheme:
            case "auto":
                self.function_Dark_Theme()
            case "dark":
                self.function_Light_Theme()
            case "light":
                self.function_Auto_Theme()
            case _:
                self.function_Auto_Theme()
                

    def function_Auto_Theme(self) -> None:
        qdarktheme.setup_theme("auto")
        self.statusBar.showMessage("System Default Theme is being Used", 2000)
        self.jSettings.setSetting("Window/Theme", "auto")
        self.action_Auto.setChecked(True)
        self.qttheme = "auto"

    
    def function_Light_Theme(self) -> None:
        qdarktheme.setup_theme("light")
        self.statusBar.showMessage("System Light Theme is being Used", 2000)
        self.jSettings.setSetting("Window/Theme", "light")        
        self.action_Light.setChecked(True)
        self.qttheme = "light"


    def function_Dark_Theme(self) -> None:
        qdarktheme.setup_theme("dark")
        self.statusBar.showMessage("System Dark Theme is being Used", 2000)
        self.jSettings.setSetting("Window/Theme", "dark")        
        self.action_Dark.setChecked(True)
        self.qttheme = "dark"

    
    def function_Contents(self) -> None:
        pass
    
    def function_About(self) -> None:
        self.aboutDialog.exec()
    
    def function_About_Qt(self) -> None:
        QApplication.aboutQt()
    
    def function_Exit(self) -> None:
        dlg = QMessageBox()
        dlg.setWindowTitle("Exit the Application")
        dlg.setText("Do you wish to exit the Applications?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            self.Settings.setValue("Window/Size", self.size())         
            sys.exit()
 
                    
    def closeEvent(self, event) -> None:
        # print "User has clicked the red x on the main window"
            event.ignore()
            self.function_Exit()  
                   

    def project_folder_defined(self) -> str:
        return self.jSettings.getProjectFolder()
    
    def apps_quantity_found(self)  -> int:
        return self.jSettings.getHeaderQuantity()

# ## We need to check here if the project folder has been set
# #  We need to check here that the required apps have been added to the .ini file
# ##

        
#         # if not vPFLocation:
#         #     print("False - vPFLocation Not Set")
#         # else:
#         #     print(vPFLocation)    

#         # if not vPFApps:
#         #     print("False - vPFApps Not Set")
#         # else:
#         #     print(vPFApps)    

#         # if not self.pfLocation or not self.pfApps:
#             # print("False - Only One or Neither of them set")
#             # setupclass.SetupClass(self, self.toolBarPrimary, self.tabWidgetCentral)
#             # setupclass.SetupClass()
#         # else:
#             # print("True - Both of them set")
#             # setupclass.SetupClass(self, self.toolBarPrimary, self.tabWidgetCentral)
#         # self.basesetup = basesetup.BaseSetup()

        