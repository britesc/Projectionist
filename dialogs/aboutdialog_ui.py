# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import buttonsGlassRound_rc
import splash_rc

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        if not aboutDialog.objectName():
            aboutDialog.setObjectName(u"aboutDialog")
        aboutDialog.resize(500, 420)
        aboutDialog.setMinimumSize(QSize(500, 420))
        aboutDialog.setMaximumSize(QSize(500, 420))
        icon = QIcon()
        icon.addFile(u":/images/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(aboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelDialogTitle = QLabel(aboutDialog)
        self.labelDialogTitle.setObjectName(u"labelDialogTitle")
        self.labelDialogTitle.setMaximumSize(QSize(16777215, 48))
        self.labelDialogTitle.setLayoutDirection(Qt.LeftToRight)
        self.labelDialogTitle.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.labelDialogTitle)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelIconImage = QLabel(aboutDialog)
        self.labelIconImage.setObjectName(u"labelIconImage")
        self.labelIconImage.setMaximumSize(QSize(150, 150))
        self.labelIconImage.setPixmap(QPixmap(u":/resources/Images/png/splash.png"))
        self.labelIconImage.setScaledContents(True)
        self.labelIconImage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelIconImage)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelVersion = QLabel(aboutDialog)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelVersion)

        self.labelPython = QLabel(aboutDialog)
        self.labelPython.setObjectName(u"labelPython")
        self.labelPython.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelPython)

        self.labelPyside6 = QLabel(aboutDialog)
        self.labelPyside6.setObjectName(u"labelPyside6")
        self.labelPyside6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelPyside6)

        self.labelQtCoreVersion = QLabel(aboutDialog)
        self.labelQtCoreVersion.setObjectName(u"labelQtCoreVersion")
        self.labelQtCoreVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelQtCoreVersion)

        self.labelCreated = QLabel(aboutDialog)
        self.labelCreated.setObjectName(u"labelCreated")
        self.labelCreated.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelCreated)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(aboutDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(2)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(aboutDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButtonClose = QPushButton(aboutDialog)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        icon1 = QIcon()
        icon1.addFile(u":/glassRound/glassButtonClose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonClose.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushButtonClose)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(aboutDialog)

        QMetaObject.connectSlotsByName(aboutDialog)
    # setupUi

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QCoreApplication.translate("aboutDialog", u"About...", None))
        self.labelDialogTitle.setText(QCoreApplication.translate("aboutDialog", u"<html><head/><body><h2 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">About Projectionist</span></h2></body></html>", None))
        self.labelIconImage.setText("")
        self.labelVersion.setText(QCoreApplication.translate("aboutDialog", u"Application Version: Not Done", None))
        self.labelPython.setText(QCoreApplication.translate("aboutDialog", u"Python Version: Not Done", None))
        self.labelPyside6.setText(QCoreApplication.translate("aboutDialog", u"PySide6 Version: Not Done", None))
        self.labelQtCoreVersion.setText(QCoreApplication.translate("aboutDialog", u"Qt Core Version: Not Done", None))
        self.labelCreated.setText(QCoreApplication.translate("aboutDialog", u"Created: 02 February 2023 11:30:00", None))
        self.label_4.setText(QCoreApplication.translate("aboutDialog", u"Projectionist is a tool to assist in the Creation and Setup of various computer language projects.\n"
"Including:\n"
"Python, C, C++, Kotlin and Php amongst others.\n"
"\n"
"It was created by Julian Bourne for Personal Use.", None))
        self.label_2.setText(QCoreApplication.translate("aboutDialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:small; font-weight:700;\">Copyright J2Casa 2023. All Rights Reserved</span></p></body></html>", None))
        self.pushButtonClose.setText(QCoreApplication.translate("aboutDialog", u"&Close", None))
    # retranslateUi

