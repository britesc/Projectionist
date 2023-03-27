#!/usr/bin/env python3
# coding: utf-8
from PyQt6.QtCore import QSettings, QCoreApplication


class J2_Settings:
    """ A Class for Settings """

    def __init__(self, OrgName, AppName) -> None:
        super().__init__()
        self.OrgName = OrgName
        self.AppName = AppName
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
        vVersion = "1.5.0"
        return vVersion

    def setDefaults(self) -> None:
        """ Set the defaults for settings """
        vTemp1 = v3JS.value("Window/Theme", False)
        if vTemp1 is False:
            v3JS.setValue("Window/Theme", "auto")

        vTemp1 = v3JS.value("Project/Folder", False)
        if vTemp1 is False:
            v3JS.setValue("Project/Folder", "")

        # vTemp1 = v3JS.value("Database/Folder", False)
        # if vTemp1 is False:
        #     v3JS.setValue("Database/Folder", "Naturism")

    def setSetting(self, Context, Value) -> None:
        """ Set the Setting """
        v3JS.setValue(Context, Value)

    def getSetting(self, Context, Default) -> str:
        """ Get the Setting """
        vTemp1 = v3JS.value(Context, Default)
        if vTemp1 is False:
            vTemp1 = ""
        return vTemp1
