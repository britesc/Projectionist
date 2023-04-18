#!/usr/bin/env python3
# coding: utf-8

import sys
import PySide6
import PySide6.QtCore


from PyQt6.QtCore import (
    QCoreApplication
)

from PySide6.QtWidgets import (
    QDialog
)  

from dialogs.aboutdialog_ui import Ui_aboutDialog


class AboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        

        self.AppVersion = QCoreApplication.applicationVersion()
        v = sys.version_info
        self.PythonVersion = f"{v[0]}.{v[1]}.{v[2]}"
        # self.PythonVersion = sys.api_version
        self.Pyside6Version = PySide6.__version__
        self.QtCoreVersion = PySide6.QtCore.__version__
                
        
        self.setWindowTitle("About Projectionist")
        
        vTemp1 = f"Application Version: {self.AppVersion}"
        self.labelVersion.setText(vTemp1)
        
        vTemp1 = f"Python Version: {self.PythonVersion}"
        self.labelPython.setText(vTemp1)        
        
        vTemp1 = f"PySide6 Version: {self.Pyside6Version}"
        self.labelPyside6.setText(vTemp1)    
        
        vTemp1 = f"Qt Core  Version: {self.QtCoreVersion}"
        self.labelQtCoreVersion.setText(vTemp1)              
                
        self.pushButtonClose.clicked.connect(self.close)

    def close(self) -> None:
        self.reject()
