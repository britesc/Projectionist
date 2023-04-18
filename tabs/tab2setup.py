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

from classes.j2_settings import J2_Settings
from wizards.appwizard import AppWizard

class Tab2(QWidget, Ui_Tab2Setup):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.AppWizard = AppWizard()    
        self.J2_Settings = J2_Settings()
        self.ProjectFolder = self.J2_Settings.getSetting("Project/Folder", "")
        self.HeaderDate = self.J2_Settings.getHeaderDate()
        self.YamlVersion = self.J2_Settings.getHeaderVersion()
        self.AppQuantity = self.J2_Settings.getHeaderQuantity()
        self.AppQuantityString = str(self.AppQuantity)
        self.FolderPath = self.J2_Settings.getProjectFolder()
        
                
        # Populate Home Folder Path                    
        self.lineEditDisplayProjectFolder.setText(self.ProjectFolder)
        
        # Populate Applications Wizard
        # Last Run
        self.labelTextLastRunWhen.setText(self.HeaderDate)
        self.labelTextVersionYAML.setText(self.YamlVersion)
        self.labelTextInstalledQuantity.setText(self.AppQuantityString)

        # Signals and Slots
        
        self.pushButtonWizardProjectFolder.clicked.connect(self.loadTheFileDialog)
        self.pushButtonWizardProjectFolder.setDefault(False)
        self.pushButtonWizardApplications.clicked.connect(self.loadTheAppWizard)
        self.pushButtonWizardApplications.setDefault(False)

        
    def loadTheFileDialog(self) -> None:
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.J2_Settings.setSetting("Project/Folder", folderpath)
        self.lineEditDisplayProjectFolder.setText(self.ProjectFolder)       
                
    def loadTheAppWizard(self) -> None:
        self.AppWizard.exec()