import qdarktheme

from PySide6.QtWidgets import QWidget, QTabWidget

from tabs.ui_tab2setup import Ui_Tab2Setup


class Tab2(QWidget, Ui_Tab2Setup):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        