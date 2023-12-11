# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepageuDZeek.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1364, 755)
        MainWindow.setStyleSheet(u"*{\n"
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
"")
        self.centralwidget = QWidget(MainWindow)
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
        self.verticalLayout_8 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContaniner = QWidget(self.centerMenuContainer)
        self.centerMenuSubContaniner.setObjectName(u"centerMenuSubContaniner")
        self.centerMenuSubContaniner.setMinimumSize(QSize(0, 0))
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
        self.centerMenuSubContaniner_2.setMinimumSize(QSize(0, 0))
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
        self.guideContainer = QFrame(self.mainBodyContainer)
        self.guideContainer.setObjectName(u"guideContainer")
        self.guideContainer.setMinimumSize(QSize(500, 0))
        self.guideContainer.setMaximumSize(QSize(500, 16777215))
        self.guideContainer.setFrameShape(QFrame.StyledPanel)
        self.guideContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.guideContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 0, 0)
        self.textBrowser = QTextBrowser(self.guideContainer)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_12.addWidget(self.textBrowser)


        self.horizontalLayout_4.addWidget(self.guideContainer)

        self.mainRightContainer = QWidget(self.mainBodyContainer)
        self.mainRightContainer.setObjectName(u"mainRightContainer")
        self.mainRightContainer.setMinimumSize(QSize(350, 0))
        self.verticalLayout_11 = QVBoxLayout(self.mainRightContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.mainRightContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.textBrowser_3 = QTextBrowser(self.frame_7)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_14.addWidget(self.textBrowser_3)


        self.verticalLayout_11.addWidget(self.frame_7)


        self.horizontalLayout_4.addWidget(self.mainRightContainer, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menuBtn.setDefault(False)
        self.TranBtn.setDefault(False)
        self.RecepBtn.setDefault(False)
        self.InfoBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Pantalla de Inicio", None))
#if QT_CONFIG(tooltip)
        self.TranBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Trabaja como nodo transmisor", None))
#endif // QT_CONFIG(tooltip)
        self.TranBtn.setText(QCoreApplication.translate("MainWindow", u"Transmisi\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.RecepBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Trabajar como nodo receptor", None))
#endif // QT_CONFIG(tooltip)
        self.RecepBtn.setText(QCoreApplication.translate("MainWindow", u"Recepci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.InfoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"M\u00e1s informaci\u00f3n sobre la Herramienta", None))
#endif // QT_CONFIG(tooltip)
        self.InfoBtn.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
#if QT_CONFIG(shortcut)
        self.InfoBtn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Digital Comunications Toolkit", None))
        self.closeMBtn.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Seleccione el tipo de mensaje", None))
        self.textBtn_2.setText(QCoreApplication.translate("MainWindow", u"Texto", None))
        self.fileBtn_2.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Digital Comunications Toolkit", None))
        self.closeMBtn_2.setText("")
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; font-size:20pt; font-weight:600;\">Gu\u00eda de Inicio</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; font-size:12pt;\">1)Conecte el m\u00f3dulo ADALM-PLUTO al ordenador</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Bahnschrift Light'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; font-size:12pt;\">2)Escoja el modo de trabajo (Transmisi\u00f3n o Recepci\u00f3n)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Bahnschrift Light'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Ligh"
                        "t'; font-size:12pt;\">2.1)Si el modo escogido es &quot;Transmisi\u00f3n&quot;, escoja el tipo de mensaje a enviar</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/images/ADALM-PLUTO.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Bahnschrift Light'; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; font-size:14pt;\">M\u00f3dulo ADALM - PLUTO</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light'; font-size:11pt;\">El m\u00f3dulo de aprendizaje activo ADALM-PLUTO (PlutoSDR) es una herramienta creada por Analog Devices Inc. Ayuda a los usuarios a introducirse en los fundamentos de la radio definida por software (SDR), la radiofrecuencia (RF) y las comunicaciones.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Bahnschrift Light'; font-size:7.8pt;\"><br /></p></body></html>", None))
    # retranslateUi

