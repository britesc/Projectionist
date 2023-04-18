#!/usr/bin/env python3
# coding: utf-8

from pathlib import Path

from PyQt6.QtCore import (
    QSettings,
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    Qt,
    QSize    
)    

class J2_Settings:
    """ A Class for Settings """
    def __init__(self) -> None:    
        super().__init__()
        self.OrgName = QCoreApplication.organizationName()
        self.AppName = QCoreApplication.applicationName()
        self.Version = QCoreApplication.applicationVersion()
        self.Domain  = QCoreApplication.organizationDomain()
        self.ClassVersion = "1.2.0"
        self.jSettings = QSettings()

        # print(f"organizationName {self.OrgName}")
        # print(f"organizationDomain {self.Domain}")
        # print(f"applicationName {self.AppName}")
        # print(f"applicationName {self.Version}")
        # exit()


    def __str__(self) -> str:
        """ The __str__ Function """
        return "J2_Settings"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "J2_Settings"

    def getClassVersion(self) -> str:
        """ The Version String of this Class """
        return self.ClassVersion

    def setDefaults(self) -> None:
        """ Set the defaults for settings """
        if not self.jSettings.value("Window/Theme", ""):
            self.jSettings.setValue("Window/Theme", "auto")

        if not self.jSettings.value("Project/Folder", ""):
            self.jSettings.setValue("Project/Folder", "")

        if not self.jSettings.value("Window/Splash", ""):
            self.jSettings.setValue("Window/Splash", "True")
        
        # v3JS.beginGroup("Applications")
        # # v3JS.setValue("size", "Naked")
        # # v3JS.setValue("fullScreen", "Nude")
        # # v3JS.endGroup()
        # v3JS.beginGroup("Apps")
        # v3JS.beginGroup("Awk")
        # v3JS.setValue("visible", "Bare")
        # v3JS.setValue("clothing", "Nothing")        
        # v3JS.endGroup()
        # v3JS.endGroup()  
        # v3JS.endGroup()      

    def setSetting(self, Context: str, Value: str) -> None:
        """ Set the Setting """
        self.jSettings.setValue(Context, Value)

    def getSetting(self, Context: str, Default: str) -> str:
        """ Get the Setting """
        # vTemp1 = v3JS.value(Context, Default)
        # if vTemp1 is False:
        #     vTemp1 = ""
        return self.jSettings.value(Context, Default, str)
    
    def getProjectFolder(self) -> str:
        temp = Path(self.jSettings.value("Project/Folder", "", str))
        return self.jSettings.value("Project/Folder", "", str) if temp.is_dir() else ""
    
    def getHeaderQuantity(self) -> int:
        return self.jSettings.value("Header/Quantity", 0, int)
    
    def getHeaderDate(self) -> str:
        temp1 = self.jSettings.value("Header/Date", 0, int)
        return QDate.fromJulianDay(temp1).toString()

    def getHeaderVersion(self) -> str:
        return self.jSettings.value("Header/Version", "", str)
    
