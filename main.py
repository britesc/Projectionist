#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import qdarktheme
import traceback

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)  

from mainwindow import MainWindow   


def main() -> None:
    vApplicationName = os.path.splitext(os.path.basename(__file__))[0]
    
    
    try:
        app = QApplication(sys.argv)
        qdarktheme.setup_theme()
        window = MainWindow(app)
        qdarktheme.__dict__
        window.show()

    
    except Exception as err:
        print(f"Unfortunately {vApplicationName} has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception()

    finally:
        sys.exit(app.exec())


if __name__ == '__main__':
    main()    