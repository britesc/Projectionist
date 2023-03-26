import qdarktheme

from PySide6.QtWidgets import QWidget, QTabWidget

from tabs import ui_tab2


class Tab2(QWidget, Ui_Tab2):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        