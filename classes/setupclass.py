import sys
import traceback

from PySide6.QtCore import (
    QSize,
    QObject
)    

from PySide6.QtGui import (
    QAction,
    QIcon
)    
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QPushButton,
    QStatusBar,
    QWidget,
    QTabWidget,
    QLabel,
    QMessageBox,
    QPushButton,
    QDialog
)    

import buttonsGlassRound_rc

from tabs.tab1setup import Tab1
from tabs.tab2setup import Tab2
 
class SetupClass():
    def __init__(self, mainWindow: QMainWindow, tb, tw) -> None:
        super().__init__()
        self.toolBarPrimary = tb
        self.toolBarPrimary.setObjectName(u"toolBarPrimary")
        self.toolBarPrimary.setMinimumSize(QSize(0, 48))
        self.toolBarPrimary.setBaseSize(QSize(0, 0))
        self.toolBarPrimary.setMovable(False)
        self.toolBarPrimary.setIconSize(QSize(48, 48))
        self.toolBarPrimary.setFloatable(False)
                
        self.tabWidget = tw
        
        menubar = mainWindow.menuBar
        file_menu = menubar.addMenu("&File")
        edit_menu = menubar.addMenu("&Edit")
        help_menu = menubar.addMenu("&Help")
        
        action_exit = QAction(QIcon(u"resources/buttons/glassRound/glassButtonExit.png"), "E&xit", mainWindow)
        action_exit.setStatusTip("Exit the Application")
        action_exit.setShortcut("Alt+X")
        self.toolBarPrimary.addAction(action_exit)
        file_menu.addSeparator()
        file_menu.addAction(action_exit)
        action_exit.triggered.connect(SetupClass.Response_Exit)
        
        taba1 = Tab1()
        tw.addTab(taba1, "Information")
        
        taba2 = Tab2()
        tw.addTab(taba2, "Configuration")        
        
        
    def Response_Exit() -> None:
        dlg = QMessageBox()
        dlg.setWindowTitle("Exit the Application")
        dlg.setText("Do you wish to exit the Applications?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            sys.exit()
        else:
            pass        