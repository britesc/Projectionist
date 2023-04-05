#!/usr/bin/env python3
# coding: utf-8
from PyQt6.QtCore import QSettings, QCoreApplication


class J2_Settings():
    """ A Class for Settings """

    def __init__(self, OrgName, AppName) -> None:
        super().__init__()
        self.OrgName = OrgName
        self.AppName = AppName
        self.version = "1.6.1"
        QCoreApplication.setOrganizationName(OrgName)
        QCoreApplication.setApplicationName(AppName)
        global v3JS
        v3JS = QSettings()

    def __str__(self) -> str:
        """ The __str__ Function """
        return "J2_Settings"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "J2_Settings"

    def getVersion(self) -> str:
        """ The Version String of this Class """
        return self.version

    def setDefaults(self) -> None:
        """ Set the defaults for settings """
        vTemp1 = v3JS.value("Window/Theme", False)
        if vTemp1 is False:
            v3JS.setValue("Window/Theme", "auto")

        vTemp1 = v3JS.value("Project/Folder", False)
        if vTemp1 is False:
            v3JS.setValue("Project/Folder", "")

        vTemp1 = v3JS.value("Window/Splash", False)
        if vTemp1 is False:
            v3JS.setValue("Window/Splash", "True")
        
        v3JS.beginGroup("Applications")
        # v3JS.setValue("size", "Naked")
        # v3JS.setValue("fullScreen", "Nude")
        # v3JS.endGroup()
        v3JS.beginGroup("Apps")
        v3JS.beginGroup("Awk")
        v3JS.setValue("visible", "Bare")
        v3JS.setValue("clothing", "Nothing")        
        v3JS.endGroup()
        v3JS.endGroup()  
        v3JS.endGroup()      

    def setSetting(self, Context, Value) -> None:
        """ Set the Setting """
        v3JS.setValue(Context, Value)

    def getSetting(self, Context, Default) -> str:
        """ Get the Setting """
        vTemp1 = v3JS.value(Context, Default)
        if vTemp1 is False:
            vTemp1 = ""
        return vTemp1
