#!/usr/bin/env python3
# coding: utf-8

from PyQt6.QtCore import (
    QSettings,
    QCoreApplication,
    QSize, 
    QRect   
)    

from PySide6.QtGui import (
    QWindow
)
    
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget
)    

class J2_Geometry:
    """ A Class for Settings """
    def __init__(self) -> None:    
        super().__init__()
        

        self.OrgName = QCoreApplication.organizationName()
        self.AppName = QCoreApplication.applicationName()
        self.Version = QCoreApplication.applicationVersion()
        self.Domain  = QCoreApplication.organizationDomain()
        self.ClassVersion = "1.2.0"
        self.ClassName = "J2_Geometry" 
        self.Geometry = QWindow()
        self.Settings = QSettings()

        
        
        
    def __str__(self) -> str:
        """ The __str__ Function """
        return self.ClassName

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return self.ClassName

    def getClassVersion(self) -> str:
        """ The Version String of this Class """
        return self.ClassVersion               
    
    def saveWindowPos(self, window) -> None:

        vGeom = self.Geometry.geometry()
        print(f"geometry {vGeom}")
        self.Settings.setValue("Window/Geometry", vGeom) 
        vGeom = self.Geometry.position()
        print(f"position {vGeom}")
        self.Settings.setValue("Window/Position", vGeom)    
        print(f"Height {self.Geometry.height()}")     
        
    
    def readWindowPos(self) -> None:
        vGeom = self.Settings.value("Window/Geometry")
        print(f"geometry {vGeom}")
        self.Geometry.setGeometry(vGeom)
        vGeom = self.Settings.value("Window/Position")
        self.Geometry.setPosition(vGeom)
        print(f"position {vGeom}")