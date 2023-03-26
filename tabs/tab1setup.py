import qdarktheme

from PySide6.QtWidgets import QWidget, QTabWidget

from tabs.ui_tab1setup import Ui_Tab1Setup


class Tab1(QWidget, Ui_Tab1Setup):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        