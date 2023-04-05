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

from classes._j2_settings import J2_Settings
from classes._j2_splash import J2_Splash


from mainwindow import MainWindow   


def main() -> None:
    vApplicationName = os.path.splitext(os.path.basename(__file__))[0]
    
    
    try:
        app = QApplication(sys.argv)
        vJ2S = J2_Settings("J2Casa", "Projectionist")
        vJ2S.setDefaults()
        vSplash = vJ2S.getSetting("Window/Splash", "")
        if vSplash != "False":
            splash = J2_Splash(app)
            splash.show(10)
        qdarktheme.setup_theme()
        window = MainWindow(app)
        qdarktheme.__dict__
        window.show()
        if vSplash != "False":
            splash.hide(window)

    
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