# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'receptionezxDXZ.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc
import images_rc

class Ui_reception(object):
    def setupUi(self, reception):
        if not reception.objectName():
            reception.setObjectName(u"reception")
        reception.resize(1607, 929)
        reception.setStyleSheet(u"*{\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 3px 8px;\n"
"\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #fff\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #dff2f9;\n"
"\n"
"}\n"
"\n"
"#leftMenuContainer{\n"
"	background-color: #4d648d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"	border: none;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"#centerMenuSubContaniner, #centerMenuSubContaniner_2{\n"
"	background-color: #283655;\n"
"	border-top-right-radius: 25px;\n"
"	border-bottom-right-radius: 25px\n"
"}\n"
"\n"
"\n"
"#frame_5 QPushButton{\n"
"	background-color: #4d648d;\n"
"	padding: 7;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#frame_5 QPushButton:hover{\n"
"	background-color: #acacac;\n"
"	bord"
                        "er-radius: 25px\n"
"}\n"
"\n"
"#modStatus {\n"
"	background-color: #4d648d;\n"
"	border-top-left-radius: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"#widget_4 QDoubleSpinBox{\n"
"	border-width: 1px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#widget_11 QDoubleSpinBox{\n"
"	border-width: 1px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#ArchiveBtn {\n"
"	background-color: #4d648d;\n"
"	text-align: center;\n"
"	border-radius: 7px;\n"
"	border-width: 1px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#ArchiveBtn:hover{\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#frame_10, #frame_9, #frame_23, #widget_6, #widget_7, #widget_2, #widget_10 {\n"
"	background-color: #fafade;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"\n"
"#frame_18, #frame_19, #frame_26, #frame_27, #frame_28 {\n"
"	background-color: #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#stackedWidget_22 QPushButton {\n"
"	background-color: #4d648d;\n"
"	borde"
                        "r-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"}\n"
"\n"
"#frame_22 QPushButton:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#frame_24 QPushButton{\n"
"	background-color: #4d648d;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#stackedWidget_15 QPushButton{\n"
"	background-color: #4d648d;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#stackedWidget_15 QPushButton:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#frame_24 QPushButton:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#frame_8 QPushButton{\n"
"	background-color: #8bb6ff;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#frame_8 QPushButton:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#widget {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#widget_4, #widget_11, #widget_13 {\n"
"	color: rgb(255, 255, 255);\n"
""
                        "	background-color: #4d648d;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        reception.setDocumentMode(False)
        self.centralwidget = QWidget(reception)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setMinimumSize(QSize(55, 0))
        self.leftMenuSubContainer.setMaximumSize(QSize(55, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamilies([u"Bahnschrift Light"])
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setFont(font)
        self.menuBtn.setAutoFillBackground(False)
        self.menuBtn.setStyleSheet(u"background-color: #283655;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.HomeBtn = QPushButton(self.frame_2)
        self.HomeBtn.setObjectName(u"HomeBtn")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Light"])
        font1.setPointSize(9)
        self.HomeBtn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeBtn.setIcon(icon1)
        self.HomeBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.HomeBtn)

        self.TranBtn = QPushButton(self.frame_2)
        self.TranBtn.setObjectName(u"TranBtn")
        self.TranBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TranBtn.setIcon(icon2)
        self.TranBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.TranBtn)

        self.RecepBtn = QPushButton(self.frame_2)
        self.RecepBtn.setObjectName(u"RecepBtn")
        self.RecepBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/trending-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RecepBtn.setIcon(icon3)
        self.RecepBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.RecepBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.InfoBtn = QPushButton(self.frame_3)
        self.InfoBtn.setObjectName(u"InfoBtn")
        self.InfoBtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.InfoBtn.setIcon(icon4)
        self.InfoBtn.setIconSize(QSize(40, 40))
        self.InfoBtn.setAutoDefault(False)
        self.InfoBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.InfoBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy1)
        self.centerMenuContainer.setMinimumSize(QSize(9, 0))
        self.verticalLayout_8 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContaniner = QWidget(self.centerMenuContainer)
        self.centerMenuSubContaniner.setObjectName(u"centerMenuSubContaniner")
        self.centerMenuSubContaniner.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuSubContaniner)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, -1, 0, -1)
        self.frame_4 = QFrame(self.centerMenuSubContaniner)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light"])
        font2.setPointSize(11)
        self.label.setFont(font2)
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeMBtn = QPushButton(self.frame_4)
        self.closeMBtn.setObjectName(u"closeMBtn")
        self.closeMBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeMBtn.setIcon(icon5)
        self.closeMBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.closeMBtn)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centerMenuSubContaniner)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift Light"])
        font3.setPointSize(10)
        self.label_9.setFont(font3)
        self.label_9.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_7.addWidget(self.label_9)

        self.textBtn_2 = QPushButton(self.frame_5)
        self.textBtn_2.setObjectName(u"textBtn_2")
        self.textBtn_2.setMinimumSize(QSize(125, 0))
        self.textBtn_2.setMaximumSize(QSize(125, 16777215))
        self.textBtn_2.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/type.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textBtn_2.setIcon(icon6)
        self.textBtn_2.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.textBtn_2)

        self.fileBtn_2 = QPushButton(self.frame_5)
        self.fileBtn_2.setObjectName(u"fileBtn_2")
        self.fileBtn_2.setMinimumSize(QSize(125, 0))
        self.fileBtn_2.setMaximumSize(QSize(125, 16777215))
        self.fileBtn_2.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileBtn_2.setIcon(icon7)
        self.fileBtn_2.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.fileBtn_2)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_8.addWidget(self.centerMenuSubContaniner)

        self.centerMenuSubContaniner_2 = QWidget(self.centerMenuContainer)
        self.centerMenuSubContaniner_2.setObjectName(u"centerMenuSubContaniner_2")
        self.centerMenuSubContaniner_2.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContaniner_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_12 = QFrame(self.centerMenuSubContaniner_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(245, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setLineWidth(1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.closeMBtn_2 = QPushButton(self.frame_12)
        self.closeMBtn_2.setObjectName(u"closeMBtn_2")
        self.closeMBtn_2.setStyleSheet(u"")
        self.closeMBtn_2.setIcon(icon5)
        self.closeMBtn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.closeMBtn_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.centerMenuSubContaniner_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_13)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 20, 0, 15)
        self.textBrowser_7 = QTextBrowser(self.frame_13)
        self.textBrowser_7.setObjectName(u"textBrowser_7")

        self.verticalLayout_24.addWidget(self.textBrowser_7)


        self.verticalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_8.addWidget(self.centerMenuSubContaniner_2)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4 = QHBoxLayout(self.mainBodyContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainBodySubLeftContainer = QFrame(self.mainBodyContainer)
        self.mainBodySubLeftContainer.setObjectName(u"mainBodySubLeftContainer")
        self.mainBodySubLeftContainer.setMaximumSize(QSize(440, 16777215))
        self.mainBodySubLeftContainer.setFrameShape(QFrame.StyledPanel)
        self.mainBodySubLeftContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.mainBodySubLeftContainer)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 9, 0, 0)
        self.frame_10 = QFrame(self.mainBodySubLeftContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(435, 0))
        self.frame_10.setMaximumSize(QSize(435, 16777215))
        self.frame_10.setStyleSheet(u"color: #000000;	\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_14 = QWidget(self.frame_10)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_54 = QVBoxLayout(self.widget_14)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, -1, 0)
        self.label_16 = QLabel(self.widget_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.verticalLayout_54.addWidget(self.label_16)

        self.formatBox = QComboBox(self.widget_14)
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.setObjectName(u"formatBox")
        self.formatBox.setMinimumSize(QSize(410, 0))
        self.formatBox.setMaximumSize(QSize(300, 16777215))
        self.formatBox.setFont(font3)
        self.formatBox.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_54.addWidget(self.formatBox, 0, Qt.AlignLeft)

        self.label_17 = QLabel(self.widget_14)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.verticalLayout_54.addWidget(self.label_17)

        self.codelineBox = QComboBox(self.widget_14)
        self.codelineBox.addItem("")
        self.codelineBox.addItem("")
        self.codelineBox.addItem("")
        self.codelineBox.addItem("")
        self.codelineBox.addItem("")
        self.codelineBox.addItem("")
        self.codelineBox.addItem("")
        self.codelineBox.setObjectName(u"codelineBox")
        self.codelineBox.setMinimumSize(QSize(410, 0))
        self.codelineBox.setMaximumSize(QSize(300, 16777215))
        self.codelineBox.setFont(font3)
        self.codelineBox.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_54.addWidget(self.codelineBox, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift Light"])
        font4.setPointSize(10)
        font4.setUnderline(False)
        self.label_10.setFont(font4)

        self.verticalLayout_54.addWidget(self.label_10)

        self.UmbPreBtn = QRadioButton(self.widget_14)
        self.UmbPreBtn.setObjectName(u"UmbPreBtn")
        self.UmbPreBtn.setFont(font3)
        self.UmbPreBtn.setStyleSheet(u"")

        self.verticalLayout_54.addWidget(self.UmbPreBtn, 0, Qt.AlignLeft)

        self.UmbDisBtn = QRadioButton(self.widget_14)
        self.UmbDisBtn.setObjectName(u"UmbDisBtn")
        self.UmbDisBtn.setFont(font3)
        self.UmbDisBtn.setStyleSheet(u"")

        self.verticalLayout_54.addWidget(self.UmbDisBtn, 0, Qt.AlignLeft)

        self.widget = QWidget(self.widget_14)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 0))
        self.verticalLayout_30 = QVBoxLayout(self.widget)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.stackedWidget_4 = QStackedWidget(self.widget)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_28 = QVBoxLayout(self.page_7)
        self.verticalLayout_28.setSpacing(7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.page_7)
        self.label_8.setObjectName(u"label_8")
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift Light"])
        font5.setPointSize(9)
        font5.setUnderline(False)
        self.label_8.setFont(font5)

        self.verticalLayout_28.addWidget(self.label_8)

        self.simPBitBox = QComboBox(self.page_7)
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.setObjectName(u"simPBitBox")
        self.simPBitBox.setMinimumSize(QSize(410, 0))
        self.simPBitBox.setMaximumSize(QSize(300, 16777215))
        self.simPBitBox.setFont(font3)
        self.simPBitBox.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_28.addWidget(self.simPBitBox)

        self.stackedWidget_4.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_29 = QVBoxLayout(self.page_8)
        self.verticalLayout_29.setSpacing(7)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.page_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.verticalLayout_29.addWidget(self.label_11)

        self.simPBitBox_2 = QComboBox(self.page_8)
        self.simPBitBox_2.addItem("")
        self.simPBitBox_2.addItem("")
        self.simPBitBox_2.addItem("")
        self.simPBitBox_2.setObjectName(u"simPBitBox_2")
        self.simPBitBox_2.setMinimumSize(QSize(410, 0))
        self.simPBitBox_2.setMaximumSize(QSize(300, 16777215))
        self.simPBitBox_2.setFont(font3)
        self.simPBitBox_2.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_29.addWidget(self.simPBitBox_2)

        self.stackedWidget_4.addWidget(self.page_8)

        self.verticalLayout_30.addWidget(self.stackedWidget_4)


        self.verticalLayout_54.addWidget(self.widget, 0, Qt.AlignLeft)


        self.verticalLayout_10.addWidget(self.widget_14, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.widget_6 = QWidget(self.mainBodySubLeftContainer)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(460, 0))
        self.widget_6.setMaximumSize(QSize(16777215, 0))
        self.widget_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.archivePath = QTextBrowser(self.widget_6)
        self.archivePath.setObjectName(u"archivePath")
        self.archivePath.setMinimumSize(QSize(0, 48))
        self.archivePath.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.archivePath)

        self.ArchiveBtn = QPushButton(self.widget_6)
        self.ArchiveBtn.setObjectName(u"ArchiveBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ArchiveBtn.setIcon(icon8)
        self.ArchiveBtn.setIconSize(QSize(30, 30))
        self.ArchiveBtn.setCheckable(True)
        self.ArchiveBtn.setChecked(False)

        self.horizontalLayout_6.addWidget(self.ArchiveBtn, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.widget_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_7 = QWidget(self.mainBodySubLeftContainer)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.widget_7.setMaximumSize(QSize(460, 0))
        self.widget_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 0)
        self.stackedWidget = QStackedWidget(self.widget_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_8 = QHBoxLayout(self.page)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 10)
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_6)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_23.addWidget(self.label_18)

        self.geoBox_1 = QComboBox(self.frame_6)
        self.geoBox_1.addItem("")
        self.geoBox_1.addItem("")
        self.geoBox_1.addItem("")
        self.geoBox_1.addItem("")
        self.geoBox_1.addItem("")
        self.geoBox_1.addItem("")
        self.geoBox_1.setObjectName(u"geoBox_1")
        self.geoBox_1.setFont(font3)
        self.geoBox_1.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_23.addWidget(self.geoBox_1)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_9 = QHBoxLayout(self.page_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 10)
        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_7)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_25.addWidget(self.label_19)

        self.geoBox_2 = QComboBox(self.frame_7)
        self.geoBox_2.addItem("")
        self.geoBox_2.addItem("")
        self.geoBox_2.addItem("")
        self.geoBox_2.addItem("")
        self.geoBox_2.setObjectName(u"geoBox_2")
        self.geoBox_2.setFont(font3)
        self.geoBox_2.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_25.addWidget(self.geoBox_2)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_22 = QVBoxLayout(self.page_5)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 10)
        self.frame_11 = QFrame(self.page_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_11)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_20)

        self.geoBox_3 = QComboBox(self.frame_11)
        self.geoBox_3.addItem("")
        self.geoBox_3.addItem("")
        self.geoBox_3.addItem("")
        self.geoBox_3.addItem("")
        self.geoBox_3.addItem("")
        self.geoBox_3.setObjectName(u"geoBox_3")
        self.geoBox_3.setFont(font3)
        self.geoBox_3.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_26.addWidget(self.geoBox_3)


        self.verticalLayout_22.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_10 = QHBoxLayout(self.page_6)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 10)
        self.frame_14 = QFrame(self.page_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_14)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.verticalLayout_27.addWidget(self.label_21)

        self.geoBox_4 = QComboBox(self.frame_14)
        self.geoBox_4.addItem("")
        self.geoBox_4.addItem("")
        self.geoBox_4.addItem("")
        self.geoBox_4.addItem("")
        self.geoBox_4.addItem("")
        self.geoBox_4.setObjectName(u"geoBox_4")
        self.geoBox_4.setMinimumSize(QSize(410, 0))
        self.geoBox_4.setMaximumSize(QSize(300, 16777215))
        self.geoBox_4.setFont(font3)
        self.geoBox_4.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_27.addWidget(self.geoBox_4)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.page_6)

        self.horizontalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_9.addWidget(self.widget_7)

        self.widget_2 = QWidget(self.mainBodySubLeftContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(460, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 0))
        self.widget_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayout_31 = QVBoxLayout(self.widget_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.stackedWidget_5 = QStackedWidget(self.widget_2)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_35 = QVBoxLayout(self.page_12)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.page_12)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_34 = QVBoxLayout(self.widget_9)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_34.addWidget(self.label_5)

        self.codelineBox_4 = QComboBox(self.widget_9)
        self.codelineBox_4.addItem("")
        self.codelineBox_4.addItem("")
        self.codelineBox_4.addItem("")
        self.codelineBox_4.addItem("")
        self.codelineBox_4.addItem("")
        self.codelineBox_4.addItem("")
        self.codelineBox_4.setObjectName(u"codelineBox_4")
        self.codelineBox_4.setFont(font3)
        self.codelineBox_4.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_34.addWidget(self.codelineBox_4)


        self.verticalLayout_35.addWidget(self.widget_9)

        self.stackedWidget_5.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.verticalLayout_36 = QVBoxLayout(self.page_13)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.page_13)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_33 = QVBoxLayout(self.widget_5)
        self.verticalLayout_33.setSpacing(5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_4)

        self.codelineBox_3 = QComboBox(self.widget_5)
        self.codelineBox_3.addItem("")
        self.codelineBox_3.addItem("")
        self.codelineBox_3.addItem("")
        self.codelineBox_3.addItem("")
        self.codelineBox_3.addItem("")
        self.codelineBox_3.addItem("")
        self.codelineBox_3.setObjectName(u"codelineBox_3")
        self.codelineBox_3.setMinimumSize(QSize(410, 0))
        self.codelineBox_3.setMaximumSize(QSize(300, 16777215))
        self.codelineBox_3.setFont(font3)
        self.codelineBox_3.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_33.addWidget(self.codelineBox_3)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setEnabled(True)
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.widget_8.setMaximumSize(QSize(16777215, 16))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.addBtn = QRadioButton(self.widget_8)
        self.addBtn.setObjectName(u"addBtn")
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift Light"])
        self.addBtn.setFont(font6)

        self.horizontalLayout_12.addWidget(self.addBtn, 0, Qt.AlignHCenter)

        self.noaddBtn = QRadioButton(self.widget_8)
        self.noaddBtn.setObjectName(u"noaddBtn")
        self.noaddBtn.setFont(font6)

        self.horizontalLayout_12.addWidget(self.noaddBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_33.addWidget(self.widget_8)


        self.verticalLayout_36.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.page_13)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 0))
        self.verticalLayout_32 = QVBoxLayout(self.widget_3)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 8, 0, 0)
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout_32.addWidget(self.label_3)

        self.codelineBox_2 = QComboBox(self.widget_3)
        self.codelineBox_2.addItem("")
        self.codelineBox_2.addItem("")
        self.codelineBox_2.addItem("")
        self.codelineBox_2.addItem("")
        self.codelineBox_2.addItem("")
        self.codelineBox_2.addItem("")
        self.codelineBox_2.setObjectName(u"codelineBox_2")
        self.codelineBox_2.setFont(font3)
        self.codelineBox_2.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_32.addWidget(self.codelineBox_2)


        self.verticalLayout_36.addWidget(self.widget_3)

        self.stackedWidget_5.addWidget(self.page_13)

        self.verticalLayout_31.addWidget(self.stackedWidget_5)


        self.verticalLayout_9.addWidget(self.widget_2, 0, Qt.AlignLeft)

        self.frame_17 = QFrame(self.mainBodySubLeftContainer)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 390))
        self.frame_17.setMaximumSize(QSize(16777215, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_17)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_29)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.frame_29)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(435, 0))
        self.widget_13.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.verticalLayout_53 = QVBoxLayout(self.widget_13)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_41 = QLabel(self.widget_13)
        self.label_41.setObjectName(u"label_41")
        font7 = QFont()
        font7.setFamilies([u"Bahnschrift Light"])
        font7.setPointSize(10)
        font7.setUnderline(True)
        self.label_41.setFont(font7)
        self.label_41.setStyleSheet(u"	color: rgb(255, 255, 255);")

        self.verticalLayout_53.addWidget(self.label_41)

        self.fbit = QDoubleSpinBox(self.widget_13)
        self.fbit.setObjectName(u"fbit")
        self.fbit.setFont(font3)
        self.fbit.setDecimals(2)
        self.fbit.setMaximum(1000000000.990000009536743)

        self.verticalLayout_53.addWidget(self.fbit)

        self.label_42 = QLabel(self.widget_13)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font7)
        self.label_42.setStyleSheet(u"	color: rgb(255, 255, 255);")

        self.verticalLayout_53.addWidget(self.label_42)

        self.tbit = QDoubleSpinBox(self.widget_13)
        self.tbit.setObjectName(u"tbit")
        self.tbit.setFont(font3)
        self.tbit.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.tbit.setDecimals(9)
        self.tbit.setMaximum(1000000000.990000009536743)

        self.verticalLayout_53.addWidget(self.tbit)

        self.label_43 = QLabel(self.widget_13)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font7)

        self.verticalLayout_53.addWidget(self.label_43)

        self.fport = QDoubleSpinBox(self.widget_13)
        self.fport.setObjectName(u"fport")
        self.fport.setFont(font4)
        self.fport.setMaximum(6000.000000000000000)

        self.verticalLayout_53.addWidget(self.fport)

        self.label_44 = QLabel(self.widget_13)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font7)

        self.verticalLayout_53.addWidget(self.label_44)

        self.gananRx = QDoubleSpinBox(self.widget_13)
        self.gananRx.setObjectName(u"gananRx")
        self.gananRx.setFont(font4)
        self.gananRx.setMaximum(50.000000000000000)

        self.verticalLayout_53.addWidget(self.gananRx)


        self.verticalLayout_55.addWidget(self.widget_13, 0, Qt.AlignLeft)

        self.frame_8 = QFrame(self.frame_29)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 400))
        self.frame_8.setStyleSheet(u"	color: #000000;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 2, 0, 0)
        self.frame_30 = QFrame(self.frame_8)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_30)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.frame_30)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 0))
        self.widget_11.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_44 = QVBoxLayout(self.widget_11)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.stackedWidget_7 = QStackedWidget(self.widget_11)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.verticalLayout_60 = QVBoxLayout(self.page_26)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.frame_20 = QFrame(self.page_26)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_20)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_52 = QLabel(self.frame_20)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_59.addWidget(self.label_52)


        self.verticalLayout_60.addWidget(self.frame_20)

        self.stackedWidget_7.addWidget(self.page_26)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.verticalLayout_45 = QVBoxLayout(self.page_20)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_28 = QLabel(self.page_20)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.verticalLayout_45.addWidget(self.label_28)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.page_20)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")
        self.doubleSpinBox_12.setFont(font3)
        self.doubleSpinBox_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_45.addWidget(self.doubleSpinBox_12)

        self.label_29 = QLabel(self.page_20)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.verticalLayout_45.addWidget(self.label_29)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.page_20)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")
        self.doubleSpinBox_13.setFont(font3)
        self.doubleSpinBox_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_45.addWidget(self.doubleSpinBox_13)

        self.stackedWidget_7.addWidget(self.page_20)
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.verticalLayout_46 = QVBoxLayout(self.page_21)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_30 = QLabel(self.page_21)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_30)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.page_21)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")
        self.doubleSpinBox_14.setFont(font3)
        self.doubleSpinBox_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_46.addWidget(self.doubleSpinBox_14)

        self.label_31 = QLabel(self.page_21)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_31)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.page_21)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")
        self.doubleSpinBox_15.setFont(font3)
        self.doubleSpinBox_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_46.addWidget(self.doubleSpinBox_15)

        self.stackedWidget_7.addWidget(self.page_21)
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.verticalLayout_47 = QVBoxLayout(self.page_22)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_32 = QLabel(self.page_22)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)

        self.verticalLayout_47.addWidget(self.label_32)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.page_22)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")
        self.doubleSpinBox_16.setFont(font3)
        self.doubleSpinBox_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_47.addWidget(self.doubleSpinBox_16)

        self.label_33 = QLabel(self.page_22)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.verticalLayout_47.addWidget(self.label_33)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.page_22)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")
        self.doubleSpinBox_17.setFont(font3)
        self.doubleSpinBox_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_47.addWidget(self.doubleSpinBox_17)

        self.stackedWidget_7.addWidget(self.page_22)
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.verticalLayout_48 = QVBoxLayout(self.page_23)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_34 = QLabel(self.page_23)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.verticalLayout_48.addWidget(self.label_34)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.page_23)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")
        self.doubleSpinBox_18.setFont(font3)
        self.doubleSpinBox_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_48.addWidget(self.doubleSpinBox_18)

        self.label_35 = QLabel(self.page_23)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)

        self.verticalLayout_48.addWidget(self.label_35)

        self.doubleSpinBox_19 = QDoubleSpinBox(self.page_23)
        self.doubleSpinBox_19.setObjectName(u"doubleSpinBox_19")
        self.doubleSpinBox_19.setFont(font3)
        self.doubleSpinBox_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_48.addWidget(self.doubleSpinBox_19)

        self.stackedWidget_7.addWidget(self.page_23)
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.verticalLayout_49 = QVBoxLayout(self.page_24)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_36 = QLabel(self.page_24)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.verticalLayout_49.addWidget(self.label_36)

        self.doubleSpinBox_20 = QDoubleSpinBox(self.page_24)
        self.doubleSpinBox_20.setObjectName(u"doubleSpinBox_20")
        self.doubleSpinBox_20.setFont(font3)
        self.doubleSpinBox_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_49.addWidget(self.doubleSpinBox_20)

        self.label_37 = QLabel(self.page_24)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.verticalLayout_49.addWidget(self.label_37)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.page_24)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")
        self.doubleSpinBox_21.setFont(font3)
        self.doubleSpinBox_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_49.addWidget(self.doubleSpinBox_21)

        self.label_38 = QLabel(self.page_24)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.verticalLayout_49.addWidget(self.label_38)

        self.doubleSpinBox_22 = QDoubleSpinBox(self.page_24)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")
        self.doubleSpinBox_22.setFont(font3)
        self.doubleSpinBox_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_49.addWidget(self.doubleSpinBox_22)

        self.stackedWidget_7.addWidget(self.page_24)

        self.verticalLayout_44.addWidget(self.stackedWidget_7, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_56.addWidget(self.widget_11, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_4 = QWidget(self.frame_30)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_37 = QVBoxLayout(self.widget_4)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.stackedWidget_6 = QStackedWidget(self.widget_4)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.verticalLayout_50 = QVBoxLayout(self.page_25)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_16 = QFrame(self.page_25)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_16)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_39 = QLabel(self.frame_16)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_51.addWidget(self.label_39)


        self.verticalLayout_50.addWidget(self.frame_16)

        self.stackedWidget_6.addWidget(self.page_25)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.verticalLayout_39 = QVBoxLayout(self.page_15)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_12 = QLabel(self.page_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.verticalLayout_39.addWidget(self.label_12)

        self.doubleSpinBox = QDoubleSpinBox(self.page_15)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setFont(font3)
        self.doubleSpinBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_39.addWidget(self.doubleSpinBox)

        self.label_6 = QLabel(self.page_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_39.addWidget(self.label_6)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.page_15)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setFont(font3)
        self.doubleSpinBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_39.addWidget(self.doubleSpinBox_2)

        self.stackedWidget_6.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_40 = QVBoxLayout(self.page_16)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_13 = QLabel(self.page_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.verticalLayout_40.addWidget(self.label_13)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.page_16)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setFont(font3)
        self.doubleSpinBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_40.addWidget(self.doubleSpinBox_4)

        self.label_14 = QLabel(self.page_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.verticalLayout_40.addWidget(self.label_14)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.page_16)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setFont(font3)
        self.doubleSpinBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_40.addWidget(self.doubleSpinBox_3)

        self.stackedWidget_6.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.verticalLayout_41 = QVBoxLayout(self.page_17)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_15 = QLabel(self.page_17)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.verticalLayout_41.addWidget(self.label_15)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.page_17)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setFont(font3)
        self.doubleSpinBox_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_41.addWidget(self.doubleSpinBox_6)

        self.label_22 = QLabel(self.page_17)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.verticalLayout_41.addWidget(self.label_22)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.page_17)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setFont(font3)
        self.doubleSpinBox_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_41.addWidget(self.doubleSpinBox_5)

        self.stackedWidget_6.addWidget(self.page_17)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.verticalLayout_42 = QVBoxLayout(self.page_19)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_23 = QLabel(self.page_19)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.verticalLayout_42.addWidget(self.label_23)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.page_19)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setFont(font3)
        self.doubleSpinBox_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_42.addWidget(self.doubleSpinBox_8)

        self.label_24 = QLabel(self.page_19)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.verticalLayout_42.addWidget(self.label_24)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.page_19)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setFont(font3)
        self.doubleSpinBox_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_42.addWidget(self.doubleSpinBox_7)

        self.stackedWidget_6.addWidget(self.page_19)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        font8 = QFont()
        font8.setPointSize(10)
        self.page_18.setFont(font8)
        self.verticalLayout_43 = QVBoxLayout(self.page_18)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_25 = QLabel(self.page_18)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.verticalLayout_43.addWidget(self.label_25)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.page_18)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setFont(font3)
        self.doubleSpinBox_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.doubleSpinBox_10)

        self.label_27 = QLabel(self.page_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.verticalLayout_43.addWidget(self.label_27)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.page_18)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setFont(font3)
        self.doubleSpinBox_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.doubleSpinBox_11)

        self.label_26 = QLabel(self.page_18)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.verticalLayout_43.addWidget(self.label_26)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.page_18)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setFont(font3)
        self.doubleSpinBox_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.doubleSpinBox_9)

        self.stackedWidget_6.addWidget(self.page_18)

        self.verticalLayout_37.addWidget(self.stackedWidget_6, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_56.addWidget(self.widget_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_14.addWidget(self.frame_30, 0, Qt.AlignLeft)

        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 0, 0, 0)
        self.recepBtn = QPushButton(self.frame_15)
        self.recepBtn.setObjectName(u"recepBtn")
        self.recepBtn.setMinimumSize(QSize(0, 0))
        self.recepBtn.setFont(font1)
        self.recepBtn.setStyleSheet(u"#recepBtn {\n"
"	background-color: rgb(238, 146, 143);\n"
"}\n"
"\n"
"#recepBtn:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.recepBtn, 0, Qt.AlignHCenter)

        self.stoprecBtn = QPushButton(self.frame_15)
        self.stoprecBtn.setObjectName(u"stoprecBtn")
        self.stoprecBtn.setMinimumSize(QSize(0, 0))
        self.stoprecBtn.setFont(font1)
        self.stoprecBtn.setStyleSheet(u"#stoprecBtn {\n"
"	background-color: rgb(238, 146, 143);\n"
"}\n"
"\n"
"#stoprecBtn:hover {\n"
"	background-color: #acacac;\n"
"}")

        self.verticalLayout_11.addWidget(self.stoprecBtn)

        self.recSBtn = QPushButton(self.frame_15)
        self.recSBtn.setObjectName(u"recSBtn")
        self.recSBtn.setMinimumSize(QSize(0, 0))
        self.recSBtn.setMaximumSize(QSize(16777215, 16777215))
        self.recSBtn.setFont(font1)
        self.recSBtn.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.recSBtn)


        self.horizontalLayout_14.addWidget(self.frame_15, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_55.addWidget(self.frame_8)


        self.horizontalLayout_16.addWidget(self.frame_29, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_17, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.mainBodySubLeftContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.mainBodySubRightContainer = QFrame(self.mainBodyContainer)
        self.mainBodySubRightContainer.setObjectName(u"mainBodySubRightContainer")
        self.mainBodySubRightContainer.setMinimumSize(QSize(0, 0))
        self.mainBodySubRightContainer.setFrameShape(QFrame.StyledPanel)
        self.mainBodySubRightContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.mainBodySubRightContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, -1, -1, -1)
        self.frame_9 = QFrame(self.mainBodySubRightContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 450))
        self.frame_9.setStyleSheet(u"	color: #000000;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stackedWidget_15 = QStackedWidget(self.frame_9)
        self.stackedWidget_15.setObjectName(u"stackedWidget_15")
        self.stackedWidget_15.setStyleSheet(u"")
        self.page_29 = QWidget()
        self.page_29.setObjectName(u"page_29")
        self.page_29.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_18 = QHBoxLayout(self.page_29)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.graph_recep = QPushButton(self.page_29)
        self.graph_recep.setObjectName(u"graph_recep")
        self.graph_recep.setFont(font3)
        self.graph_recep.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_18.addWidget(self.graph_recep)

        self.info_text_recep = QTextBrowser(self.page_29)
        self.info_text_recep.setObjectName(u"info_text_recep")
        self.info_text_recep.setMinimumSize(QSize(0, 0))
        self.info_text_recep.setMaximumSize(QSize(16777215, 24))
        self.info_text_recep.setFont(font)

        self.horizontalLayout_18.addWidget(self.info_text_recep)

        self.stackedWidget_15.addWidget(self.page_29)
        self.page_30 = QWidget()
        self.page_30.setObjectName(u"page_30")
        self.horizontalLayout_19 = QHBoxLayout(self.page_30)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.graph_recep_2 = QPushButton(self.page_30)
        self.graph_recep_2.setObjectName(u"graph_recep_2")
        self.graph_recep_2.setFont(font3)
        self.graph_recep_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_19.addWidget(self.graph_recep_2)

        self.info_text_recep_2 = QTextBrowser(self.page_30)
        self.info_text_recep_2.setObjectName(u"info_text_recep_2")
        self.info_text_recep_2.setMinimumSize(QSize(0, 0))
        self.info_text_recep_2.setMaximumSize(QSize(16777215, 24))
        self.info_text_recep_2.setFont(font)

        self.horizontalLayout_19.addWidget(self.info_text_recep_2)

        self.stackedWidget_15.addWidget(self.page_30)
        self.page_31 = QWidget()
        self.page_31.setObjectName(u"page_31")
        self.horizontalLayout_23 = QHBoxLayout(self.page_31)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.graph_recep_1 = QPushButton(self.page_31)
        self.graph_recep_1.setObjectName(u"graph_recep_1")
        self.graph_recep_1.setFont(font3)
        self.graph_recep_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_23.addWidget(self.graph_recep_1)

        self.info_text_recep_1 = QTextBrowser(self.page_31)
        self.info_text_recep_1.setObjectName(u"info_text_recep_1")
        self.info_text_recep_1.setMinimumSize(QSize(0, 0))
        self.info_text_recep_1.setMaximumSize(QSize(16777215, 24))
        self.info_text_recep_1.setFont(font)

        self.horizontalLayout_23.addWidget(self.info_text_recep_1)

        self.stackedWidget_15.addWidget(self.page_31)
        self.page_35 = QWidget()
        self.page_35.setObjectName(u"page_35")
        self.horizontalLayout_27 = QHBoxLayout(self.page_35)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.graph_recep_0 = QPushButton(self.page_35)
        self.graph_recep_0.setObjectName(u"graph_recep_0")
        self.graph_recep_0.setFont(font3)
        self.graph_recep_0.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_27.addWidget(self.graph_recep_0)

        self.info_text_recep_0 = QTextBrowser(self.page_35)
        self.info_text_recep_0.setObjectName(u"info_text_recep_0")
        self.info_text_recep_0.setMinimumSize(QSize(0, 0))
        self.info_text_recep_0.setMaximumSize(QSize(16777215, 24))
        self.info_text_recep_0.setFont(font)

        self.horizontalLayout_27.addWidget(self.info_text_recep_0)

        self.stackedWidget_15.addWidget(self.page_35)
        self.page_36 = QWidget()
        self.page_36.setObjectName(u"page_36")
        self.horizontalLayout_28 = QHBoxLayout(self.page_36)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.info_text_recep_final = QTextBrowser(self.page_36)
        self.info_text_recep_final.setObjectName(u"info_text_recep_final")
        self.info_text_recep_final.setMinimumSize(QSize(0, 0))
        self.info_text_recep_final.setMaximumSize(QSize(16777215, 24))
        self.info_text_recep_final.setFont(font)

        self.horizontalLayout_28.addWidget(self.info_text_recep_final)

        self.stackedWidget_15.addWidget(self.page_36)
        self.page_39 = QWidget()
        self.page_39.setObjectName(u"page_39")
        self.horizontalLayout_30 = QHBoxLayout(self.page_39)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.info_text_recep_inicio = QTextBrowser(self.page_39)
        self.info_text_recep_inicio.setObjectName(u"info_text_recep_inicio")
        self.info_text_recep_inicio.setMinimumSize(QSize(0, 0))
        self.info_text_recep_inicio.setMaximumSize(QSize(16777215, 24))
        self.info_text_recep_inicio.setFont(font)

        self.horizontalLayout_30.addWidget(self.info_text_recep_inicio)

        self.stackedWidget_15.addWidget(self.page_39)

        self.verticalLayout_12.addWidget(self.stackedWidget_15, 0, Qt.AlignTop)

        self.frame_21 = QFrame(self.frame_9)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 200))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_22 = QStackedWidget(self.frame_21)
        self.stackedWidget_22.setObjectName(u"stackedWidget_22")
        self.stackedWidget_22.setStyleSheet(u"")
        self.stackedWidget_22.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_22.setFrameShadow(QFrame.Raised)
        self.page_27 = QWidget()
        self.page_27.setObjectName(u"page_27")
        self.horizontalLayout_17 = QHBoxLayout(self.page_27)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, -1, 0)
        self.text_recep = QTextBrowser(self.page_27)
        self.text_recep.setObjectName(u"text_recep")
        self.text_recep.setMinimumSize(QSize(0, 0))
        self.text_recep.setMaximumSize(QSize(16777215, 30))
        self.text_recep.setFont(font)

        self.horizontalLayout_17.addWidget(self.text_recep, 0, Qt.AlignTop)

        self.stackedWidget_22.addWidget(self.page_27)
        self.page_28 = QWidget()
        self.page_28.setObjectName(u"page_28")
        self.horizontalLayout_15 = QHBoxLayout(self.page_28)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mesRecBtn = QPushButton(self.page_28)
        self.mesRecBtn.setObjectName(u"mesRecBtn")
        self.mesRecBtn.setFont(font3)
        self.mesRecBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_15.addWidget(self.mesRecBtn)

        self.recBBBTN = QPushButton(self.page_28)
        self.recBBBTN.setObjectName(u"recBBBTN")
        self.recBBBTN.setFont(font3)
        self.recBBBTN.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_15.addWidget(self.recBBBTN)

        self.stackedWidget_22.addWidget(self.page_28)

        self.verticalLayout_13.addWidget(self.stackedWidget_22, 0, Qt.AlignTop)

        self.stackedWidget_2 = QStackedWidget(self.frame_21)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 200))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMinimumSize(QSize(0, 230))
        self.page_4.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.page_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_19 = QFrame(self.page_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 210))
        self.frame_19.setMaximumSize(QSize(16777215, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.recBBlayout = QVBoxLayout()
        self.recBBlayout.setSpacing(7)
        self.recBBlayout.setObjectName(u"recBBlayout")

        self.horizontalLayout_21.addLayout(self.recBBlayout)


        self.verticalLayout_15.addWidget(self.frame_19)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(0, 230))
        self.page_3.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.page_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_18 = QFrame(self.page_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 210))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_18)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_40 = QLabel(self.frame_18)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)

        self.verticalLayout_52.addWidget(self.label_40)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.stackedWidget_2.addWidget(self.page_3)

        self.verticalLayout_13.addWidget(self.stackedWidget_2)


        self.verticalLayout_12.addWidget(self.frame_21)


        self.verticalLayout_16.addWidget(self.frame_9)

        self.frame_23 = QFrame(self.mainBodySubRightContainer)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_23)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_24)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 10, 0, 0)
        self.stackedWidget_25 = QStackedWidget(self.frame_24)
        self.stackedWidget_25.setObjectName(u"stackedWidget_25")
        self.stackedWidget_25.setStyleSheet(u"")
        self.stackedWidget_25.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_25.setFrameShadow(QFrame.Raised)
        self.page_37 = QWidget()
        self.page_37.setObjectName(u"page_37")
        self.horizontalLayout_13 = QHBoxLayout(self.page_37)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.dataBtn = QPushButton(self.page_37)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setFont(font3)
        self.dataBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_13.addWidget(self.dataBtn)

        self.SRBtn = QPushButton(self.page_37)
        self.SRBtn.setObjectName(u"SRBtn")
        self.SRBtn.setFont(font3)
        self.SRBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_13.addWidget(self.SRBtn)

        self.DEPBtn = QPushButton(self.page_37)
        self.DEPBtn.setObjectName(u"DEPBtn")
        self.DEPBtn.setFont(font3)
        self.DEPBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_13.addWidget(self.DEPBtn)

        self.ConstBtn = QPushButton(self.page_37)
        self.ConstBtn.setObjectName(u"ConstBtn")
        self.ConstBtn.setFont(font3)
        self.ConstBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_13.addWidget(self.ConstBtn)

        self.stackedWidget_25.addWidget(self.page_37)
        self.page_38 = QWidget()
        self.page_38.setObjectName(u"page_38")
        self.horizontalLayout_29 = QHBoxLayout(self.page_38)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.SRBtn_2 = QPushButton(self.page_38)
        self.SRBtn_2.setObjectName(u"SRBtn_2")
        self.SRBtn_2.setFont(font3)
        self.SRBtn_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_29.addWidget(self.SRBtn_2)

        self.DEPBtn_2 = QPushButton(self.page_38)
        self.DEPBtn_2.setObjectName(u"DEPBtn_2")
        self.DEPBtn_2.setFont(font3)
        self.DEPBtn_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_29.addWidget(self.DEPBtn_2)

        self.ConstBtn_2 = QPushButton(self.page_38)
        self.ConstBtn_2.setObjectName(u"ConstBtn_2")
        self.ConstBtn_2.setFont(font3)
        self.ConstBtn_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_29.addWidget(self.ConstBtn_2)

        self.stackedWidget_25.addWidget(self.page_38)

        self.verticalLayout_17.addWidget(self.stackedWidget_25, 0, Qt.AlignTop)

        self.stackedWidget_3 = QStackedWidget(self.frame_24)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 250))
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setMinimumSize(QSize(0, 250))
        self.page_10.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.page_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_27 = QFrame(self.page_10)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 230))
        self.frame_27.setMaximumSize(QSize(16777215, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.SRlayout = QVBoxLayout()
        self.SRlayout.setSpacing(7)
        self.SRlayout.setObjectName(u"SRlayout")

        self.horizontalLayout_25.addLayout(self.SRlayout)


        self.verticalLayout_19.addWidget(self.frame_27)

        self.stackedWidget_3.addWidget(self.page_10)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setMinimumSize(QSize(0, 250))
        self.page_9.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_18 = QVBoxLayout(self.page_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_26 = QFrame(self.page_9)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 230))
        self.frame_26.setMaximumSize(QSize(16777215, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.Constlayout = QVBoxLayout()
        self.Constlayout.setSpacing(7)
        self.Constlayout.setObjectName(u"Constlayout")

        self.horizontalLayout_24.addLayout(self.Constlayout)


        self.verticalLayout_18.addWidget(self.frame_26)

        self.stackedWidget_3.addWidget(self.page_9)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_21 = QVBoxLayout(self.page_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_28 = QFrame(self.page_11)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.DEPlayout = QVBoxLayout()
        self.DEPlayout.setSpacing(7)
        self.DEPlayout.setObjectName(u"DEPlayout")

        self.horizontalLayout_26.addLayout(self.DEPlayout)


        self.verticalLayout_21.addWidget(self.frame_28)

        self.stackedWidget_3.addWidget(self.page_11)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.verticalLayout_38 = QVBoxLayout(self.page_14)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.widget_10 = QWidget(self.page_14)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.finalInfo_2 = QTextBrowser(self.widget_10)
        self.finalInfo_2.setObjectName(u"finalInfo_2")
        self.finalInfo_2.setFont(font3)

        self.horizontalLayout_11.addWidget(self.finalInfo_2)


        self.verticalLayout_38.addWidget(self.widget_10)

        self.stackedWidget_3.addWidget(self.page_14)

        self.verticalLayout_17.addWidget(self.stackedWidget_3)


        self.verticalLayout_20.addWidget(self.frame_24)


        self.verticalLayout_16.addWidget(self.frame_23)

        self.verticalLayout_16.setStretch(1, 5)

        self.horizontalLayout_4.addWidget(self.mainBodySubRightContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        reception.setCentralWidget(self.centralwidget)

        self.retranslateUi(reception)

        self.menuBtn.setDefault(False)
        self.TranBtn.setDefault(False)
        self.RecepBtn.setDefault(False)
        self.InfoBtn.setDefault(False)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_7.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedWidget_15.setCurrentIndex(4)
        self.stackedWidget_22.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_25.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(reception)
    # setupUi

    def retranslateUi(self, reception):
        reception.setWindowTitle(QCoreApplication.translate("reception", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("reception", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
        self.HomeBtn.setText(QCoreApplication.translate("reception", u"Pantalla de Inicio", None))
#if QT_CONFIG(tooltip)
        self.TranBtn.setToolTip(QCoreApplication.translate("reception", u"Trabaja como nodo transmisor", None))
#endif // QT_CONFIG(tooltip)
        self.TranBtn.setText(QCoreApplication.translate("reception", u"Transmisi\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.RecepBtn.setToolTip(QCoreApplication.translate("reception", u"Trabajar como nodo receptor", None))
#endif // QT_CONFIG(tooltip)
        self.RecepBtn.setText(QCoreApplication.translate("reception", u"Recepci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.InfoBtn.setToolTip(QCoreApplication.translate("reception", u"M\u00e1s informaci\u00f3n sobre la Herramienta", None))
#endif // QT_CONFIG(tooltip)
        self.InfoBtn.setText(QCoreApplication.translate("reception", u"Informaci\u00f3n", None))
#if QT_CONFIG(shortcut)
        self.InfoBtn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("reception", u"Digital Comunications Toolkit", None))
        self.closeMBtn.setText("")
        self.label_9.setText(QCoreApplication.translate("reception", u"Seleccione el tipo de mensaje", None))
        self.textBtn_2.setText(QCoreApplication.translate("reception", u"Texto", None))
        self.fileBtn_2.setText(QCoreApplication.translate("reception", u"Archivo", None))
        self.label_2.setText(QCoreApplication.translate("reception", u"Digital Comunications Toolkit", None))
        self.closeMBtn_2.setText("")
        self.textBrowser_7.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; text-decoration: underline; color:#ffffff;\">Nombre</span><span style=\" font-family:'Bahnschrift Light'; color:#ffffff;\">: Digital Communications Toolkit</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "Bahnschrift Light'; text-decoration: underline; color:#ffffff;\">Versi\u00f3n</span><span style=\" font-family:'Bahnschrift Light'; color:#ffffff;\">: 1.0 2023</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; text-decoration: underline; color:#ffffff;\">Creado por</span><span style=\" font-family:'Bahnschrift Light'; color:#ffffff;\">: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; color:#ffffff;\">Luis G. Mu\u00f1oz L. y Jes\u00fas A. Del Mar R.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Bahnschrift Light'; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; font-style:italic; color:#ffffff;\">Ingenier\u00eda en Telecomunicaciones</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; font-style:italic; color:#ffffff;\">Universidad Cat\u00f3lica Andr\u00e9s Bello</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("reception", u"Escoja el formato del mensaje a recibir:", None))
        self.formatBox.setItemText(0, "")
        self.formatBox.setItemText(1, QCoreApplication.translate("reception", u"Texto (variable tipo String)", None))
        self.formatBox.setItemText(2, QCoreApplication.translate("reception", u"Imagen (*.jpg)", None))
        self.formatBox.setItemText(3, QCoreApplication.translate("reception", u"Imagen (*.png)", None))
        self.formatBox.setItemText(4, QCoreApplication.translate("reception", u"Audio (*.mp3)", None))
        self.formatBox.setItemText(5, QCoreApplication.translate("reception", u"Video (*.mp4)", None))
        self.formatBox.setItemText(6, QCoreApplication.translate("reception", u"Documento Word (*.docx)", None))
        self.formatBox.setItemText(7, QCoreApplication.translate("reception", u"Documento PDF (*.pdf)", None))
        self.formatBox.setItemText(8, QCoreApplication.translate("reception", u"Archivo Excel (*.xlsx)", None))
        self.formatBox.setItemText(9, QCoreApplication.translate("reception", u"Diapositivas PP (*.pptx)", None))
        self.formatBox.setItemText(10, "")

        self.label_17.setText(QCoreApplication.translate("reception", u"Escoja el tipo de c\u00f3digo de l\u00ednea (Solo referencial):", None))
        self.codelineBox.setItemText(0, "")
        self.codelineBox.setItemText(1, QCoreApplication.translate("reception", u"NRZu (Non Return to Zero Unipolar)", None))
        self.codelineBox.setItemText(2, QCoreApplication.translate("reception", u"NRZp (Non Return to Zero Polar)", None))
        self.codelineBox.setItemText(3, QCoreApplication.translate("reception", u"RZu (Return to Zero Unipolar)", None))
        self.codelineBox.setItemText(4, QCoreApplication.translate("reception", u"RZp (Return to Zero Polar)", None))
        self.codelineBox.setItemText(5, QCoreApplication.translate("reception", u"AMI (Alternate Mark Inversion)", None))
        self.codelineBox.setItemText(6, QCoreApplication.translate("reception", u"Manchester", None))

        self.label_10.setText(QCoreApplication.translate("reception", u"Para la deteci\u00f3n de los simbolos, \u00bfComo prefiere definir los umbrales?", None))
        self.UmbPreBtn.setText(QCoreApplication.translate("reception", u"Umbrales previamente definidos", None))
        self.UmbDisBtn.setText(QCoreApplication.translate("reception", u"Dise\u00f1ar los umbrales ", None))
        self.label_8.setText(QCoreApplication.translate("reception", u"Escoja la cantidad de simbolos por bit de la se\u00f1al transmitida:", None))
        self.simPBitBox.setItemText(0, "")
        self.simPBitBox.setItemText(1, QCoreApplication.translate("reception", u"2 simbolos por bit", None))
        self.simPBitBox.setItemText(2, QCoreApplication.translate("reception", u"4 simbolos por bit", None))
        self.simPBitBox.setItemText(3, QCoreApplication.translate("reception", u"8 simbolos por bit", None))
        self.simPBitBox.setItemText(4, QCoreApplication.translate("reception", u"16 simbolos por bit", None))

        self.label_11.setText(QCoreApplication.translate("reception", u"Escoja la cantidad de simbolos por bit de la se\u00f1al transmitida:", None))
        self.simPBitBox_2.setItemText(0, "")
        self.simPBitBox_2.setItemText(1, QCoreApplication.translate("reception", u"2 simbolos por bit", None))
        self.simPBitBox_2.setItemText(2, QCoreApplication.translate("reception", u"4 simbolos por bit", None))

        self.label_7.setText(QCoreApplication.translate("reception", u"Escoja la ubicaci\u00f3n en donde guardar el archivo:", None))
        self.archivePath.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.ArchiveBtn.setText("")
        self.label_18.setText(QCoreApplication.translate("reception", u"Defina la geometr\u00eda del umbral:", None))
        self.geoBox_1.setItemText(0, "")
        self.geoBox_1.setItemText(1, QCoreApplication.translate("reception", u"Recta Inclinada (pendiente positiva)", None))
        self.geoBox_1.setItemText(2, QCoreApplication.translate("reception", u"Recta paralela al eje X", None))
        self.geoBox_1.setItemText(3, QCoreApplication.translate("reception", u"Recta paralela al eje Y", None))
        self.geoBox_1.setItemText(4, QCoreApplication.translate("reception", u"Recta en el eje Y = 1.5", None))
        self.geoBox_1.setItemText(5, QCoreApplication.translate("reception", u"Recta en el eje Y = 0.5", None))

        self.label_19.setText(QCoreApplication.translate("reception", u"Defina la geometr\u00eda del umbral:", None))
        self.geoBox_2.setItemText(0, "")
        self.geoBox_2.setItemText(1, QCoreApplication.translate("reception", u"2 Rectas Diagonales ", None))
        self.geoBox_2.setItemText(2, QCoreApplication.translate("reception", u"2 Rectas paralelas a los ejes", None))
        self.geoBox_2.setItemText(3, QCoreApplication.translate("reception", u"3 Rectas verticales", None))

        self.label_20.setText(QCoreApplication.translate("reception", u"Defina la geometr\u00eda del umbral:", None))
        self.geoBox_3.setItemText(0, "")
        self.geoBox_3.setItemText(1, QCoreApplication.translate("reception", u"2 Rectas en los ejes y Un Circulo", None))
        self.geoBox_3.setItemText(2, QCoreApplication.translate("reception", u"4 Rectas Diagonales", None))
        self.geoBox_3.setItemText(3, QCoreApplication.translate("reception", u"4 Rectas: 3 verticales y 1 horizontal", None))
        self.geoBox_3.setItemText(4, QCoreApplication.translate("reception", u"6 Rectas Verticales", None))

        self.label_21.setText(QCoreApplication.translate("reception", u"Defina la geometr\u00eda del umbral:", None))
        self.geoBox_4.setItemText(0, "")
        self.geoBox_4.setItemText(1, QCoreApplication.translate("reception", u"8 Rectas Diagonales", None))
        self.geoBox_4.setItemText(2, QCoreApplication.translate("reception", u"4 Rectas Diagonales y Un Circulo (Radio = 2.5)", None))
        self.geoBox_4.setItemText(3, QCoreApplication.translate("reception", u"4 Rectas Diagonales y Un Circulos (Radio = 1.5)", None))
        self.geoBox_4.setItemText(4, QCoreApplication.translate("reception", u"6 Rectas: 3 Horizontales y 3 Verticales", None))

        self.label_5.setText(QCoreApplication.translate("reception", u"Umbral 1: Escoja la geometr\u00eda del umbral que desea agregar:", None))
        self.codelineBox_4.setItemText(0, "")
        self.codelineBox_4.setItemText(1, QCoreApplication.translate("reception", u"L\u00ednea Vertical (x = a) ", None))
        self.codelineBox_4.setItemText(2, QCoreApplication.translate("reception", u"L\u00ednea Vertical (x = -a) ", None))
        self.codelineBox_4.setItemText(3, QCoreApplication.translate("reception", u"L\u00ednea Horizontal (y = b)", None))
        self.codelineBox_4.setItemText(4, QCoreApplication.translate("reception", u"L\u00ednea Horizontal (y = -b)", None))
        self.codelineBox_4.setItemText(5, QCoreApplication.translate("reception", u"L\u00ednea Inclinada ", None))

        self.label_4.setText(QCoreApplication.translate("reception", u"Umbral 1: Escoja la geometr\u00eda del umbral que desea agregar:", None))
        self.codelineBox_3.setItemText(0, "")
        self.codelineBox_3.setItemText(1, QCoreApplication.translate("reception", u"L\u00ednea Vertical (x = a)", None))
        self.codelineBox_3.setItemText(2, QCoreApplication.translate("reception", u"L\u00ednea Vertical (x = -a)", None))
        self.codelineBox_3.setItemText(3, QCoreApplication.translate("reception", u"L\u00ednea Horizontal (y = b)", None))
        self.codelineBox_3.setItemText(4, QCoreApplication.translate("reception", u"L\u00ednea Horizontal (y = -b)", None))
        self.codelineBox_3.setItemText(5, QCoreApplication.translate("reception", u"L\u00ednea Inclinada ", None))

        self.addBtn.setText(QCoreApplication.translate("reception", u"Agregar otro Umbral", None))
        self.noaddBtn.setText(QCoreApplication.translate("reception", u"No Agregar otro Umbral", None))
        self.label_3.setText(QCoreApplication.translate("reception", u"Umbral 2: Escoja la geometr\u00eda del umbral que desea agregar:", None))
        self.codelineBox_2.setItemText(0, "")
        self.codelineBox_2.setItemText(1, QCoreApplication.translate("reception", u"L\u00ednea Vertical (x = a)", None))
        self.codelineBox_2.setItemText(2, QCoreApplication.translate("reception", u"L\u00ednea Vertical (x = -a)", None))
        self.codelineBox_2.setItemText(3, QCoreApplication.translate("reception", u"L\u00ednea Horizontal (y = b)", None))
        self.codelineBox_2.setItemText(4, QCoreApplication.translate("reception", u"L\u00ednea Horizontal (y = -b)", None))
        self.codelineBox_2.setItemText(5, QCoreApplication.translate("reception", u"L\u00ednea Inclinada ", None))

        self.label_41.setText(QCoreApplication.translate("reception", u"Defina fsim (frecuencia de simbolo) - En base al tiempo de simbolo", None))
        self.label_42.setText(QCoreApplication.translate("reception", u"Defina tsim (tiempo de simbolo) -  En base a la frecuencia de simbolo", None))
        self.label_43.setText(QCoreApplication.translate("reception", u"Defina la frecuencia de Portadora (MHz - Max: 6000)", None))
        self.label_44.setText(QCoreApplication.translate("reception", u"Defina la ganancia de recepci\u00f3n (dB - Max: 50)", None))
        self.label_52.setText("")
        self.label_28.setText(QCoreApplication.translate("reception", u"Para x = a, defina el valor de a", None))
        self.label_29.setText(QCoreApplication.translate("reception", u"Defina el valor del offset", None))
        self.label_30.setText(QCoreApplication.translate("reception", u"Para x = -a, defina el valor de a", None))
        self.label_31.setText(QCoreApplication.translate("reception", u"Definal el valor del offset", None))
        self.label_32.setText(QCoreApplication.translate("reception", u"Para y = b, defina el valor de b", None))
        self.label_33.setText(QCoreApplication.translate("reception", u"Definal el valor del offset", None))
        self.label_34.setText(QCoreApplication.translate("reception", u"Para y = -b, defina el valor de b", None))
        self.label_35.setText(QCoreApplication.translate("reception", u"Definal el valor del offset", None))
        self.label_36.setText(QCoreApplication.translate("reception", u"Defina el \u00e1ngulo de Inclinaci\u00f3n", None))
        self.label_37.setText(QCoreApplication.translate("reception", u"Definal el valor del offset para el eje x", None))
        self.label_38.setText(QCoreApplication.translate("reception", u"Definal el valor del offset para el eje y", None))
        self.label_39.setText("")
        self.label_12.setText(QCoreApplication.translate("reception", u"Para x = a, defina el valor de a", None))
        self.label_6.setText(QCoreApplication.translate("reception", u"Defina el valor del offset", None))
        self.label_13.setText(QCoreApplication.translate("reception", u"Para x = -a, defina el valor de a", None))
        self.label_14.setText(QCoreApplication.translate("reception", u"Definal el valor del offset", None))
        self.label_15.setText(QCoreApplication.translate("reception", u"Para y = b, defina el valor de b", None))
        self.label_22.setText(QCoreApplication.translate("reception", u"Definal el valor del offset", None))
        self.label_23.setText(QCoreApplication.translate("reception", u"Para y = -b, defina el valor de b", None))
        self.label_24.setText(QCoreApplication.translate("reception", u"Definal el valor del offset", None))
        self.label_25.setText(QCoreApplication.translate("reception", u"Defina el \u00e1ngulo de Inclinaci\u00f3n", None))
        self.label_27.setText(QCoreApplication.translate("reception", u"Definal el valor del offset para el eje x", None))
        self.label_26.setText(QCoreApplication.translate("reception", u"Definal el valor del offset para el eje y", None))
        self.recepBtn.setText(QCoreApplication.translate("reception", u"Habilitar estado de Recepci\u00f3n", None))
        self.stoprecBtn.setText(QCoreApplication.translate("reception", u"Detener estado de Recepci\u00f3n", None))
        self.recSBtn.setText(QCoreApplication.translate("reception", u"Visualizar Mensaje Recibido\n"
"(Solo si es texto o Imagen)", None))
        self.graph_recep.setText(QCoreApplication.translate("reception", u"Filtrar la Se\u00f1al y Graficar", None))
        self.info_text_recep.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Actualmente est\u00e1 graficado la se\u00f1al tal y como la recibe el m\u00f3dulo ADALM - PLUTO</span></p></body></html>", None))
        self.graph_recep_2.setText(QCoreApplication.translate("reception", u"Corregir la Frecuencia y/o Fase y Graficar", None))
        self.info_text_recep_2.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Actualmente est\u00e1 graficada la se\u00f1al despu\u00e9s de haber sido filtrada</span></p></body></html>", None))
        self.graph_recep_1.setText(QCoreApplication.translate("reception", u"Sincronizar en tiempo la Se\u00f1al y Graficar", None))
        self.info_text_recep_1.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Actualmente est\u00e1 graficado la se\u00f1al despu\u00e9s de haber sido corregida su frecuencia y/o fase</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.graph_recep_0.setText(QCoreApplication.translate("reception", u"Realizar Correci\u00f3n de Errores y Graficar ", None))
        self.info_text_recep_0.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Actualmente est\u00e1 graficado la se\u00f1al despu\u00e9s de haber sido sincronizada en tiempo, frecuencia y/o fase</span></p></body></html>", None))
        self.info_text_recep_final.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Actualmente est\u00e1 graficado la se\u00f1al despu\u00e9s de pasar por todos los mecanismos de recuperaci\u00f3n</span></p></body></html>", None))
        self.info_text_recep_inicio.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">En espera de inicializar el proceso de recepci\u00f3n</span></p></body></html>", None))
        self.text_recep.setHtml(QCoreApplication.translate("reception", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Se\u00f1al Recibida en Tiempo</span></p></body></html>", None))
        self.mesRecBtn.setText(QCoreApplication.translate("reception", u"Mensaje Recuperado", None))
        self.recBBBTN.setText(QCoreApplication.translate("reception", u"Se\u00f1al Banda - Base Recuperada", None))
        self.label_40.setText("")
        self.dataBtn.setText(QCoreApplication.translate("reception", u"Datos de la Se\u00f1al Recibida", None))
        self.SRBtn.setText(QCoreApplication.translate("reception", u"Se\u00f1al Recibida", None))
        self.DEPBtn.setText(QCoreApplication.translate("reception", u"D.E.P", None))
        self.ConstBtn.setText(QCoreApplication.translate("reception", u"Constelaci\u00f3n de la S.R.", None))
        self.SRBtn_2.setText(QCoreApplication.translate("reception", u"Bits Recuperados", None))
        self.DEPBtn_2.setText(QCoreApplication.translate("reception", u"D.E.P", None))
        self.ConstBtn_2.setText(QCoreApplication.translate("reception", u"Constelaci\u00f3n de la S.R.", None))
    # retranslateUi
