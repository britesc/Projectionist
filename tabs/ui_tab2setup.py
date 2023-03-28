# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab2setup.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import buttonsGlassRound_rc

class Ui_Tab2Setup(object):
    def setupUi(self, Tab2Setup):
        if not Tab2Setup.objectName():
            Tab2Setup.setObjectName(u"Tab2Setup")
        Tab2Setup.resize(476, 351)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Tab2Setup.sizePolicy().hasHeightForWidth())
        Tab2Setup.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Tab2Setup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayoutConfigTab = QGridLayout()
        self.gridLayoutConfigTab.setObjectName(u"gridLayoutConfigTab")
        self.groupBoxProjectFolder = QGroupBox(Tab2Setup)
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
        self.lineEditDisplayProjectFolder.setReadOnly(True)

        self.verticalLayoutlineEditDisplayProjectFolder.addWidget(self.lineEditDisplayProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutlineEditDisplayProjectFolder)

        self.verticalLayoutButtonsProjectFolder = QVBoxLayout()
        self.verticalLayoutButtonsProjectFolder.setObjectName(u"verticalLayoutButtonsProjectFolder")
        self.horizontalLayoutButtonsProjectFolder = QHBoxLayout()
        self.horizontalLayoutButtonsProjectFolder.setObjectName(u"horizontalLayoutButtonsProjectFolder")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonsProjectFolder.addItem(self.horizontalSpacer)

        self.pushButtonWizardProjectFolder = QPushButton(self.groupBoxProjectFolder)
        self.pushButtonWizardProjectFolder.setObjectName(u"pushButtonWizardProjectFolder")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonWizardProjectFolder.sizePolicy().hasHeightForWidth())
        self.pushButtonWizardProjectFolder.setSizePolicy(sizePolicy2)
        self.pushButtonWizardProjectFolder.setMinimumSize(QSize(48, 48))
        self.pushButtonWizardProjectFolder.setMaximumSize(QSize(48, 48))
        icon = QIcon()
        icon.addFile(u":/glassRound/glassButtonWizard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonWizardProjectFolder.setIcon(icon)
        self.pushButtonWizardProjectFolder.setIconSize(QSize(48, 48))
        self.pushButtonWizardProjectFolder.setFlat(True)

        self.horizontalLayoutButtonsProjectFolder.addWidget(self.pushButtonWizardProjectFolder)

        self.horizontalLayoutButtonsProjectFolder.setStretch(0, 97)

        self.verticalLayoutButtonsProjectFolder.addLayout(self.horizontalLayoutButtonsProjectFolder)


        self.verticalLayout_4.addLayout(self.verticalLayoutButtonsProjectFolder)


        self.gridLayoutConfigTab.addWidget(self.groupBoxProjectFolder, 1, 0, 1, 1)

        self.labelConfigTitle = QLabel(Tab2Setup)
        self.labelConfigTitle.setObjectName(u"labelConfigTitle")
        self.labelConfigTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutConfigTab.addWidget(self.labelConfigTitle, 0, 0, 1, 1)

        self.labelConfigCopyright = QLabel(Tab2Setup)
        self.labelConfigCopyright.setObjectName(u"labelConfigCopyright")

        self.gridLayoutConfigTab.addWidget(self.labelConfigCopyright, 3, 0, 1, 1)

        self.groupBoxLocateApps = QGroupBox(Tab2Setup)
        self.groupBoxLocateApps.setObjectName(u"groupBoxLocateApps")
        sizePolicy1.setHeightForWidth(self.groupBoxLocateApps.sizePolicy().hasHeightForWidth())
        self.groupBoxLocateApps.setSizePolicy(sizePolicy1)

        self.gridLayoutConfigTab.addWidget(self.groupBoxLocateApps, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayoutConfigTab, 1, 1, 1, 1)


        self.retranslateUi(Tab2Setup)

        QMetaObject.connectSlotsByName(Tab2Setup)
    # setupUi

    def retranslateUi(self, Tab2Setup):
        Tab2Setup.setWindowTitle(QCoreApplication.translate("Tab2Setup", u"Tab", None))
#if QT_CONFIG(tooltip)
        Tab2Setup.setToolTip(QCoreApplication.translate("Tab2Setup", u"Tab Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Tab2Setup.setStatusTip(QCoreApplication.translate("Tab2Setup", u"Tab Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Tab2Setup.setWhatsThis(QCoreApplication.translate("Tab2Setup", u"Tab Whats This", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxProjectFolder.setTitle(QCoreApplication.translate("Tab2Setup", u"Project Folder Wizard", None))
        self.labelTextProjectFolder.setText(QCoreApplication.translate("Tab2Setup", u"Please use the Wizard to locate your Master Project Folder.", None))
        self.lineEditDisplayProjectFolder.setPlaceholderText(QCoreApplication.translate("Tab2Setup", u"Master Project Folder Location", None))
#if QT_CONFIG(tooltip)
        self.pushButtonWizardProjectFolder.setToolTip(QCoreApplication.translate("Tab2Setup", u"Location Wizard", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonWizardProjectFolder.setStatusTip(QCoreApplication.translate("Tab2Setup", u"Project Folder Location Wizard", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonWizardProjectFolder.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonWizardProjectFolder.setShortcut(QCoreApplication.translate("Tab2Setup", u"Ctrl+Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.labelConfigTitle.setText(QCoreApplication.translate("Tab2Setup", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Configuration</span></h1></body></html>", None))
        self.labelConfigCopyright.setText(QCoreApplication.translate("Tab2Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:small; font-weight:700;\">Copyright J2Casa 2023. All Rights Reserved</span></p></body></html>", None))
        self.groupBoxLocateApps.setTitle(QCoreApplication.translate("Tab2Setup", u"Applications Locations Wizard", None))
    # retranslateUi

