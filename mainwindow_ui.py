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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QToolBar, QVBoxLayout, QWidget)
import buttonsGlassRound_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 500)
        MainWindow.setMinimumSize(QSize(630, 500))
        self.action_Toggle_Theme = QAction(MainWindow)
        self.action_Toggle_Theme.setObjectName(u"action_Toggle_Theme")
        icon = QIcon()
        icon.addFile(u":/glassRound/glassButtonTheme.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Toggle_Theme.setIcon(icon)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        icon1 = QIcon()
        icon1.addFile(u":/glassRound/glassButtonExit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Auto = QAction(MainWindow)
        self.action_Auto.setObjectName(u"action_Auto")
        self.action_Auto.setCheckable(True)
        self.action_Light = QAction(MainWindow)
        self.action_Light.setObjectName(u"action_Light")
        self.action_Light.setCheckable(True)
        self.action_Dark = QAction(MainWindow)
        self.action_Dark.setObjectName(u"action_Dark")
        self.action_Dark.setCheckable(True)
        self.action_Contents = QAction(MainWindow)
        self.action_Contents.setObjectName(u"action_Contents")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_About_Qt = QAction(MainWindow)
        self.action_About_Qt.setObjectName(u"action_About_Qt")
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
        self.menu_bar_All = QMenuBar(MainWindow)
        self.menu_bar_All.setObjectName(u"menu_bar_All")
        self.menu_bar_All.setGeometry(QRect(0, 0, 630, 22))
        self.menu_bar_All.setAcceptDrops(False)
        self.menu_File = QMenu(self.menu_bar_All)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menu_bar_All)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu_Theme = QMenu(self.menu_Edit)
        self.menu_Theme.setObjectName(u"menu_Theme")
        self.menu_Help = QMenu(self.menu_bar_All)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menu_bar_All)
        self.tool_bar_Basic = QToolBar(MainWindow)
        self.tool_bar_Basic.setObjectName(u"tool_bar_Basic")
        self.tool_bar_Basic.setMinimumSize(QSize(0, 0))
        self.tool_bar_Basic.setBaseSize(QSize(0, 48))
        self.tool_bar_Basic.setMovable(False)
        self.tool_bar_Basic.setAllowedAreas(Qt.TopToolBarArea)
        self.tool_bar_Basic.setIconSize(QSize(48, 48))
        self.tool_bar_Basic.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.tool_bar_Basic)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menu_bar_All.addAction(self.menu_File.menuAction())
        self.menu_bar_All.addAction(self.menu_Edit.menuAction())
        self.menu_bar_All.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.action_Exit)
        self.menu_Edit.addAction(self.menu_Theme.menuAction())
        self.menu_Theme.addAction(self.action_Auto)
        self.menu_Theme.addAction(self.action_Light)
        self.menu_Theme.addAction(self.action_Dark)
        self.menu_Help.addAction(self.action_Contents)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_About)
        self.menu_Help.addAction(self.action_About_Qt)
        self.tool_bar_Basic.addAction(self.action_Exit)
        self.tool_bar_Basic.addAction(self.action_Toggle_Theme)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Projectionist", None))
        self.action_Toggle_Theme.setText(QCoreApplication.translate("MainWindow", u"Toggle Theme", None))
#if QT_CONFIG(tooltip)
        self.action_Toggle_Theme.setToolTip(QCoreApplication.translate("MainWindow", u"Select Display Theme", None))
#endif // QT_CONFIG(tooltip)
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
#if QT_CONFIG(shortcut)
        self.action_Exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F4", None))
#endif // QT_CONFIG(shortcut)
        self.action_Auto.setText(QCoreApplication.translate("MainWindow", u"&Auto", None))
        self.action_Light.setText(QCoreApplication.translate("MainWindow", u"&Light", None))
        self.action_Dark.setText(QCoreApplication.translate("MainWindow", u"&Dark", None))
        self.action_Contents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
#if QT_CONFIG(shortcut)
        self.action_Contents.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"About...", None))
#if QT_CONFIG(shortcut)
        self.action_About.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_About_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt...", None))
#if QT_CONFIG(shortcut)
        self.action_About_Qt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menu_Theme.setTitle(QCoreApplication.translate("MainWindow", u"&Theme", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.tool_bar_Basic.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

