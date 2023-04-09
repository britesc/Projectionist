#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import qdarktheme
import traceback

from PyQt6.QtCore import QSettings, QCoreApplication

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)  

from classes import (
    j2_settings,
    j2_splash
)

from mainwindow import MainWindow   

def SetupApp() -> None:
    QCoreApplication.setOrganizationName("J2Casa")
    QCoreApplication.setOrganizationDomain("j2casa.com")
    QCoreApplication.setApplicationName("Projectionist")    
    QCoreApplication.setApplicationVersion("1.7.5")


def main() -> None:
    vApplicationName = os.path.splitext(os.path.basename(__file__))[0]
    
    try:
        # First we instatiate the App
        
        app = QApplication(sys.argv)
        # Them we instatiate the settings        
        
        PJ_Settings = j2_settings.J2_Settings()
        PJ_Settings.setDefaults()
        # Then we read the settigs to see if we need the Splash Screen
        PJ_ShowSplash = PJ_Settings.getSetting("Window/Splash", "")
        # We instatiate the Spalsh Screen
        PJ_Splash   = j2_splash.J2_Splash(app)
        
        # If setting says anything other than False we show the splash screen
        
        if PJ_ShowSplash != "False":
            PJ_Splash.show(10) # Currently 10 seconds

        # Then we setup the use of darktheme
        PJ_DarkTheme = qdarktheme.setup_theme()        
        
        # The we call the mainwindow script
        window = MainWindow(app)
        # qdarktheme.__dict__
        window.show()
        
        if PJ_ShowSplash != "False":
            PJ_Splash.hide(window)

    
    except Exception as err:
        print(f"Unfortunately {vApplicationName} has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception()

    finally:
        sys.exit(app.exec())


if __name__ == '__main__':
    SetupApp()
    main()    