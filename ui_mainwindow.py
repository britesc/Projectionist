# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow:
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 500)
        MainWindow.setMinimumSize(QSize(630, 500))
        self.widgetCentral = QWidget(MainWindow)
        self.widgetCentral.setObjectName(u"widgetCentral")
        self.verticalLayoutWidgetCentral = QVBoxLayout(self.widgetCentral)
        self.verticalLayoutWidgetCentral.setObjectName(u"verticalLayoutWidgetCentral")
        self.horizontalLayoutWidgetCentral = QHBoxLayout()
        self.horizontalLayoutWidgetCentral.setObjectName(u"horizontalLayoutWidgetCentral")
        self.tabWidgetCentral = QTabWidget(self.widgetCentral)
        self.tabWidgetCentral.setObjectName(u"tabWidgetCentral")

        self.horizontalLayoutWidgetCentral.addWidget(self.tabWidgetCentral)


        self.verticalLayoutWidgetCentral.addLayout(self.horizontalLayoutWidgetCentral)

        MainWindow.setCentralWidget(self.widgetCentral)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 630, 22))
        self.menuBar.setAcceptDrops(False)
        MainWindow.setMenuBar(self.menuBar)
        self.toolBarPrimary = QToolBar(MainWindow)
        self.toolBarPrimary.setObjectName(u"toolBarPrimary")
        self.toolBarPrimary.setMinimumSize(QSize(0, 48))
        self.toolBarPrimary.setBaseSize(QSize(0, 0))
        self.toolBarPrimary.setMovable(False)
        self.toolBarPrimary.setAllowedAreas(Qt.TopToolBarArea)
        self.toolBarPrimary.setIconSize(QSize(48, 48))
        self.toolBarPrimary.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBarPrimary)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Projectionist", None))
        self.toolBarPrimary.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

