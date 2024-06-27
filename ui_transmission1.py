# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transmission1rwyCdq.ui'
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

class Ui_transmission1(object):
    def setupUi(self, transmission1):
        if not transmission1.objectName():
            transmission1.setObjectName(u"transmission1")
        transmission1.setEnabled(True)
        transmission1.resize(1753, 934)
        transmission1.setStyleSheet(u"*{\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	border: none;\n"
"}\n"
"\n"
"QToolTip { \n"
"	background-color: black; \n"
"	color: white; \n"
"	border: black solid 1px;\n"
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
"	bo"
                        "rder-style: inset;\n"
"\n"
"}\n"
"\n"
"#frame_5 QPushButton:hover{\n"
"	background-color: #acacac;\n"
"	border-radius: 25px\n"
"}\n"
"\n"
"#modStatus {\n"
"	background-color: #4d648d;\n"
"	border-top-left-radius: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"#doubleSpinBox, #doubleSpinBox_2, #doubleSpinBox_3, #doubleSpinBox_4 {\n"
"	border-width: 1px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#TxtBtn {\n"
"	background-color: #4d648d;\n"
"	text-align: center;\n"
"	border-radius: 7px;\n"
"	border-width: 1px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#TxtBtn:hover{\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#frame_10, #frame_9, #frame_23, #text {\n"
"	background-color: #fafade;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}\n"
"\n"
"#frame_7 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"}\n"
"\n"
"#frame_18, #frame_19, #frame_26, #frame_27, #frame_28 {\n"
"	background-color: #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-st"
                        "yle: inset;\n"
"\n"
"}\n"
"\n"
"#frame_22 QPushButton {\n"
"	background-color: #4d648d;\n"
"	border-width: 1px;\n"
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
"#frame_24 QPushButton:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#widget_2 QPushButton{\n"
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
"#widget_8, #widget_32, #widget_4 {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4d648d;\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(transmission1)
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

        self.widget_15 = QWidget(self.frame_2)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(16777215, 0))
        self.widget_15.setStyleSheet(u"#widget_15 QPushButton{\n"
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
"#widget_15 QPushButton:hover{\n"
"	background-color: #acacac;\n"
"	border-radius: 25px\n"
"}\n"
"\n"
"#widget_15 {\n"
"	background-color: #283655;\n"
"	padding: 7;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"	border-width: 1px;\n"
"	border-style: inset;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textBtn_4 = QPushButton(self.widget_15)
        self.textBtn_4.setObjectName(u"textBtn_4")
        self.textBtn_4.setMinimumSize(QSize(0, 0))
        self.textBtn_4.setMaximumSize(QSize(125, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light"])
        font2.setPointSize(10)
        self.textBtn_4.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/type.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textBtn_4.setIcon(icon3)
        self.textBtn_4.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.textBtn_4)

        self.fileBtn_4 = QPushButton(self.widget_15)
        self.fileBtn_4.setObjectName(u"fileBtn_4")
        self.fileBtn_4.setMinimumSize(QSize(0, 0))
        self.fileBtn_4.setMaximumSize(QSize(125, 16777215))
        self.fileBtn_4.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileBtn_4.setIcon(icon4)
        self.fileBtn_4.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.fileBtn_4)


        self.verticalLayout_3.addWidget(self.widget_15)

        self.RecepBtn = QPushButton(self.frame_2)
        self.RecepBtn.setObjectName(u"RecepBtn")
        self.RecepBtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/trending-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RecepBtn.setIcon(icon5)
        self.RecepBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.RecepBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.mainBodyContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainBodySubLeftContainer = QFrame(self.mainBodyContainer)
        self.mainBodySubLeftContainer.setObjectName(u"mainBodySubLeftContainer")
        self.mainBodySubLeftContainer.setFrameShape(QFrame.StyledPanel)
        self.mainBodySubLeftContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.mainBodySubLeftContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.frame_10 = QFrame(self.mainBodySubLeftContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(413, 200))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setStyleSheet(u"color: #000000;	\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.frame_10)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 80))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.text = QPlainTextEdit(self.frame_6)
        self.text.setObjectName(u"text")
        self.text.setFont(font2)
        self.text.setStyleSheet(u"#text {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.text)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_16)

        self.codeBox = QComboBox(self.frame_10)
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.setObjectName(u"codeBox")
        self.codeBox.setFont(font2)
        self.codeBox.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_10.addWidget(self.codeBox)

        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift Light"])
        font3.setPointSize(10)
        font3.setUnderline(False)
        self.label_14.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_14)

        self.UmbPreBtn = QRadioButton(self.frame_10)
        self.UmbPreBtn.setObjectName(u"UmbPreBtn")
        self.UmbPreBtn.setFont(font2)

        self.verticalLayout_10.addWidget(self.UmbPreBtn)

        self.UmbDisBtn = QRadioButton(self.frame_10)
        self.UmbDisBtn.setObjectName(u"UmbDisBtn")
        self.UmbDisBtn.setFont(font2)

        self.verticalLayout_10.addWidget(self.UmbDisBtn)

        self.widget_3 = QWidget(self.frame_10)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(16777215, 0))
        self.widget_3.setStyleSheet(u"#widget_3 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.widget_3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.stackedWidget_4 = QStackedWidget(self.widget_3)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_28 = QVBoxLayout(self.page_12)
        self.verticalLayout_28.setSpacing(7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.page_12)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift Light"])
        font4.setPointSize(9)
        font4.setUnderline(False)
        self.label_8.setFont(font4)

        self.verticalLayout_28.addWidget(self.label_8)

        self.simPBitBox = QComboBox(self.page_12)
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.addItem("")
        self.simPBitBox.setObjectName(u"simPBitBox")
        self.simPBitBox.setFont(font2)
        self.simPBitBox.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_28.addWidget(self.simPBitBox)

        self.stackedWidget_4.addWidget(self.page_12)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.verticalLayout_29 = QVBoxLayout(self.page_14)
        self.verticalLayout_29.setSpacing(7)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.page_14)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.verticalLayout_29.addWidget(self.label_19)

        self.simPBitBox_2 = QComboBox(self.page_14)
        self.simPBitBox_2.addItem("")
        self.simPBitBox_2.addItem("")
        self.simPBitBox_2.addItem("")
        self.simPBitBox_2.setObjectName(u"simPBitBox_2")
        self.simPBitBox_2.setFont(font2)
        self.simPBitBox_2.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_29.addWidget(self.simPBitBox_2)

        self.stackedWidget_4.addWidget(self.page_14)

        self.verticalLayout_30.addWidget(self.stackedWidget_4)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.widget = QWidget(self.frame_10)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 0))
        self.widget.setStyleSheet(u"#widget {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")
        self.verticalLayout_34 = QVBoxLayout(self.widget)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.stackedWidget_5 = QStackedWidget(self.widget)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.verticalLayout_22 = QVBoxLayout(self.page_18)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_44 = QFrame(self.page_18)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_44)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.frame_44, 0, Qt.AlignRight|Qt.AlignTop)

        self.stackedWidget_5.addWidget(self.page_18)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.verticalLayout_35 = QVBoxLayout(self.page_13)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.page_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_35.addWidget(self.label_6)

        self.modBox = QComboBox(self.page_13)
        self.modBox.addItem("")
        self.modBox.addItem("")
        self.modBox.addItem("")
        self.modBox.addItem("")
        self.modBox.addItem("")
        self.modBox.setObjectName(u"modBox")
        self.modBox.setFont(font1)
        self.modBox.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_35.addWidget(self.modBox)

        self.stackedWidget_5.addWidget(self.page_13)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.verticalLayout_36 = QVBoxLayout(self.page_15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.page_15)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_36.addWidget(self.label_15)

        self.modBox_2 = QComboBox(self.page_15)
        self.modBox_2.addItem("")
        self.modBox_2.addItem("")
        self.modBox_2.addItem("")
        self.modBox_2.addItem("")
        self.modBox_2.setObjectName(u"modBox_2")
        self.modBox_2.setFont(font1)
        self.modBox_2.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_36.addWidget(self.modBox_2)

        self.stackedWidget_5.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_37 = QVBoxLayout(self.page_16)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.page_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.verticalLayout_37.addWidget(self.label_17)

        self.modBox_3 = QComboBox(self.page_16)
        self.modBox_3.addItem("")
        self.modBox_3.addItem("")
        self.modBox_3.addItem("")
        self.modBox_3.addItem("")
        self.modBox_3.setObjectName(u"modBox_3")
        self.modBox_3.setFont(font1)
        self.modBox_3.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_37.addWidget(self.modBox_3)

        self.stackedWidget_5.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.verticalLayout_38 = QVBoxLayout(self.page_17)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.page_17)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_38.addWidget(self.label_18)

        self.modBox_4 = QComboBox(self.page_17)
        self.modBox_4.addItem("")
        self.modBox_4.addItem("")
        self.modBox_4.addItem("")
        self.modBox_4.setObjectName(u"modBox_4")
        self.modBox_4.setFont(font1)
        self.modBox_4.setStyleSheet(u"	background-color: #769ad8;\n"
"	border-width: 1px;\n"
"	border-style: inset;")

        self.verticalLayout_38.addWidget(self.modBox_4)

        self.stackedWidget_5.addWidget(self.page_17)

        self.verticalLayout_34.addWidget(self.stackedWidget_5)


        self.verticalLayout_10.addWidget(self.widget)


        self.verticalLayout_9.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.mainBodySubLeftContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.frame_8)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.verticalLayout_11 = QVBoxLayout(self.widget_8)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift Light"])
        font5.setPointSize(10)
        font5.setUnderline(True)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"	color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_5)

        self.fbit = QDoubleSpinBox(self.widget_8)
        self.fbit.setObjectName(u"fbit")
        self.fbit.setFont(font2)
        self.fbit.setDecimals(2)
        self.fbit.setMaximum(1000000.000000000000000)

        self.verticalLayout_11.addWidget(self.fbit)

        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"	color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_4)

        self.tbit = QDoubleSpinBox(self.widget_8)
        self.tbit.setObjectName(u"tbit")
        self.tbit.setFont(font2)
        self.tbit.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.tbit.setDecimals(8)
        self.tbit.setMaximum(10.000000000000000)

        self.verticalLayout_11.addWidget(self.tbit)

        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)

        self.verticalLayout_11.addWidget(self.label_3)

        self.fport = QDoubleSpinBox(self.widget_8)
        self.fport.setObjectName(u"fport")
        self.fport.setFont(font3)
        self.fport.setMinimum(325.000000000000000)
        self.fport.setMaximum(3500.000000000000000)

        self.verticalLayout_11.addWidget(self.fport, 0, Qt.AlignLeft)


        self.horizontalLayout_27.addWidget(self.widget_8, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.mainBodySubLeftContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.widget_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_15)
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_32 = QWidget(self.frame_15)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(0, 174))
        self.widget_32.setMaximumSize(QSize(220, 200))
        self.widget_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_41 = QVBoxLayout(self.widget_32)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.stackedWidget_8 = QStackedWidget(self.widget_32)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.verticalLayout_69 = QVBoxLayout(self.page_24)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.frame_43 = QFrame(self.page_24)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_43)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")

        self.verticalLayout_69.addWidget(self.frame_43, 0, Qt.AlignRight|Qt.AlignTop)

        self.stackedWidget_8.addWidget(self.page_24)
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.verticalLayout_67 = QVBoxLayout(self.page_25)
        self.verticalLayout_67.setSpacing(20)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_23 = QLabel(self.page_25)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)

        self.verticalLayout_67.addWidget(self.label_23)

        self.radioButton_2 = QRadioButton(self.page_25)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font2)

        self.verticalLayout_67.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.page_25)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font2)

        self.verticalLayout_67.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.page_25)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font2)

        self.verticalLayout_67.addWidget(self.radioButton_4)

        self.stackedWidget_8.addWidget(self.page_25)
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.verticalLayout_66 = QVBoxLayout(self.page_26)
        self.verticalLayout_66.setSpacing(20)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_22 = QLabel(self.page_26)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)

        self.verticalLayout_66.addWidget(self.label_22, 0, Qt.AlignTop)

        self.radioButton_5 = QRadioButton(self.page_26)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font2)

        self.verticalLayout_66.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.page_26)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font2)

        self.verticalLayout_66.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.page_26)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setFont(font2)

        self.verticalLayout_66.addWidget(self.radioButton_7)

        self.stackedWidget_8.addWidget(self.page_26)

        self.verticalLayout_41.addWidget(self.stackedWidget_8, 0, Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.widget_32)

        self.widget_4 = QWidget(self.frame_15)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(220, 200))
        self.widget_4.setStyleSheet(u"	color: rgb(255, 255, 255);")
        self.verticalLayout_25 = QVBoxLayout(self.widget_4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 9, -1, -1)
        self.stackedWidget_6 = QStackedWidget(self.widget_4)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.verticalLayout_31 = QVBoxLayout(self.page_21)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.page_21)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_30)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")

        self.verticalLayout_31.addWidget(self.frame_30, 0, Qt.AlignRight|Qt.AlignTop)

        self.stackedWidget_6.addWidget(self.page_21)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.verticalLayout_26 = QVBoxLayout(self.page_19)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.page_19)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.text_4 = QPlainTextEdit(self.page_19)
        self.text_4.setObjectName(u"text_4")
        self.text_4.setMaximumSize(QSize(16777215, 40))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift Light"])
        font6.setUnderline(False)
        self.text_4.setFont(font6)
        self.text_4.setStyleSheet(u"#text_4 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.text_4, 0, Qt.AlignTop)

        self.text_3 = QPlainTextEdit(self.page_19)
        self.text_3.setObjectName(u"text_3")
        self.text_3.setMaximumSize(QSize(16777215, 40))
        self.text_3.setFont(font6)
        self.text_3.setStyleSheet(u"#text_3 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.text_3, 0, Qt.AlignTop)

        self.stackedWidget_6.addWidget(self.page_19)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.verticalLayout_27 = QVBoxLayout(self.page_20)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.page_20)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_27.addWidget(self.label_20)

        self.text_8 = QPlainTextEdit(self.page_20)
        self.text_8.setObjectName(u"text_8")
        self.text_8.setMaximumSize(QSize(16777215, 30))
        self.text_8.setFont(font6)
        self.text_8.setStyleSheet(u"#text_8 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")

        self.verticalLayout_27.addWidget(self.text_8)

        self.text_5 = QPlainTextEdit(self.page_20)
        self.text_5.setObjectName(u"text_5")
        self.text_5.setMaximumSize(QSize(16777215, 30))
        self.text_5.setFont(font6)
        self.text_5.setStyleSheet(u"#text_5 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")

        self.verticalLayout_27.addWidget(self.text_5)

        self.text_9 = QPlainTextEdit(self.page_20)
        self.text_9.setObjectName(u"text_9")
        self.text_9.setMaximumSize(QSize(16777215, 30))
        self.text_9.setFont(font6)
        self.text_9.setStyleSheet(u"#text_9 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")

        self.verticalLayout_27.addWidget(self.text_9)

        self.text_7 = QPlainTextEdit(self.page_20)
        self.text_7.setObjectName(u"text_7")
        self.text_7.setMaximumSize(QSize(16777215, 30))
        self.text_7.setFont(font6)
        self.text_7.setStyleSheet(u"#text_7 {\n"
"	border-width: 1px;\n"
"	border-radius: 7px;\n"
"	border-style: inset;\n"
"\n"
"}")

        self.verticalLayout_27.addWidget(self.text_7)

        self.stackedWidget_6.addWidget(self.page_20)

        self.verticalLayout_25.addWidget(self.stackedWidget_6, 0, Qt.AlignTop)


        self.verticalLayout_23.addWidget(self.widget_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_9.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.frame_14 = QFrame(self.widget_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(100, 0))
        self.frame_14.setMaximumSize(QSize(190, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_14)
        self.verticalLayout_40.setSpacing(8)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.preSPBtn = QPushButton(self.frame_14)
        self.preSPBtn.setObjectName(u"preSPBtn")
        self.preSPBtn.setMinimumSize(QSize(175, 0))
        self.preSPBtn.setFont(font1)
        self.preSPBtn.setStyleSheet(u"#preSPBtn:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#preSPBtn {\n"
"	text-align: center\n"
"}")

        self.verticalLayout_40.addWidget(self.preSPBtn, 0, Qt.AlignHCenter)

        self.preSMBtn = QPushButton(self.frame_14)
        self.preSMBtn.setObjectName(u"preSMBtn")
        self.preSMBtn.setMinimumSize(QSize(175, 0))
        self.preSMBtn.setFont(font1)
        self.preSMBtn.setStyleSheet(u"#preSMBtn:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"\n"
"#preSMBtn {\n"
"	text-align: center\n"
"}")

        self.verticalLayout_40.addWidget(self.preSMBtn, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.ConfBtn = QPushButton(self.frame_14)
        self.ConfBtn.setObjectName(u"ConfBtn")
        self.ConfBtn.setMinimumSize(QSize(175, 0))
        self.ConfBtn.setFont(font1)
        self.ConfBtn.setStyleSheet(u"#ConfBtn {\n"
"	background-color: rgb(238, 146, 143);\n"
"	text-align: center\n"
"}\n"
"\n"
"#ConfBtn:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"")

        self.verticalLayout_40.addWidget(self.ConfBtn, 0, Qt.AlignHCenter)

        self.widget_5 = QWidget(self.frame_14)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 0))
        self.verticalLayout_39 = QVBoxLayout(self.widget_5)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.TransBtn = QPushButton(self.widget_5)
        self.TransBtn.setObjectName(u"TransBtn")
        self.TransBtn.setMinimumSize(QSize(175, 0))
        self.TransBtn.setFont(font1)
        self.TransBtn.setStyleSheet(u"#TransBtn {\n"
"	background-color: rgb(238, 146, 143);\n"
"	text-align: center\n"
"}\n"
"\n"
"#TransBtn:hover {\n"
"	background-color: #acacac;\n"
"}\n"
"")

        self.verticalLayout_39.addWidget(self.TransBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_40.addWidget(self.widget_5)

        self.simWarnTxt = QTextBrowser(self.frame_14)
        self.simWarnTxt.setObjectName(u"simWarnTxt")
        self.simWarnTxt.setMaximumSize(QSize(16777215, 100))
        self.simWarnTxt.setFont(font2)
        self.simWarnTxt.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout_40.addWidget(self.simWarnTxt)

        self.widget_6 = QWidget(self.frame_14)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout_33 = QVBoxLayout(self.widget_6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.ConfigSig = QTextBrowser(self.widget_6)
        self.ConfigSig.setObjectName(u"ConfigSig")
        self.ConfigSig.setFont(font2)
        self.ConfigSig.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.verticalLayout_33.addWidget(self.ConfigSig)


        self.verticalLayout_40.addWidget(self.widget_6)


        self.horizontalLayout_9.addWidget(self.frame_14, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.widget_2)


        self.horizontalLayout_4.addWidget(self.mainBodySubLeftContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.mainBodySubRightContainer = QFrame(self.mainBodyContainer)
        self.mainBodySubRightContainer.setObjectName(u"mainBodySubRightContainer")
        self.mainBodySubRightContainer.setFrameShape(QFrame.StyledPanel)
        self.mainBodySubRightContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.mainBodySubRightContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_9 = QFrame(self.mainBodySubRightContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 520))
        self.frame_9.setMaximumSize(QSize(16777215, 520))
        self.frame_9.setStyleSheet(u"	color: #000000;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(140, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mSim = QLCDNumber(self.frame_11)
        self.mSim.setObjectName(u"mSim")
        font7 = QFont()
        font7.setFamilies([u"Bahnschrift Light"])
        font7.setPointSize(14)
        self.mSim.setFont(font7)
        self.mSim.setFrameShape(QFrame.Panel)
        self.mSim.setFrameShadow(QFrame.Sunken)
        self.mSim.setLineWidth(0)
        self.mSim.setMidLineWidth(0)
        self.mSim.setSmallDecimalPoint(True)
        self.mSim.setDigitCount(9)
        self.mSim.setSegmentStyle(QLCDNumber.Flat)
        self.mSim.setProperty("value", 0.000000000000000)
        self.mSim.setProperty("intValue", 0)

        self.horizontalLayout_7.addWidget(self.mSim)


        self.horizontalLayout_8.addWidget(self.frame_11)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_11)


        self.verticalLayout_12.addWidget(self.frame_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_21 = QFrame(self.frame_9)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 200))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 10, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_12)

        self.prevBBBTN = QPushButton(self.frame_22)
        self.prevBBBTN.setObjectName(u"prevBBBTN")
        self.prevBBBTN.setFont(font2)
        self.prevBBBTN.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_22.addWidget(self.prevBBBTN)

        self.prevPBBtn = QPushButton(self.frame_22)
        self.prevPBBtn.setObjectName(u"prevPBBtn")
        self.prevPBBtn.setFont(font2)
        self.prevPBBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_22.addWidget(self.prevPBBtn)


        self.verticalLayout_13.addWidget(self.frame_22)

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
        self.prevPBlayout = QVBoxLayout()
        self.prevPBlayout.setSpacing(7)
        self.prevPBlayout.setObjectName(u"prevPBlayout")

        self.horizontalLayout_21.addLayout(self.prevPBlayout)


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
        self.horizontalLayout_20 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.recBBlayout = QVBoxLayout()
        self.recBBlayout.setSpacing(7)
        self.recBBlayout.setObjectName(u"recBBlayout")

        self.horizontalLayout_20.addLayout(self.recBBlayout)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.stackedWidget_2.addWidget(self.page_3)

        self.verticalLayout_13.addWidget(self.stackedWidget_2)


        self.verticalLayout_12.addWidget(self.frame_21)


        self.verticalLayout_16.addWidget(self.frame_9)

        self.frame_23 = QFrame(self.mainBodySubRightContainer)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 430))
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
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
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_25)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_23.addWidget(self.label_13)

        self.prevMSBtn = QPushButton(self.frame_25)
        self.prevMSBtn.setObjectName(u"prevMSBtn")
        self.prevMSBtn.setFont(font2)
        self.prevMSBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_23.addWidget(self.prevMSBtn)

        self.prevDEPBtn = QPushButton(self.frame_25)
        self.prevDEPBtn.setObjectName(u"prevDEPBtn")
        self.prevDEPBtn.setFont(font2)
        self.prevDEPBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_23.addWidget(self.prevDEPBtn)

        self.prevConstBtn = QPushButton(self.frame_25)
        self.prevConstBtn.setObjectName(u"prevConstBtn")
        self.prevConstBtn.setFont(font2)
        self.prevConstBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.horizontalLayout_23.addWidget(self.prevConstBtn)


        self.verticalLayout_17.addWidget(self.frame_25)

        self.stackedWidget_3 = QStackedWidget(self.frame_24)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 250))
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
        self.prevConstlayout = QVBoxLayout()
        self.prevConstlayout.setSpacing(7)
        self.prevConstlayout.setObjectName(u"prevConstlayout")

        self.horizontalLayout_24.addLayout(self.prevConstlayout)


        self.verticalLayout_18.addWidget(self.frame_26)

        self.stackedWidget_3.addWidget(self.page_9)
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
        self.prevMSlayout = QVBoxLayout()
        self.prevMSlayout.setSpacing(7)
        self.prevMSlayout.setObjectName(u"prevMSlayout")

        self.horizontalLayout_25.addLayout(self.prevMSlayout)


        self.verticalLayout_19.addWidget(self.frame_27)

        self.stackedWidget_3.addWidget(self.page_10)
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
        self.prevDEPlayout = QVBoxLayout()
        self.prevDEPlayout.setSpacing(7)
        self.prevDEPlayout.setObjectName(u"prevDEPlayout")

        self.horizontalLayout_26.addLayout(self.prevDEPlayout)


        self.verticalLayout_21.addWidget(self.frame_28)

        self.stackedWidget_3.addWidget(self.page_11)

        self.verticalLayout_17.addWidget(self.stackedWidget_3)


        self.verticalLayout_20.addWidget(self.frame_24)


        self.verticalLayout_16.addWidget(self.frame_23)


        self.horizontalLayout_4.addWidget(self.mainBodySubRightContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        transmission1.setCentralWidget(self.centralwidget)
        self.mainBodyContainer.raise_()
        self.leftMenuContainer.raise_()

        self.retranslateUi(transmission1)

        self.menuBtn.setDefault(False)
        self.TranBtn.setDefault(False)
        self.RecepBtn.setDefault(False)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_5.setCurrentIndex(2)
        self.stackedWidget_8.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(transmission1)
    # setupUi

    def retranslateUi(self, transmission1):
        transmission1.setWindowTitle(QCoreApplication.translate("transmission1", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("transmission1", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.HomeBtn.setToolTip(QCoreApplication.translate("transmission1", u"Pantalla de Inicio", None))
#endif // QT_CONFIG(tooltip)
        self.HomeBtn.setText(QCoreApplication.translate("transmission1", u"Pantalla de Inicio", None))
#if QT_CONFIG(tooltip)
        self.TranBtn.setToolTip(QCoreApplication.translate("transmission1", u"Trabaja como nodo transmisor", None))
#endif // QT_CONFIG(tooltip)
        self.TranBtn.setText(QCoreApplication.translate("transmission1", u"Transmisi\u00f3n", None))
        self.textBtn_4.setText(QCoreApplication.translate("transmission1", u"Texto", None))
        self.fileBtn_4.setText(QCoreApplication.translate("transmission1", u"Archivo", None))
#if QT_CONFIG(tooltip)
        self.RecepBtn.setToolTip(QCoreApplication.translate("transmission1", u"Trabajar como nodo receptor", None))
#endif // QT_CONFIG(tooltip)
        self.RecepBtn.setText(QCoreApplication.translate("transmission1", u"Recepci\u00f3n", None))
        self.text.setPlaceholderText(QCoreApplication.translate("transmission1", u"Escriba el mensaje a transmitir.", None))
        self.label_16.setText(QCoreApplication.translate("transmission1", u"Escoja el tipo de c\u00f3digo de l\u00ednea (Solo referencial):", None))
        self.codeBox.setItemText(0, "")
        self.codeBox.setItemText(1, QCoreApplication.translate("transmission1", u"NRZu (Non Return to Zero Unipolar)", None))
        self.codeBox.setItemText(2, QCoreApplication.translate("transmission1", u"NRZp (Non Return to Zero Polar)", None))
        self.codeBox.setItemText(3, QCoreApplication.translate("transmission1", u"RZu (Return to Zero Unipolar)", None))
        self.codeBox.setItemText(4, QCoreApplication.translate("transmission1", u"RZp (Return to Zero Polar)", None))
        self.codeBox.setItemText(5, QCoreApplication.translate("transmission1", u"AMI (Alternate Mark Inversion)", None))
        self.codeBox.setItemText(6, QCoreApplication.translate("transmission1", u"Manchester", None))

        self.label_14.setText(QCoreApplication.translate("transmission1", u"\u00bfC\u00f3mo prefiere configurar la modulaci\u00f3n de la se\u00f1al?", None))
        self.UmbPreBtn.setText(QCoreApplication.translate("transmission1", u"Modulaci\u00f3n previamente definida ", None))
        self.UmbDisBtn.setText(QCoreApplication.translate("transmission1", u"Dise\u00f1ar la constelaci\u00f3n de la se\u00f1al", None))
        self.label_8.setText(QCoreApplication.translate("transmission1", u"Escoja la cantidad de bits codificados por simbolo para la se\u00f1al:", None))
        self.simPBitBox.setItemText(0, "")
        self.simPBitBox.setItemText(1, QCoreApplication.translate("transmission1", u"1 bit codificado por simbolo", None))
        self.simPBitBox.setItemText(2, QCoreApplication.translate("transmission1", u"2 bits codificados por simbolo", None))
        self.simPBitBox.setItemText(3, QCoreApplication.translate("transmission1", u"3 bits codificados por simbolo", None))
        self.simPBitBox.setItemText(4, QCoreApplication.translate("transmission1", u"4 bits codificados por simbolo", None))

        self.label_19.setText(QCoreApplication.translate("transmission1", u"Escoja la cantidad de bits codificados por simbolo para la se\u00f1al:", None))
        self.simPBitBox_2.setItemText(0, "")
        self.simPBitBox_2.setItemText(1, QCoreApplication.translate("transmission1", u"1 bit codificado por simbolo", None))
        self.simPBitBox_2.setItemText(2, QCoreApplication.translate("transmission1", u"2 bits codifcados por simbolo", None))

        self.label_6.setText(QCoreApplication.translate("transmission1", u"Escoja el tipo de Modulaci\u00f3n:", None))
        self.modBox.setItemText(0, "")
        self.modBox.setItemText(1, QCoreApplication.translate("transmission1", u"ASK (Amplitude Shift Keying) ", None))
        self.modBox.setItemText(2, QCoreApplication.translate("transmission1", u"OOK (On - Off Keying)", None))
        self.modBox.setItemText(3, QCoreApplication.translate("transmission1", u"BPSK (Phase Shift Keying)", None))
        self.modBox.setItemText(4, QCoreApplication.translate("transmission1", u"FSK (Frecuency Shift Keying)", None))

        self.label_15.setText(QCoreApplication.translate("transmission1", u"Escoja el tipo de Modulaci\u00f3n:", None))
        self.modBox_2.setItemText(0, "")
        self.modBox_2.setItemText(1, QCoreApplication.translate("transmission1", u"QPSK - Variante de simbolos sobre los ejes", None))
        self.modBox_2.setItemText(2, QCoreApplication.translate("transmission1", u"QPSK (Phase Shift Keying)", None))
        self.modBox_2.setItemText(3, QCoreApplication.translate("transmission1", u"4-ASK (Amplitude Shift Keying) ", None))

        self.label_17.setText(QCoreApplication.translate("transmission1", u"Escoja el tipo de Modulaci\u00f3n:", None))
        self.modBox_3.setItemText(0, "")
        self.modBox_3.setItemText(1, QCoreApplication.translate("transmission1", u"8-ASK (Amplitude Shift Keying)", None))
        self.modBox_3.setItemText(2, QCoreApplication.translate("transmission1", u"8-PSK (Phase Shift Keying)", None))
        self.modBox_3.setItemText(3, QCoreApplication.translate("transmission1", u"8QAM (Quadrature Amplitude Modulation)", None))

        self.label_18.setText(QCoreApplication.translate("transmission1", u"Escoja el tipo de Modulaci\u00f3n:", None))
        self.modBox_4.setItemText(0, "")
        self.modBox_4.setItemText(1, QCoreApplication.translate("transmission1", u"16-PSK (Phase Shift Keying)", None))
        self.modBox_4.setItemText(2, QCoreApplication.translate("transmission1", u"16QAM (Quadrature Amplitude Modulation)", None))

        self.label_5.setText(QCoreApplication.translate("transmission1", u"Defina fsim (frecuencia de simbolo) - En base al tiempo de simbolo (Hz)", None))
        self.label_4.setText(QCoreApplication.translate("transmission1", u"Defina tsim (tiempo de simbolo) -  En base a la frecuencia de simbolo (s)", None))
        self.label_3.setText(QCoreApplication.translate("transmission1", u"Defina la frecuencia de Portadora (MHz - Max: 3500 - Min: 325)", None))
        self.label_23.setText(QCoreApplication.translate("transmission1", u"Defina la variante", None))
        self.radioButton_2.setText(QCoreApplication.translate("transmission1", u"Variante A", None))
        self.radioButton_3.setText(QCoreApplication.translate("transmission1", u"Variante B", None))
        self.radioButton_4.setText(QCoreApplication.translate("transmission1", u"Variante C", None))
        self.label_22.setText(QCoreApplication.translate("transmission1", u"Defina la variante", None))
        self.radioButton_5.setText(QCoreApplication.translate("transmission1", u"Rectangular", None))
        self.radioButton_6.setText(QCoreApplication.translate("transmission1", u"Circular", None))
        self.radioButton_7.setText(QCoreApplication.translate("transmission1", u"Estrella", None))
        self.label_7.setText(QCoreApplication.translate("transmission1", u"Escriba a los simb, de la forma x + yj", None))
        self.text_4.setPlaceholderText(QCoreApplication.translate("transmission1", u"Escriba el simbolo 1", None))
        self.text_3.setPlaceholderText(QCoreApplication.translate("transmission1", u"Escriba el simbolo 2", None))
        self.label_20.setText(QCoreApplication.translate("transmission1", u"Escriba a los simb, de la forma x + yj", None))
        self.text_8.setPlaceholderText(QCoreApplication.translate("transmission1", u"Escriba el simbolo 1", None))
        self.text_5.setPlaceholderText(QCoreApplication.translate("transmission1", u"Escriba el simbolo 2", None))
        self.text_9.setPlaceholderText(QCoreApplication.translate("transmission1", u"Escriba el simbolo 3", None))
        self.text_7.setPlaceholderText(QCoreApplication.translate("transmission1", u"Escriba el simbolo 4", None))
        self.preSPBtn.setText(QCoreApplication.translate("transmission1", u"Graficar Bits a transmitir", None))
        self.preSMBtn.setText(QCoreApplication.translate("transmission1", u"Graficar Se\u00f1al Banda-Base \n"
"y Pasa-Banda ", None))
        self.ConfBtn.setText(QCoreApplication.translate("transmission1", u"Configurar Se\u00f1al", None))
        self.TransBtn.setText(QCoreApplication.translate("transmission1", u"Transmitir Se\u00f1al", None))
        self.simWarnTxt.setHtml(QCoreApplication.translate("transmission1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.ConfigSig.setHtml(QCoreApplication.translate("transmission1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("transmission1", u"Cantidad de M-Simbolos", None))
        self.label_12.setText(QCoreApplication.translate("transmission1", u"Previsualizaci\u00f3n:", None))
        self.prevBBBTN.setText(QCoreApplication.translate("transmission1", u"Se\u00f1al Banda - Base IQ", None))
        self.prevPBBtn.setText(QCoreApplication.translate("transmission1", u"Bits a transmitir ", None))
        self.label_13.setText(QCoreApplication.translate("transmission1", u"Previsualizaci\u00f3n:", None))
        self.prevMSBtn.setText(QCoreApplication.translate("transmission1", u"Se\u00f1al Pasa - Banda", None))
        self.prevDEPBtn.setText(QCoreApplication.translate("transmission1", u"D.E.P", None))
        self.prevConstBtn.setText(QCoreApplication.translate("transmission1", u"Constelaci\u00f3n de la S.T.", None))
    # retranslateUi

