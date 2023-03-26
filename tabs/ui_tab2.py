# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import buttonsGlassRound_rc

class Ui_Tab1(object):
    def setupUi(self, Tab1) -> None:
        if not Tab1.objectName():
            Tab1.setObjectName(u"Tab1")
        Tab1.resize(476, 351)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Tab1.sizePolicy().hasHeightForWidth())
        Tab1.setSizePolicy(sizePolicy)
        self.actionLocateProjectFolder = QAction(Tab1)
        self.actionLocateProjectFolder.setObjectName(u"actionLocateProjectFolder")
        icon = QIcon()
        icon.addFile(u":/resources/buttons/glassround/glassButtonFind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLocateProjectFolder.setIcon(icon)
        self.actionSaveProjectFolder = QAction(Tab1)
        self.actionSaveProjectFolder.setObjectName(u"actionSaveProjectFolder")
        icon1 = QIcon()
        icon1.addFile(u":/resources/buttons/glassround/glassButtonSave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveProjectFolder.setIcon(icon1)
        self.actionCancelProjectFolder = QAction(Tab1)
        self.actionCancelProjectFolder.setObjectName(u"actionCancelProjectFolder")
        icon2 = QIcon()
        icon2.addFile(u":/resources/buttons/glassround/glassButtonCancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCancelProjectFolder.setIcon(icon2)
        self.gridLayout = QGridLayout(Tab1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayoutConfigTab = QGridLayout()
        self.gridLayoutConfigTab.setObjectName(u"gridLayoutConfigTab")
        self.groupBoxProjectFolder = QGroupBox(Tab1)
        self.groupBoxProjectFolder.setObjectName(u"groupBoxProjectFolder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.groupBoxProjectFolder.sizePolicy().hasHeightForWidth())
        self.groupBoxProjectFolder.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupBoxProjectFolder)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayoutlabelTextProjectFolder = QVBoxLayout()
        self.verticalLayoutlabelTextProjectFolder.setObjectName(u"verticalLayoutlabelTextProjectFolder")
        self.labelTextProjectFolder = QLabel(self.groupBoxProjectFolder)
        self.labelTextProjectFolder.setObjectName(u"labelTextProjectFolder")

        self.verticalLayoutlabelTextProjectFolder.addWidget(self.labelTextProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutlabelTextProjectFolder)

        self.verticalLayoutlineEditDisplayProjectFolder = QVBoxLayout()
        self.verticalLayoutlineEditDisplayProjectFolder.setObjectName(u"verticalLayoutlineEditDisplayProjectFolder")
        self.lineEditDisplayProjectFolder = QLineEdit(self.groupBoxProjectFolder)
        self.lineEditDisplayProjectFolder.setObjectName(u"lineEditDisplayProjectFolder")

        self.verticalLayoutlineEditDisplayProjectFolder.addWidget(self.lineEditDisplayProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutlineEditDisplayProjectFolder)

        self.verticalLayoutButtonsProjectFolder = QVBoxLayout()
        self.verticalLayoutButtonsProjectFolder.setObjectName(u"verticalLayoutButtonsProjectFolder")
        self.horizontalLayoutButtonsProjectFolder = QHBoxLayout()
        self.horizontalLayoutButtonsProjectFolder.setObjectName(u"horizontalLayoutButtonsProjectFolder")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonsProjectFolder.addItem(self.horizontalSpacer)

        self.pushButtonLocateMasterProjectFolder = QPushButton(self.groupBoxProjectFolder)
        self.pushButtonLocateMasterProjectFolder.setObjectName(u"pushButtonLocateMasterProjectFolder")
        self.pushButtonLocateMasterProjectFolder.setIcon(icon)
        self.pushButtonLocateMasterProjectFolder.setIconSize(QSize(24, 24))

        self.horizontalLayoutButtonsProjectFolder.addWidget(self.pushButtonLocateMasterProjectFolder)

        self.pushButtonSaveMasterProjectFolder = QPushButton(self.groupBoxProjectFolder)
        self.pushButtonSaveMasterProjectFolder.setObjectName(u"pushButtonSaveMasterProjectFolder")
        self.pushButtonSaveMasterProjectFolder.setIcon(icon1)
        self.pushButtonSaveMasterProjectFolder.setIconSize(QSize(24, 24))

        self.horizontalLayoutButtonsProjectFolder.addWidget(self.pushButtonSaveMasterProjectFolder)

        self.pushButtonCancelMasterProjectsFolder = QPushButton(self.groupBoxProjectFolder)
        self.pushButtonCancelMasterProjectsFolder.setObjectName(u"pushButtonCancelMasterProjectsFolder")
        self.pushButtonCancelMasterProjectsFolder.setIcon(icon2)
        self.pushButtonCancelMasterProjectsFolder.setIconSize(QSize(24, 24))

        self.horizontalLayoutButtonsProjectFolder.addWidget(self.pushButtonCancelMasterProjectsFolder)

        self.horizontalLayoutButtonsProjectFolder.setStretch(0, 97)
        self.horizontalLayoutButtonsProjectFolder.setStretch(1, 1)
        self.horizontalLayoutButtonsProjectFolder.setStretch(2, 1)
        self.horizontalLayoutButtonsProjectFolder.setStretch(3, 1)

        self.verticalLayoutButtonsProjectFolder.addLayout(self.horizontalLayoutButtonsProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutButtonsProjectFolder)


        self.gridLayoutConfigTab.addWidget(self.groupBoxProjectFolder, 1, 0, 1, 1)

        self.labelConfigTitle = QLabel(Tab1)
        self.labelConfigTitle.setObjectName(u"labelConfigTitle")
        self.labelConfigTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutConfigTab.addWidget(self.labelConfigTitle, 0, 0, 1, 1)

        self.labelConfigCopyright = QLabel(Tab1)
        self.labelConfigCopyright.setObjectName(u"labelConfigCopyright")

        self.gridLayoutConfigTab.addWidget(self.labelConfigCopyright, 3, 0, 1, 1)

        self.groupBoxLocateApps = QGroupBox(Tab1)
        self.groupBoxLocateApps.setObjectName(u"groupBoxLocateApps")
        sizePolicy1.setHeightForWidth(self.groupBoxLocateApps.sizePolicy().hasHeightForWidth())
        self.groupBoxLocateApps.setSizePolicy(sizePolicy1)

        self.gridLayoutConfigTab.addWidget(self.groupBoxLocateApps, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayoutConfigTab, 1, 1, 1, 1)


        self.retranslateUi(Tab1)

        QMetaObject.connectSlotsByName(Tab1)
    # setupUi

    def retranslateUi(self, Tab1):
        Tab1.setWindowTitle(QCoreApplication.translate("Tab1", u"Tab", None))
#if QT_CONFIG(tooltip)
        Tab1.setToolTip(QCoreApplication.translate("Tab1", u"Tab Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Tab1.setStatusTip(QCoreApplication.translate("Tab1", u"Tab Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Tab1.setWhatsThis(QCoreApplication.translate("Tab1", u"Tab Whats This", None))
#endif // QT_CONFIG(whatsthis)
        self.actionLocateProjectFolder.setText(QCoreApplication.translate("Tab1", u"Locate", None))
#if QT_CONFIG(tooltip)
        self.actionLocateProjectFolder.setToolTip(QCoreApplication.translate("Tab1", u"Locate Project Master Folder", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionLocateProjectFolder.setShortcut(QCoreApplication.translate("Tab1", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveProjectFolder.setText(QCoreApplication.translate("Tab1", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSaveProjectFolder.setToolTip(QCoreApplication.translate("Tab1", u"Save Master Project Folder", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSaveProjectFolder.setShortcut(QCoreApplication.translate("Tab1", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCancelProjectFolder.setText(QCoreApplication.translate("Tab1", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.actionCancelProjectFolder.setToolTip(QCoreApplication.translate("Tab1", u"Cancel Amendments to Master Project Folder", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCancelProjectFolder.setShortcut(QCoreApplication.translate("Tab1", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.groupBoxProjectFolder.setTitle(QCoreApplication.translate("Tab1", u"Project Folder Wizard", None))
        self.labelTextProjectFolder.setText(QCoreApplication.translate("Tab1", u"Please select the location of your Project Folder Master", None))
        self.lineEditDisplayProjectFolder.setPlaceholderText(QCoreApplication.translate("Tab1", u"Project Folder Location", None))
#if QT_CONFIG(statustip)
        self.pushButtonLocateMasterProjectFolder.setStatusTip(QCoreApplication.translate("Tab1", u"Locate Master  Project Folder", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonLocateMasterProjectFolder.setText(QCoreApplication.translate("Tab1", u"Locate", None))
#if QT_CONFIG(shortcut)
        self.pushButtonLocateMasterProjectFolder.setShortcut(QCoreApplication.translate("Tab1", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.pushButtonSaveMasterProjectFolder.setText(QCoreApplication.translate("Tab1", u"Save", None))
#if QT_CONFIG(shortcut)
        self.pushButtonSaveMasterProjectFolder.setShortcut(QCoreApplication.translate("Tab1", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.pushButtonCancelMasterProjectsFolder.setText(QCoreApplication.translate("Tab1", u"Cancel", None))
#if QT_CONFIG(shortcut)
        self.pushButtonCancelMasterProjectsFolder.setShortcut(QCoreApplication.translate("Tab1", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.labelConfigTitle.setText(QCoreApplication.translate("Tab1", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Configuration</span></h1></body></html>", None))
        self.labelConfigCopyright.setText(QCoreApplication.translate("Tab1", u"<html><head/><body><p align=\"center\"><span style=\" font-size:small; font-weight:700;\">Copyright J2Casa 2023. All Rights Reserved</span></p></body></html>", None))
        self.groupBoxLocateApps.setTitle(QCoreApplication.translate("Tab1", u"Applications Locations Wizard", None))
    # retranslateUi

