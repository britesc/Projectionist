#!/usr/bin/env python3
# coding: utf-8


from PySide6.QtWidgets import QDialog

from wizards.ui_appwizard import Ui_dialogAppWizard

class AppWizard(QDialog, Ui_dialogAppWizard):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Applications Wizard")
        
        self.pushButtonCancel.clicked.connect(self.close)
        self.pushButtonStart.clicked.connect(self.start)

    def close(self) -> None:
        self.reject()
        
    def start(self) -> None:
        pass