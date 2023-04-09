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
        self.J2_Settings = J2_Settings("J2Casa", "Projectionist")

        # Signals and Slots
        
        self.pushButtonWizardProjectFolder.clicked.connect(self.loadTheFileDialog)
        self.pushButtonWizardProjectFolder.setDefault(False)
        self.pushButtonWizardApplications.clicked.connect(self.loadTheAppWizard)
        self.pushButtonWizardApplications.setDefault(False)
        
        # Populate Home Folder Path            
        folderpath = self.J2_Settings.getSetting("Project/Folder", "")
        self.lineEditDisplayProjectFolder.setText(folderpath)
        
        # Populate Applications Wizard
        # Last Run
        textwhen = self.J2_Settings.getSetting("Applications/Date", "Never")
        self.labelTextLastRunWhen.setText(textwhen)
        yamlversion = self.J2_Settings.getSetting("Applications/Version", "0.0.0")
        self.labelTextVersionYAML.setText(yamlversion)
        appquantity = self.J2_Settings.getSetting("Applications/Quantity", "None")
        self.labelTextInstallledQuantity.setText(appquantity)



        
    def loadTheFileDialog(self) -> None:
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEditDisplayProjectFolder.setText(folderpath)
#        self.J2_Settings.setSetting(self, "Project/Folder", folderpath)
        self.J2_Settings.setSetting("Project/Folder", folderpath)
        
    def loadTheAppWizard(self) -> None:
        self.AppWizard.exec()