# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(233, 396)
        self.gridLayoutWidget = QWidget(MainWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 90, 231, 321))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button8 = QPushButton(self.gridLayoutWidget)
        self.button8.setObjectName(u"button8")

        self.gridLayout.addWidget(self.button8, 1, 1, 1, 1)

        self.button5 = QPushButton(self.gridLayoutWidget)
        self.button5.setObjectName(u"button5")

        self.gridLayout.addWidget(self.button5, 2, 1, 1, 1)

        self.button3 = QPushButton(self.gridLayoutWidget)
        self.button3.setObjectName(u"button3")

        self.gridLayout.addWidget(self.button3, 3, 2, 1, 1)

        self.button6 = QPushButton(self.gridLayoutWidget)
        self.button6.setObjectName(u"button6")

        self.gridLayout.addWidget(self.button6, 2, 2, 1, 1)

        self.button7 = QPushButton(self.gridLayoutWidget)
        self.button7.setObjectName(u"button7")

        self.gridLayout.addWidget(self.button7, 1, 0, 1, 1)

        self.buttonEnt = QPushButton(self.gridLayoutWidget)
        self.buttonEnt.setObjectName(u"buttonEnt")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.buttonEnt.sizePolicy().hasHeightForWidth())
        self.buttonEnt.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.buttonEnt, 3, 3, 2, 1)

        self.buttonDiv = QPushButton(self.gridLayoutWidget)
        self.buttonDiv.setObjectName(u"buttonDiv")

        self.gridLayout.addWidget(self.buttonDiv, 0, 1, 1, 1)

        self.button1 = QPushButton(self.gridLayoutWidget)
        self.button1.setObjectName(u"button1")

        self.gridLayout.addWidget(self.button1, 3, 0, 1, 1)

        self.buttonPlus = QPushButton(self.gridLayoutWidget)
        self.buttonPlus.setObjectName(u"buttonPlus")
        sizePolicy.setHeightForWidth(self.buttonPlus.sizePolicy().hasHeightForWidth())
        self.buttonPlus.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.buttonPlus, 1, 3, 2, 1)

        self.buttonMin = QPushButton(self.gridLayoutWidget)
        self.buttonMin.setObjectName(u"buttonMin")

        self.gridLayout.addWidget(self.buttonMin, 0, 3, 1, 1)

        self.button9 = QPushButton(self.gridLayoutWidget)
        self.button9.setObjectName(u"button9")

        self.gridLayout.addWidget(self.button9, 1, 2, 1, 1)

        self.button4 = QPushButton(self.gridLayoutWidget)
        self.button4.setObjectName(u"button4")

        self.gridLayout.addWidget(self.button4, 2, 0, 1, 1)

        self.buttonCCE = QPushButton(self.gridLayoutWidget)
        self.buttonCCE.setObjectName(u"buttonCCE")

        self.gridLayout.addWidget(self.buttonCCE, 0, 0, 1, 1)

        self.buttonCom = QPushButton(self.gridLayoutWidget)
        self.buttonCom.setObjectName(u"buttonCom")

        self.gridLayout.addWidget(self.buttonCom, 4, 2, 1, 1)

        self.button2 = QPushButton(self.gridLayoutWidget)
        self.button2.setObjectName(u"button2")

        self.gridLayout.addWidget(self.button2, 3, 1, 1, 1)

        self.button0 = QPushButton(self.gridLayoutWidget)
        self.button0.setObjectName(u"button0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.button0, 4, 0, 1, 2)

        self.buttonMul = QPushButton(self.gridLayoutWidget)
        self.buttonMul.setObjectName(u"buttonMul")

        self.gridLayout.addWidget(self.buttonMul, 0, 2, 1, 1)

        self.lcdNumber = QLCDNumber(MainWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(0, 0, 231, 91))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.lcdNumber.setProperty("intValue", 0)

        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Calculator", None))
        self.button8.setText(QCoreApplication.translate("MainWidget", u"8", None))
        self.button5.setText(QCoreApplication.translate("MainWidget", u"5", None))
        self.button3.setText(QCoreApplication.translate("MainWidget", u"3", None))
        self.button6.setText(QCoreApplication.translate("MainWidget", u"6", None))
        self.button7.setText(QCoreApplication.translate("MainWidget", u"7", None))
        self.buttonEnt.setText(QCoreApplication.translate("MainWidget", u"Enter", None))
        self.buttonDiv.setText(QCoreApplication.translate("MainWidget", u"/", None))
        self.button1.setText(QCoreApplication.translate("MainWidget", u"1", None))
        self.buttonPlus.setText(QCoreApplication.translate("MainWidget", u"+", None))
        self.buttonMin.setText(QCoreApplication.translate("MainWidget", u"-", None))
        self.button9.setText(QCoreApplication.translate("MainWidget", u"9", None))
        self.button4.setText(QCoreApplication.translate("MainWidget", u"4", None))
        self.buttonCCE.setText(QCoreApplication.translate("MainWidget", u"C ( CE)", None))
        self.buttonCom.setText(QCoreApplication.translate("MainWidget", u",", None))
        self.button2.setText(QCoreApplication.translate("MainWidget", u"2", None))
        self.button0.setText(QCoreApplication.translate("MainWidget", u"0", None))
        self.buttonMul.setText(QCoreApplication.translate("MainWidget", u"*", None))
    # retranslateUi

