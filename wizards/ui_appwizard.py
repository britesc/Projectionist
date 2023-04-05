# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appwizard.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import buttonsGlassRound_rc

class Ui_dialogAppWizard(object):
    def setupUi(self, dialogAppWizard) -> None:
        if not dialogAppWizard.objectName():
            dialogAppWizard.setObjectName(u"dialogAppWizard")
        dialogAppWizard.setWindowModality(Qt.ApplicationModal)
        dialogAppWizard.resize(520, 345)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogAppWizard.sizePolicy().hasHeightForWidth())
        dialogAppWizard.setSizePolicy(sizePolicy)
        dialogAppWizard.setMinimumSize(QSize(520, 345))
        dialogAppWizard.setMaximumSize(QSize(520, 345))
        icon = QIcon()
        icon.addFile(u"../resources/buttons/glassRound/glassButtonWizard.png", QSize(), QIcon.Normal, QIcon.Off)
        dialogAppWizard.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(dialogAppWizard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, -1)
        self.labelWizardPixmap = QLabel(dialogAppWizard)
        self.labelWizardPixmap.setObjectName(u"labelWizardPixmap")
        self.labelWizardPixmap.setMaximumSize(QSize(96, 96))
        self.labelWizardPixmap.setPixmap(QPixmap(u":/glassRound/glassButtonWizard.png"))
        self.labelWizardPixmap.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.labelWizardPixmap)

        self.labelApplicationsInfo = QLabel(dialogAppWizard)
        self.labelApplicationsInfo.setObjectName(u"labelApplicationsInfo")
        self.labelApplicationsInfo.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.labelApplicationsInfo)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(dialogAppWizard)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(dialogAppWizard)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(dialogAppWizard)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(dialogAppWizard)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(dialogAppWizard)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(dialogAppWizard)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(dialogAppWizard)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(dialogAppWizard)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 5, -1)
        self.progressBarApplicatios = QProgressBar(dialogAppWizard)
        self.progressBarApplicatios.setObjectName(u"progressBarApplicatios")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBarApplicatios.sizePolicy().hasHeightForWidth())
        self.progressBarApplicatios.setSizePolicy(sizePolicy1)
        self.progressBarApplicatios.setCursor(QCursor(Qt.WaitCursor))
        self.progressBarApplicatios.setValue(50)
        self.progressBarApplicatios.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBarApplicatios)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButtonCancel = QPushButton(dialogAppWizard)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        icon1 = QIcon()
        icon1.addFile(u":/glassRound/glassButtonCancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCancel.setIcon(icon1)
        self.pushButtonCancel.setIconSize(QSize(28, 28))
        self.pushButtonCancel.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.pushButtonCancel)

        self.pushButtonStart = QPushButton(dialogAppWizard)
        self.pushButtonStart.setObjectName(u"pushButtonStart")
        icon2 = QIcon()
        icon2.addFile(u":/glassRound/glassButtonStart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonStart.setIcon(icon2)
        self.pushButtonStart.setIconSize(QSize(28, 28))
        self.pushButtonStart.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.pushButtonStart)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(dialogAppWizard)

        QMetaObject.connectSlotsByName(dialogAppWizard)
    # setupUi

    def retranslateUi(self, dialogAppWizard) -> None:
        dialogAppWizard.setWindowTitle(QCoreApplication.translate("dialogAppWizard", u"Applications Wizard", None))
        self.labelWizardPixmap.setText("")
        self.labelApplicationsInfo.setText(QCoreApplication.translate("dialogAppWizard", u"When you are ready, please pess the Start Button, which will then open a dialog box to find the file applicationsneeded.yaml. It will then check to ensure that it is the desired file and then automatically attempt to find the applications neccessary for Projectionist to run properly.", None))
        self.label_2.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("dialogAppWizard", u"TextLabel", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("dialogAppWizard", u"Cancel", None))
        self.pushButtonStart.setText(QCoreApplication.translate("dialogAppWizard", u"Start", None))
    # retranslateUi

