import qdarktheme

from PySide6.QtWidgets import (
    QWidget,
    QTabWidget,
    QFileDialog,
    QPushButton,
    QLineEdit 
)

from PySide6 import (
    QtCore,
    QtGui,
)
from PySide6.QtGui import QActionEvent
from tabs.ui_tab2setup import Ui_Tab2Setup

from classes._j2_settings import J2_Settings

class Tab2(QWidget, Ui_Tab2Setup):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonWizardProjectFolder.clicked.connect(self.loadTheFileDialog)

        
        # self.toolButtonWizardProjectFolder.clicked.connext        
        
    def loadTheFileDialog(self) -> None:
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEditDisplayProjectFolder.setText(folderpath)
        J2_Settings.setSetting(self, "Project/Folder", folderpath)
        