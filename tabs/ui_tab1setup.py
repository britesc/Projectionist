# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab1setup.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Tab1Setup(object):
    def setupUi(self, Tab1Setup) -> None:
        if not Tab1Setup.objectName():
            Tab1Setup.setObjectName(u"Tab1Setup")
        Tab1Setup.resize(476, 351)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Tab1Setup.sizePolicy().hasHeightForWidth())
        Tab1Setup.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Tab1Setup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayoutInfoTab = QGridLayout()
        self.gridLayoutInfoTab.setObjectName(u"gridLayoutInfoTab")
        self.labelInfoTitle = QLabel(Tab1Setup)
        self.labelInfoTitle.setObjectName(u"labelInfoTitle")
        self.labelInfoTitle.setAlignment(Qt.AlignCenter)

        self.gridLayoutInfoTab.addWidget(self.labelInfoTitle, 0, 0, 1, 1)

        self.labelInfoDetails = QLabel(Tab1Setup)
        self.labelInfoDetails.setObjectName(u"labelInfoDetails")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(98)
        sizePolicy1.setHeightForWidth(self.labelInfoDetails.sizePolicy().hasHeightForWidth())
        self.labelInfoDetails.setSizePolicy(sizePolicy1)
        self.labelInfoDetails.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelInfoDetails.setWordWrap(True)
        self.labelInfoDetails.setMargin(5)
        self.labelInfoDetails.setIndent(-4)

        self.gridLayoutInfoTab.addWidget(self.labelInfoDetails, 1, 0, 1, 1)

        self.labelInfoCopyright = QLabel(Tab1Setup)
        self.labelInfoCopyright.setObjectName(u"labelInfoCopyright")

        self.gridLayoutInfoTab.addWidget(self.labelInfoCopyright, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayoutInfoTab, 1, 1, 1, 1)


        self.retranslateUi(Tab1Setup)

        QMetaObject.connectSlotsByName(Tab1Setup)
    # setupUi

    def retranslateUi(self, Tab1Setup):
        Tab1Setup.setWindowTitle(QCoreApplication.translate("Tab1Setup", u"Tab", None))
#if QT_CONFIG(tooltip)
        Tab1Setup.setToolTip(QCoreApplication.translate("Tab1Setup", u"Tab Tool Tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Tab1Setup.setStatusTip(QCoreApplication.translate("Tab1Setup", u"Tab Status Tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Tab1Setup.setWhatsThis(QCoreApplication.translate("Tab1Setup", u"Tab Whats This", None))
#endif // QT_CONFIG(whatsthis)
        self.labelInfoTitle.setText(QCoreApplication.translate("Tab1Setup", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Projectionist</span></h1></body></html>", None))
#if QT_CONFIG(statustip)
        self.labelInfoDetails.setStatusTip(QCoreApplication.translate("Tab1Setup", u"Welcome Tab", None))
#endif // QT_CONFIG(statustip)
        self.labelInfoDetails.setText(QCoreApplication.translate("Tab1Setup", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Welcome to Projectionist.</span></h3><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">In order to make use of this excellent application it is first necessary to configure it.</span></h4><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">It may also be necessary to add applications to the OS $PATH Variable to ensure that they can be found and utilised correctly. This should be fairly easy to do.</span></h4><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:"
                        "700;\">Once you are ready to commence the configuration, please click on the Configuration Tab and follow the instructions.</span></h4><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:700;\">This application has been set to operate in a minimum size of 630 x 500, but can operate just as well or better in large sizes, imcluding full screen.</span></h4><p><br/></p></body></html>", None))
        self.labelInfoCopyright.setText(QCoreApplication.translate("Tab1Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:small; font-weight:700;\">Copyright J2Casa 2023. All Rights Reserved</span></p></body></html>", None))
    # retranslateUi

