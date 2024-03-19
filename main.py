#Animation Libraries
import platform
from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtCore import QRunnable, Slot, QThreadPool
import traceback, sys
from PySide2.QtGui import QIcon


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# GUI FILE
from ui_homepage import Ui_MainWindow
from ui_reception import Ui_reception
from ui_transmission1 import Ui_transmission1
from ui_transmission2 import Ui_transmission2
from ui_functions import *

import pyqtgraph as pg
import time
import threading
import os

import adi

from scipy import interpolate
from scipy import signal
import sys
import numpy as np
from matplotlib import pyplot as plt
import math
from commpy.filters import rrcosfilter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PIL import Image
import zipfile
import gc

import random
from random import randint

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # opening window in maximized size 
        self.showMaximized() 
        
        self.setWindowTitle("Digital Comunications Toolkit")

        
        ## TOGGLE/MENU
        ########################################################################
        self.ui.menuBtn.clicked.connect(lambda: MainFunctions.toggleMenu(self, 180, True))
        
        #BUTTON ACTIONS       
        #TRANSMISSION
        #############################################################################################       
        self.ui.TranBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
            
        #INFO
        #############################################################################################              
        self.ui.InfoBtn.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))       

        #CLOSE
        #############################################################################################       
        self.ui.closeMBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        self.ui.closeMBtn_2.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))
        
        #RECEPTION PAGE
        #############################################################################################
        self.ui.RecepBtn.clicked.connect(self.open_reception)
        self.ui.RecepBtn.clicked.connect(self.close)
        
        #TRANSMISSION-TEXT PAGE
        #############################################################################################
        self.ui.textBtn_2.clicked.connect(self.open_transmission1)
        self.ui.textBtn_2.clicked.connect(self.close)
        
        #TRANSMISSION-ARCHIVE PAGE
        #############################################################################################
        self.ui.fileBtn_2.clicked.connect(self.open_transmission2)
        self.ui.fileBtn_2.clicked.connect(self.close) 
          
        self.show()
    
    def open_homepage(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.ventana)

        # opening window in maximized size 
        self.ventana.showMaximized() 
        
        self.ventana.setWindowTitle("Digital Comunications Toolkit")
        
        ## TOGGLE/MENU
        ########################################################################
        self.ui.menuBtn.clicked.connect(lambda: MainFunctions.toggleMenu(self, 180, True))
        
        #BUTTON ACTIONS       
        #TRANSMISSION
        #############################################################################################       
        self.ui.TranBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
            
        #INFO
        #############################################################################################              
        self.ui.InfoBtn.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))       

        #CLOSE
        #############################################################################################       
        self.ui.closeMBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        self.ui.closeMBtn_2.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))
        
        #RECEPTION PAGE
        #############################################################################################
        self.ui.RecepBtn.clicked.connect(self.open_reception)
        self.ui.RecepBtn.clicked.connect(self.close)
        
        #TRANSMISSION-TEXT PAGE
        #############################################################################################
        self.ui.textBtn_2.clicked.connect(self.open_transmission1)
        self.ui.textBtn_2.clicked.connect(self.close)
        
        #TRANSMISSION-ARCHIVE PAGE
        #############################################################################################
        self.ui.fileBtn_2.clicked.connect(self.open_transmission2)
        self.ui.fileBtn_2.clicked.connect(self.close) 
        
        self.ventana.show()
        
    
    def open_reception(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_reception()
        self.ui.setupUi(self.ventana)

        # opening window in maximized size 
        self.ventana.showMaximized() 
        #self.ventana.setFixedHeight(800)
        self.fsample = 522000
        
        #REAL TIME GRAPH NECESARY OBJECTS
        self.timer = QtCore.QTimer()
        #self.graphWidget = pg.PlotWidget(background= "w")
        #self.graphWidget_2 = pg.PlotWidget(background= "w")
        #self.graphWidget_3 = pg.PlotWidget(background= "w")
        #self.graphWidget_4 = pg.PlotWidget(background= "w")
        
        #FLAGS
        self.BB_graph_flag = False
        self.delete_status = False
        self.format_path_flag_received = False
        self.defined_threshold_flag = False
        self.user_defined_threshold_flag = False
        self.df_threshold_options = False
        self.user_df_threshold_options = False

        self.user_defined_symbols_flag = False
        
        self.add_threshold_2_symbols_flag = False
        self.add_threshold_4_symbols_flag = False
        self.add_threshold_4_symbols_2_flag = False
        
        self.reception_initiated_prev = False
        self.reception_configured = False
        self.graphics_final_fase = False
        
        #self.ui.stackedWidget_25.setCurrentWidget(self.ui.page_37)
        #self.ui.finalInfo_2.setText("A continuación se presenta información relacionada de la señal recibida:" + "\n\n" + 
        #                            "Cantidad total de bits recibidos: " + "12222" + "\n\n" +
        #                            "Cantidad total de simbolos recibidos: " + "40000")

        #WINDOW ICON
        self.ventana.setWindowTitle("Digital Comunications Toolkit - Reception Mode")
        
        ## TOGGLE/MENU
        ########################################################################
        self.ui.menuBtn.clicked.connect(lambda: MainFunctions.toggleMenu(self, 180, True))
        
        
############################################################################################# 
        #BUTTON ACTIONS

        #TRANSMISSION      
        self.ui.TranBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        #self.ui.TranBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
            
        #INFO             
        self.ui.InfoBtn.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))       
        #self.ui.InfoBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))

        #CLOSE       
        self.ui.closeMBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        self.ui.closeMBtn_2.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))
        
        #HOME PAGE
        self.ui.HomeBtn.clicked.connect(self.open_homepage)
        self.ui.HomeBtn.clicked.connect(self.close)
        
        #TRANSMISSION-TEXT PAGE
        self.ui.textBtn_2.clicked.connect(self.open_transmission1)
        self.ui.textBtn_2.clicked.connect(self.close)
        
        #TRANSMISSION-ARCHIVE PAGE
        self.ui.fileBtn_2.clicked.connect(self.open_transmission2)
        self.ui.fileBtn_2.clicked.connect(self.close)


#####################################################################################
        #RECEPTION GRAPHS BUTTONS
        self.ui.graph_recep.clicked.connect(self.recep_filter_signal)
        self.ui.graph_recep_2.clicked.connect(self.recep_freq_fase_signal)
        self.ui.graph_recep_1.clicked.connect(self.recep_time_sync_signal)
        self.ui.graph_recep_0.clicked.connect(self.recep_error_correc_signal)

#####################################################################################

        #CHOOSE PATH
        self.filePath_message_received = ""
        self.ui.ArchiveBtn.clicked.connect(self.setArchive)

        #RECEIVED MESSAGE FORMAT
        self.ui.formatBox.activated.connect(self.format_box_animation_desicion)
        
########################################################################################################## SIGNAL RECEIVED AND RECOVERED

        #INFO ABOUT THE SIGNAL
        self.ui.dataBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_14))
        
        #SIGNAL RECEIVED 
        self.ui.SRBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_10))
      
        #DEP
        self.ui.DEPBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11))

        #CONSTELATION
        self.ui.ConstBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_9))
        
        #BAND BASE RETRIEVED
        self.ui.recBBBTN.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4))

        #MESSAGE RETRIEVED
        self.ui.mesRecBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3))

######################################################################################################## REAL TIME
        
        #SIGNAL RECEIVED 
        #self.ui.SRBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_10))
      
        #DEP
        self.ui.DEPBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11))

        #CONSTELATION
        self.ui.ConstBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_9))

#########################################################################################################
        
        self.ui.stoprecBtn.clicked.connect(self.check_reception_state)

        
        ## SYMBOL DETECTION
###########################################################################################################
        
        #DEFINED THRESHOLD
        self.ui.UmbPreBtn.pressed.connect(self.defined_threshold)
        self.ui.simPBitBox.activated.connect(self.symbols_per_bit_DT)   
        
        #USER DEFINED THRESHOLD
        self.ui.UmbDisBtn.pressed.connect(self.user_defined_threshold)
        self.ui.simPBitBox_2.activated.connect(self.symbols_per_bit_UDT)

        self.ui.codelineBox_4.activated.connect(self.add_threshold_2_symbols)
        self.ui.codelineBox_3.activated.connect(self.add_threshold_4_symbols)  
        self.ui.codelineBox_2.activated.connect(self.add_threshold_4_symbols_2)       
   
        
        #RECEPTION
        self.ui.recepBtn.clicked.connect(self.reception_signal)

        #FBIT
        self.ui.fbit.valueChanged[str].connect(self.bit_frecuency)
        
        #TBIT
        self.ui.tbit.valueChanged[str].connect(self.bit_duration)
        
        self.ventana.show()
        
    def open_transmission1(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_transmission1()
        self.ui.setupUi(self.ventana)

        # opening window in maximized size 
        self.ventana.showMaximized()
        #self.ventana.setFixedHeight(820)
        
        self.filePath = ["", ""]
        self.fsample = 522000
        
        #FLAGS
        self.BB_graph_flag = False
        self.CS_graph_flag = False
        self.signal_graph_flag = False
        
        self.defined_const_flag = False
        self.user_defined_const_flag = False
        
        self.user_defined_const_complex_flag = False
        self.number_of_symbols_flag = False
        
        self.text_flag_message = True
        self.filepath_flag_message = False
        
        self.configured_signal = False
        self.setting_in_process = False
        
        #WINDOW ICON
        self.ventana.setWindowTitle("Digital Comunications Toolkit - Transmition Mode")
        
        # TOGGLE/MENU
        ########################################################################
        self.ui.menuBtn.clicked.connect(lambda: MainFunctions.toggleMenu(self, 180, True))
        
        #BUTTON ACTIONS
        ########################################################################
               
        #TRANSMISSION     
        self.ui.TranBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        #self.ui.TranBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
            
        #INFO            
        self.ui.InfoBtn.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))       
        #self.ui.InfoBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))

        #CLOSE     
        self.ui.closeMBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        self.ui.closeMBtn_2.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))

        #RECEPTION PAGE
        self.ui.RecepBtn.clicked.connect(self.open_reception)
        self.ui.RecepBtn.clicked.connect(self.close)
        
        #HOME PAGE
        self.ui.HomeBtn.clicked.connect(self.open_homepage)
        self.ui.HomeBtn.clicked.connect(self.close)
        
        #TRANSMISSION-ARCHIVE PAGE
        self.ui.fileBtn_2.clicked.connect(self.open_transmission2)
        self.ui.fileBtn_2.clicked.connect(self.close)
        
        
        #PREV BASE BAND
        self.ui.prevBBBTN.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4))
        
        #PREV BAND PASS
        self.ui.prevPBBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3))
        
        #PREV MODULATED SIGNAL
        self.ui.prevMSBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_10))
        
        #PREV DEP
        self.ui.prevDEPBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11))
        
        #PREV CONSTELATION
        self.ui.prevConstBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_9))
        
        #MODULATION
        #############################################################################################
        
        #TYPE OF MODULATION ACCORDING TO NUMBER OF SYMBOLS PER BIT
        self.ui.simPBitBox.activated.connect(self.type_of_modulation)
        
        #CHOOSE MODULATION - OPTIONS
        self.ui.modBox_3.activated.connect(self.eight_symbols_options)
        self.ui.modBox_4.activated.connect(self.sixteen_symbols_options)
        
        self.ui.UmbPreBtn.pressed.connect(self.defined_const)
        self.ui.simPBitBox.activated.connect(self.type_of_modulation)   
        

        self.ui.UmbDisBtn.pressed.connect(self.user_defined_const)
        self.ui.simPBitBox_2.activated.connect(self.user_defined_const_complex)
        
        
        #FBIT
        self.ui.fbit.valueChanged[str].connect(self.bit_frecuency)
        
        #TBIT
        self.ui.tbit.valueChanged[str].connect(self.bit_duration)
        
        
        #GRAPH PREV OF MODULATED SIGNAL
        self.ui.preSMBtn.clicked.connect(self.graph_modulated_signal_prev)
        
        
        
        #GRAPH CARRIER
        self.ui.preSPBtn.clicked.connect(self.graph_original_bits)
        
        
        #CONFIGURE TRANSMITION
        self.ui.ConfBtn.clicked.connect(self.configure_signal)
        
        #TRANSMIT
        self.ui.TransBtn.clicked.connect(self.transmit_signal_pluto)
        
            
        self.ventana.show()
        
    def open_transmission2(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_transmission2()
        self.ui.setupUi(self.ventana)

        # opening window in maximized size 
        self.ventana.showMaximized() 
        
        self.fsample = 522000
        
        #FLAGS
        self.BB_graph_flag = False
        self.CS_graph_flag = False
        self.signal_graph_flag = False
        
        
        self.number_of_symbols_flag = False
        self.defined_const_flag = False
        self.user_defined_const_flag = False
        
        self.user_defined_const_complex_flag = False
        
        self.text_flag_message = False
        self.filepath_flag_message = True
        
        self.configured_signal = False
        self.setting_in_process = False
        
        #WINDOW ICON
        self.ventana.setWindowTitle("Digital Comunications Toolkit - Transmition Mode")
        
        ## TOGGLE/MENU
        ########################################################################
        self.ui.menuBtn.clicked.connect(lambda: MainFunctions.toggleMenu(self, 180, True))
        
        #BUTTON ACTIONS  
        #############################################################################################        
        
        ###TRANSMISSION      
        self.ui.TranBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        #self.ui.TranBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
            
        ###INFO           
        self.ui.InfoBtn.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))       
        #self.ui.InfoBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))

        ###CLOSE     
        self.ui.closeMBtn.clicked.connect(lambda: MainFunctions.info(self, 255, True))
        self.ui.closeMBtn_2.clicked.connect(lambda: MainFunctions.info_2(self, 255, True))
        
        ###RECEPTION PAGE
        self.ui.RecepBtn.clicked.connect(self.open_reception)
        self.ui.RecepBtn.clicked.connect(self.close)
        
        ###TRANSMISSION-TEXT PAGE
        self.ui.textBtn_2.clicked.connect(self.open_transmission1)
        self.ui.textBtn_2.clicked.connect(self.close)
        
        ###HOME PAGE
        self.ui.HomeBtn.clicked.connect(self.open_homepage)
        self.ui.HomeBtn.clicked.connect(self.close)
        
        
        
        #CHOOSE ARCHIVE
        self.ui.ArchiveBtn.clicked.connect(self.getArchive)
        
        #PREV BASE BAND
        self.ui.prevBBBTN.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4))
        
        #PREV CARRIER
        self.ui.prevPBBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3))
        
        #PREV MODULATED SIGNAL
        self.ui.prevMSBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_10))
        
        #PREV DEP
        self.ui.prevDEPBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11))
        
        #PREV CONSTELATION
        self.ui.prevConstBtn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_9))
        
        
        
        #MODULATION
        #############################################################################################
        
        #TYPE OF MODULATION ACCORDING TO NUMBER OF SYMBOLS PER BIT
        self.ui.simPBitBox.activated.connect(self.type_of_modulation)
        
        #CHOOSE MODULATION - OPTIONS
        self.ui.modBox_3.activated.connect(self.eight_symbols_options)
        self.ui.modBox_4.activated.connect(self.sixteen_symbols_options)
        

        self.ui.UmbPreBtn.pressed.connect(self.defined_const)
        self.ui.simPBitBox.activated.connect(self.type_of_modulation)   
        
        self.ui.UmbDisBtn.pressed.connect(self.user_defined_const)
        self.ui.simPBitBox_2.activated.connect(self.user_defined_const_complex)
        
        
        #GRAPH PREV OF MODULATED SIGNAL
        self.ui.preSMBtn.clicked.connect(self.graph_modulated_signal_prev)
        
        #CONFIGURE TRANSMITION
        self.ui.ConfBtn.clicked.connect(self.configure_signal)        
        
        #TRANSMIT
        self.ui.TransBtn.clicked.connect(self.transmit_signal_pluto)
        
        
        #FBIT
        self.ui.fbit.valueChanged[str].connect(self.bit_frecuency)
        
        #TBIT
        self.ui.tbit.valueChanged[str].connect(self.bit_duration)
        
        #GRAPH CARRIER
        self.ui.preSPBtn.clicked.connect(self.graph_original_bits)
             
        self.ventana.show()

#######################################################################################################################################
#METHODS
####################################################################################################################################### 

    def recep_filter_signal(self):
        self.ui.stackedWidget_15.setCurrentWidget(self.ui.page_30)

        #self.grafica1.ax.cla()
        #self.grafica1.fig.clf()
        #self.grafica3.ax3.cla()
        #self.grafica3.fig3.clf()
        #self.grafica4.ax2.cla()
        #self.grafica4.fig2.clf()
        plt.close("all")

        for i in reversed(range(self.ui.DEPlayout.count())):
                
            widgetToRemove = self.ui.DEPlayout.itemAt(i).widget()
            self.ui.DEPlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #AwidgetToRemove0 = self.ui.DEPlayout.itemAt(0).widget()
        #AwidgetToRemove1 = self.ui.DEPlayout.itemAt(1).widget()
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove0)
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove1)
        #AwidgetToRemove0.deleteLater()
        #AwidgetToRemove1.deleteLater()
            
        for i in reversed(range(self.ui.Constlayout.count())):
                
            widgetToRemove = self.ui.Constlayout.itemAt(i).widget()
            self.ui.Constlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #BwidgetToRemove0 = self.ui.Constlayout.itemAt(0).widget()
        #BwidgetToRemove1 = self.ui.Constlayout.itemAt(1).widget()
        #self.ui.Constlayout.removeWidget(BwidgetToRemove0)
        #self.ui.Constlayout.removeWidget(BwidgetToRemove1)
        #BwidgetToRemove0.deleteLater()
        #BwidgetToRemove1.deleteLater()

        for i in reversed(range(self.ui.recBBlayout.count())):
                
            widgetToRemove = self.ui.recBBlayout.itemAt(i).widget()
            self.ui.recBBlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #CwidgetToRemove0 = self.ui.recBBlayout.itemAt(0).widget()
        #CwidgetToRemove1 = self.ui.recBBlayout.itemAt(1).widget()
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove0)
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove1)
        #CwidgetToRemove0.deleteLater()
        #CwidgetToRemove1.deleteLater()

        
        t = np.arange(len(self.graph_filtered)) / 522000

        self.grafica1 = plt_received_signal(self.graph_filtered, 522000) #PASA LAS VARIABLES PARA CONSTRUIR LA DEP DE LA SEÑAL RECIBIDA
        self.toolbar1 = NavigationToolbar(self.grafica1, self)

        self.grafica3 = plt_received_signal3(self.graph_filtered.real, self.graph_filtered.imag) #PASA LAS VARIABLES PARA CONSTRUIR LA CONSTELACIÓN DE LA SEÑAL RECIBIDA
        self.toolbar3 = NavigationToolbar(self.grafica3, self)
            
        self.grafica4 = plt_received_signal2(t, self.graph_filtered.real, t, self.graph_filtered.imag, plot_sync_time=self.symbols_indices_plot) #PASA LAS VARIABLES PARA CONSTRUIR LA SEÑAL ORIGINAL RECIBIDA
        self.toolbar4 = NavigationToolbar(self.grafica4, self)

        self.ui.DEPlayout.addWidget(self.grafica1)
        self.ui.DEPlayout.addWidget(self.toolbar1)
        self.ui.Constlayout.addWidget(self.grafica3)
        self.ui.Constlayout.addWidget(self.toolbar3)
        self.ui.recBBlayout.addWidget(self.grafica4)
        self.ui.recBBlayout.addWidget(self.toolbar4) 

        

    def recep_freq_fase_signal(self):      
        self.ui.stackedWidget_15.setCurrentWidget(self.ui.page_31)

        #self.grafica1.ax.cla()
        #self.grafica1.fig.clf()
        #self.grafica3.ax3.cla()
        #self.grafica3.fig3.clf()
        #self.grafica4.ax2.cla()
        #self.grafica4.fig2.clf()
        plt.close("all")

        for i in reversed(range(self.ui.DEPlayout.count())):
                
            widgetToRemove = self.ui.DEPlayout.itemAt(i).widget()
            self.ui.DEPlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #AwidgetToRemove0 = self.ui.DEPlayout.itemAt(0).widget()
        #AwidgetToRemove1 = self.ui.DEPlayout.itemAt(1).widget()
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove0)
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove1)
        #AwidgetToRemove0.deleteLater()
        #AwidgetToRemove1.deleteLater()
            
        for i in reversed(range(self.ui.Constlayout.count())):
                
            widgetToRemove = self.ui.Constlayout.itemAt(i).widget()
            self.ui.Constlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #BwidgetToRemove0 = self.ui.Constlayout.itemAt(0).widget()
        #BwidgetToRemove1 = self.ui.Constlayout.itemAt(1).widget()
        #self.ui.Constlayout.removeWidget(BwidgetToRemove0)
        #self.ui.Constlayout.removeWidget(BwidgetToRemove1)
        #BwidgetToRemove0.deleteLater()
        #BwidgetToRemove1.deleteLater()

        for i in reversed(range(self.ui.recBBlayout.count())):
                
            widgetToRemove = self.ui.recBBlayout.itemAt(i).widget()
            self.ui.recBBlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #CwidgetToRemove0 = self.ui.recBBlayout.itemAt(0).widget()
        #CwidgetToRemove1 = self.ui.recBBlayout.itemAt(1).widget()
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove0)
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove1)
        #CwidgetToRemove0.deleteLater()
        #CwidgetToRemove1.deleteLater()


        t = np.arange(len(self.graph_corrected)) / 522000

        self.grafica1 = plt_received_signal(self.graph_corrected, 522000) #PASA LAS VARIABLES PARA CONSTRUIR LA DEP DE LA SEÑAL RECIBIDA
        self.toolbar1 = NavigationToolbar(self.grafica1, self)

        self.grafica3 = plt_received_signal3(self.graph_corrected.real, self.graph_corrected.imag) #PASA LAS VARIABLES PARA CONSTRUIR LA CONSTELACIÓN DE LA SEÑAL RECIBIDA
        self.toolbar3 = NavigationToolbar(self.grafica3, self)
            
        self.grafica4 = plt_received_signal2(t, self.graph_corrected.real, t, self.graph_corrected.imag, plot_sync_time=self.symbols_indices_plot) #PASA LAS VARIABLES PARA CONSTRUIR LA SEÑAL ORIGINAL RECIBIDA
        self.toolbar4 = NavigationToolbar(self.grafica4, self)

        self.ui.DEPlayout.addWidget(self.grafica1)
        self.ui.DEPlayout.addWidget(self.toolbar1)
        self.ui.Constlayout.addWidget(self.grafica3)
        self.ui.Constlayout.addWidget(self.toolbar3)
        self.ui.recBBlayout.addWidget(self.grafica4)
        self.ui.recBBlayout.addWidget(self.toolbar4)

    def recep_time_sync_signal(self):
        self.ui.stackedWidget_15.setCurrentWidget(self.ui.page_35)

        #self.grafica1.ax.cla()
        #self.grafica1.fig.clf()
        #self.grafica3.ax3.cla()
        #self.grafica3.fig3.clf()
        #self.grafica4.ax2.cla()
        #self.grafica4.fig2.clf()
        plt.close("all")

        for i in reversed(range(self.ui.DEPlayout.count())):
                
            widgetToRemove = self.ui.DEPlayout.itemAt(i).widget()
            self.ui.DEPlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #AwidgetToRemove0 = self.ui.DEPlayout.itemAt(0).widget()
        #AwidgetToRemove1 = self.ui.DEPlayout.itemAt(1).widget()
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove0)
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove1)
        #AwidgetToRemove0.deleteLater()
        #AwidgetToRemove1.deleteLater()
            
        for i in reversed(range(self.ui.Constlayout.count())):
                
            widgetToRemove = self.ui.Constlayout.itemAt(i).widget()
            self.ui.Constlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #BwidgetToRemove0 = self.ui.Constlayout.itemAt(0).widget()
        #BwidgetToRemove1 = self.ui.Constlayout.itemAt(1).widget()
        #self.ui.Constlayout.removeWidget(BwidgetToRemove0)
        #self.ui.Constlayout.removeWidget(BwidgetToRemove1)
        #BwidgetToRemove0.deleteLater()
        #BwidgetToRemove1.deleteLater()

        for i in reversed(range(self.ui.recBBlayout.count())):
                
            widgetToRemove = self.ui.recBBlayout.itemAt(i).widget()
            self.ui.recBBlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #CwidgetToRemove0 = self.ui.recBBlayout.itemAt(0).widget()
        #CwidgetToRemove1 = self.ui.recBBlayout.itemAt(1).widget()
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove0)
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove1)
        #CwidgetToRemove0.deleteLater()
        #CwidgetToRemove1.deleteLater()


        t = np.arange(len(self.graph_sincro)) / 522000

        self.grafica1 = plt_received_signal(self.graph_sincro, 522000) #PASA LAS VARIABLES PARA CONSTRUIR LA DEP DE LA SEÑAL RECIBIDA
        self.toolbar1 = NavigationToolbar(self.grafica1, self)

        self.grafica3 = plt_received_signal3(self.graph_sincro.real, self.graph_sincro.imag, thresholds=self.thresholds_plot) #PASA LAS VARIABLES PARA CONSTRUIR LA CONSTELACIÓN DE LA SEÑAL RECIBIDA
        self.toolbar3 = NavigationToolbar(self.grafica3, self)
            
        self.grafica4 = plt_received_signal2(t, self.graph_sincro.real, t, self.graph_sincro.imag) #PASA LAS VARIABLES PARA CONSTRUIR LA SEÑAL ORIGINAL RECIBIDA
        self.toolbar4 = NavigationToolbar(self.grafica4, self)

        self.ui.DEPlayout.addWidget(self.grafica1)
        self.ui.DEPlayout.addWidget(self.toolbar1)
        self.ui.Constlayout.addWidget(self.grafica3)
        self.ui.Constlayout.addWidget(self.toolbar3)
        self.ui.recBBlayout.addWidget(self.grafica4)
        self.ui.recBBlayout.addWidget(self.toolbar4)

    def recep_error_correc_signal(self):
        self.ui.stackedWidget_15.setCurrentWidget(self.ui.page_36)
        self.ui.stackedWidget_22.setCurrentWidget(self.ui.page_28)
        self.ui.stackedWidget_25.setCurrentWidget(self.ui.page_37)
        n_format = self.ui.formatBox.currentIndex()
        self.graphics_final_fase = True

        #self.grafica1.ax.cla()
        #self.grafica1.fig.clf()
        #self.grafica3.ax3.cla()
        #self.grafica3.fig3.clf()
        #self.grafica4.ax2.cla()
        #self.grafica4.fig2.clf()
        plt.close("all")

        for i in reversed(range(self.ui.DEPlayout.count())):
                
            widgetToRemove = self.ui.DEPlayout.itemAt(i).widget()
            self.ui.DEPlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #AwidgetToRemove0 = self.ui.DEPlayout.itemAt(0).widget()
        #AwidgetToRemove1 = self.ui.DEPlayout.itemAt(1).widget()
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove0)
        #self.ui.DEPlayout.removeWidget(AwidgetToRemove1)
        #AwidgetToRemove0.deleteLater()
        #AwidgetToRemove1.deleteLater()
            
        for i in reversed(range(self.ui.Constlayout.count())):
                
            widgetToRemove = self.ui.Constlayout.itemAt(i).widget()
            self.ui.Constlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #BwidgetToRemove0 = self.ui.Constlayout.itemAt(0).widget()
        #BwidgetToRemove1 = self.ui.Constlayout.itemAt(1).widget()
        #self.ui.Constlayout.removeWidget(BwidgetToRemove0)
        #self.ui.Constlayout.removeWidget(BwidgetToRemove1)
        #BwidgetToRemove0.deleteLater()
        #BwidgetToRemove1.deleteLater()

        for i in reversed(range(self.ui.recBBlayout.count())):
                
            widgetToRemove = self.ui.recBBlayout.itemAt(i).widget()
            self.ui.recBBlayout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

        #CwidgetToRemove0 = self.ui.recBBlayout.itemAt(0).widget()
        #CwidgetToRemove1 = self.ui.recBBlayout.itemAt(1).widget()
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove0)
        #self.ui.recBBlayout.removeWidget(CwidgetToRemove1)
        #CwidgetToRemove0.deleteLater()
        #CwidgetToRemove1.deleteLater()


        MainFunctions.graph_original_bits_reception(self)

        self.ui.finalInfo_2.setText("A continuación se presenta información relacionada de la señal recibida:" + "\n\n" + 
                                    "Cantidad total de bits recibidos: " + self.cantidad_bits + "\n\n" +
                                    "Cantidad total de simbolos recibidos: " + self.cantidad_simbolos  + "\n\n" +
                                    "SER (Signal Error rate): " + str(self.ser) + "\n\n" +
                                    "Número de simbolos con posible error: " + str(self.num_errors) + "\n\n" +
                                    "Número de muestras por simbolo: " + str(self.sps))

        t = np.arange(len(self.graph_sincro_corrected)) / 522000

        self.grafica1 = plt_received_signal(self.graph_sincro_corrected, 522000) #PASA LAS VARIABLES PARA CONSTRUIR LA DEP DE LA SEÑAL RECIBIDA
        self.toolbar1 = NavigationToolbar(self.grafica1, self)

        self.grafica3 = plt_received_signal3(self.graph_sincro_corrected.real, self.graph_sincro_corrected.imag, thresholds=self.thresholds_plot) #PASA LAS VARIABLES PARA CONSTRUIR LA CONSTELACIÓN DE LA SEÑAL RECIBIDA
        self.toolbar3 = NavigationToolbar(self.grafica3, self)
            
        self.grafica4 = plt_received_signal2(t, self.graph_sincro_corrected.real, t, self.graph_sincro_corrected.imag) #PASA LAS VARIABLES PARA CONSTRUIR LA SEÑAL ORIGINAL RECIBIDA
        self.toolbar4 = NavigationToolbar(self.grafica4, self)

        self.ui.DEPlayout.addWidget(self.grafica1)
        self.ui.DEPlayout.addWidget(self.toolbar1)
        self.ui.Constlayout.addWidget(self.grafica3)
        self.ui.Constlayout.addWidget(self.toolbar3)
        self.ui.SRlayout.addWidget(self.grafica4)
        self.ui.SRlayout.addWidget(self.toolbar4)


        if n_format == 1:
            self.ui.label_40.setText(self.string_resultado)

        elif n_format == 2 or n_format == 3:
            try:
                pixmap = QPixmap("imagen_recibida5.jpg")
                self.ui.label_40.setPixmap(pixmap)
                print("Imagen en interfaz")
            except Exception as e:
                self.ui.label_40.setText("Algo ha salido mal...")
                print("NO imagen en interfaz")
            

        elif n_format > 3:
            pass
            
        gc.collect() #Verificar si esto afecta negativamente. Se llama al Garbage Collector al final de que se tenga en pantalla toda la info final de la señal
        del self.muestras #Borra el arreglo de muestras completas recibidas


    def check_reception_state(self):
        self.ui.recepBtn.setEnabled(True)
        if self.reception_configured == False:
            self.ui.simWarnTxt.setText("Debe primero inicializar el estado de recepción")
            

    def configure_signal(self):
        
        fsim = self.ui.fbit.value()
        tsim = self.ui.tbit.value()
        fport = self.ui.fport.value()
        fsample = self.fsample
        flag = self.configured_signal

        self.threadpool = QThreadPool()
        worker = Worker_config_signal(flag, fsample, tsim, fport, fsim)
        worker.signals.finished.connect(self.configure_signal_action)

        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.threadpool.start(worker)
        self.ui.ConfBtn.setEnabled(False)

        #self.ui.ConfigSig.setText("")

    def configure_signal_action(self, flag, sdr):

        self.sdr = sdr
        fsim = self.ui.fbit.value()
        tsim = self.ui.tbit.value()
        fport = self.ui.fport.value()
        fsample = self.fsample

        if flag == True:
            MainWindow.transmit_signal(self, fsample, tsim, fport, fsim)

            MainFunctions.transmit_motion_btn(self, 30, True) #Muestra boton de Transmitir señal luego de haberla configurado por completo

            print("Configuración PLUTO y Señal listas")
            self.ui.simWarnTxt.setText("Configuración PLUTO y Señal listas")

        else:
            self.ui.simWarnTxt.setText("Hace falta conectar el módulo ADALM - PLUTO")
            self.ui.ConfBtn.setEnabled(True)

        
    
    def graph_received_result(self):
        t = np.arange(0,len(self.muestras))
        plt.cla()
        plt.plot(self.muestras.real,self.muestras.imag,"*")
        plt.show()
        
        print(len(self.muestras))

    
    def reception_signal(self):
        message_format = self.ui.formatBox.currentIndex()
        self.muestras = np.array([])
        self.ui.recepBtn.setEnabled(False)

        self.graphWidget = pg.PlotWidget(background="w")
        self.graphWidget_3 = pg.PlotWidget(background="w")
        self.graphWidget_4 = pg.PlotWidget(background="w")

        if self.reception_configured == True:
            self.reception_configured = False
            self.ui.stackedWidget_15.setCurrentWidget(self.ui.page_39)
            self.ui.stackedWidget_22.setCurrentWidget(self.ui.page_27)
            self.ui.stackedWidget_25.setCurrentWidget(self.ui.page_38)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)


        fsample = self.fsample
        frequency_carrier = self.ui.fport.value()
        tsim = self.ui.tbit.value()
        gain_rx = self.ui.gananRx.value()
        buffer = 30000
        

        if message_format == 0:
            self.ui.simWarnTxt.setText("Hace falta definir el formato del mensaje")
            self.ui.recepBtn.setEnabled(True)

        elif self.ui.UmbPreBtn.isChecked() == False and self.ui.UmbDisBtn.isChecked() == False:
            self.ui.simWarnTxt.setText("Hace falta definir el modo de trabajo del receptor")
            self.ui.recepBtn.setEnabled(True)

        ######## UMBRALES PREDEFINIDOS
        elif self.ui.UmbPreBtn.isChecked() == True:
            print("Entró condicional inicio recepcion")
            n_symbol_index = self.ui.simPBitBox.currentIndex()
            print("n_symbol_index es:", n_symbol_index)    

            if n_symbol_index == 0:
                self.ui.simWarnTxt.setText("Hace falta definir la cantidad de bits codificados por simbolo")
                self.ui.recepBtn.setEnabled(True)            
            
            elif n_symbol_index == 1:
                threshold_index = self.ui.geoBox_1.currentIndex()

                if threshold_index == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir la geometría del umbral")
                    self.ui.recepBtn.setEnabled(True)    

                elif threshold_index != 0:
                    print("Entro segundo condicional")
                    n_symbol = 2
                    esquema = threshold_index
                    print("Esquema para umbrales es:", esquema)
                    #Esquema = 1 - Recta inclinada - FSK probablemente
                    #Esquema = 2 - Recta paralela eje X - BPSK con simbolos arriba y abajo
                    #Esquema = 3 - Recta paralela eje Y - BPSK normal
                    #Esquema = 4 - Recta eje Y=1.5 - ASK normal
                    #Esquema = 5 - Recta eje Y=0.5 - OOK normal, probablemente no se use
                    
                    if esquema == 1: #Umbrales 2ASK
                        esquema = "2ASK"
                        
                    if threshold_index == 1:
                        threshold_index = 1 #En este caso se acomodo en threshold_defined, regiones es 4 para 2ask

                    MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)

                    if self.reception_configured == True:

                        thresholds = MainFunctions.threshold_defined(self, n_symbol, threshold_index)
                        self.thresholds_plot = thresholds
                        print("Umbrales definidos listos")
                        regions, bits_save = MainFunctions.define_regions(self, n_symbol, threshold_index)
                        print("Regiones definidas listas")
                        thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                        print("Umbrales interpolados listos")
                        print("2- UMBRALES Y REGIONES CONFIGURADOS")
                        print("3. RECIBIENDO...")
                        MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)
                    
            elif n_symbol_index == 2:
                threshold_index = self.ui.geoBox_2.currentIndex()

                if threshold_index == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir la geometría del umbral")
                    self.ui.recepBtn.setEnabled(True)   

                elif threshold_index != 0:
                    n_symbol = 4
                    esquema = threshold_index
                    print("Esquema para umbrales es:", esquema)
                    #Esquema = 3 - Rectas diagonales - QPSK en ejes
                    #Esquema = 2 - Rectas paralelas ejes - QPSK normal
                    #Esquema = 1 - Rectas verticales - 4ASK normal

                    MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)
                    
                    if self.reception_configured == True:
                        thresholds = MainFunctions.threshold_defined(self, n_symbol, threshold_index)
                        self.thresholds_plot = thresholds
                        print("Umbrales definidos listos")
                        regions, bits_save = MainFunctions.define_regions(self, n_symbol, threshold_index)
                        print("Regiones definidas listas")
                        thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                        print("Umbrales interpolados listos")
                        print("2- UMBRALES Y REGIONES CONFIGURADOS")
                        print("3. RECIBIENDO...")
                        MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)                
                        
                    
            elif n_symbol_index == 3:
                threshold_index = self.ui.geoBox_3.currentIndex()

                if threshold_index == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir la geometría del umbral")
                    self.ui.recepBtn.setEnabled(True)   

                elif threshold_index != 0:
                    n_symbol = 8
                    esquema = threshold_index
                    #EsquemaTX = 3,C - Dos rectas en los ejes y 1 circulo - 8QAM Diagonal - Esquema 3,3 en constelación - Index 1 en interfazRX
                    #EsquemaTX = 1 - 6 Verticales - 8ASK Bipolar - Esquema 1 en constelación - Index 4 en interfaz RX
                    #EsquemaTX = 2 - 4 Diagonales - 8PSK - Esquema 2 en constelación - Index 2 en interfaz RX
                    #EsquemaTX = 3,A - 3 Verticales una Horizonal - 8QAM rectangular - Esquema 3,1 en constelación - Index 3 en interfaz RX
                    
                    if esquema == 1: #Se configuran los distintos esquemas para 8 símbolos, pues estos usan esquemas distintos y otro adicional
                        esquema = "8QAM-DIAGONAL"
                    elif esquema == 3:
                        esquema = "8QAM-RECTANGULAR"
                    elif esquema == 4:
                        esquema = "8ASK-BIPOLAR"
                    print("Esquema para umbrales es:", esquema)
                    #Para el 8QAM-CIRCULAR se usan mismos umbrales que 8PSK
                    
                    #Esquemas para definir umbrales con threshold_defined:
                    # 1 - 2 Rectas Ejes 1 Circulo
                    # 2 - 4 Diagonales - 8PSK & 8QAM-CIRCULAR
                    # 3 - 3 Horizontales 1 Vertical
                    # 4 - 3 Verticales 1 Horizontal - 8QAM-RECTANGULAR
                    # 5 - 7 Verticales - 8ASK Bipolar
                    #Estos esquemas coinciden para los umbrales y regiones
                    
                    if threshold_index == 1:
                        threshold_index = 1
                    elif threshold_index == 2: #Recordar acomodar regiones y bits_save para 8QAM-CIRCULAR para que coincidan con las de 8PSK 
                        threshold_index = 2
                    elif threshold_index == 3: #Este umbral es para 8QAM-RECTANGULAR, que en threshold_defined es el esquema 4
                        threshold_index = 4
                    elif threshold_index == 4: #Este umbral es para 8ASK BIPOLAR, que en threshold_defined es el esquema 5
                        threshold_index = 5
                    
                    MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)

                    if self.reception_configured == True:
                        thresholds = MainFunctions.threshold_defined(self, n_symbol, threshold_index)
                        self.thresholds_plot = thresholds
                        print("Umbrales definidos listos")
                        regions, bits_save = MainFunctions.define_regions(self, n_symbol, threshold_index)
                        print("Regiones definidas listas")
                        thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                        print("Umbrales interpolados listos")
                        print("2- UMBRALES Y REGIONES CONFIGURADOS")
                        print("3. RECIBIENDO...")
                        MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)                

                
            elif n_symbol_index == 4:
                threshold_index = self.ui.geoBox_4.currentIndex()

                if threshold_index == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir la geometría del umbral")
                    self.ui.recepBtn.setEnabled(True)    

                elif threshold_index != 0:
                    n_symbol = 16
                    esquema = threshold_index
                    #Esquema = 1 - 8 Diagonales - PSK
                    #Para los QAM se utilizo otro valor de esquema ademas del threshold index para la constelación, arreglar para estos casos
                    
                    if esquema == 2: #Se configuran los distintos esquemas para 16 símbolos, pues estos usan esquemas distintos y otro adicional
                        esquema = "16QAM-CIRCULAR"
                    elif esquema == 3:
                        esquema = "16QAM-DIAGONAL"
                    elif esquema == 4:
                        esquema = "16QAM-RECTANGULAR"
                    print("Esquema para umbrales es:", esquema)
                    
                    MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)

                    if self.reception_configured == True:
                        self.ui.stackedWidget_15.setCurrentWidget(self.ui.page_39)
                        self.ui.stackedWidget_22.setCurrentWidget(self.ui.page_27)
                        self.ui.stackedWidget_25.setCurrentWidget(self.ui.page_38)

                        thresholds = MainFunctions.threshold_defined(self, n_symbol, threshold_index)
                        self.thresholds_plot = thresholds
                        print("Umbrales definidos listos")
                        regions, bits_save = MainFunctions.define_regions(self, n_symbol, threshold_index)
                        print("Regiones definidas listas")
                        thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                        print("Umbrales interpolados listos")
                        print("2- UMBRALES Y REGIONES CONFIGURADOS")
                        print("3. RECIBIENDO...")
                        MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)                    
                    
                    

                
                
        ######## UMBRALES DEFINIDOS POR EL USUARIO
 
        elif self.ui.UmbDisBtn.isChecked() == True:
            n_symbol_index = self.ui.simPBitBox_2.currentIndex()

            if n_symbol_index == 0:
                self.ui.simWarnTxt.setText("Hace falta definir la cantidad de bits codificados por simbolo")
                self.ui.recepBtn.setEnabled(True)  
            
            elif n_symbol_index == 1: #Dos simbolos
                n_symbol = 2
                geo_threshold_index = self.ui.codelineBox_4.currentIndex()

                if geo_threshold_index == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir la geometría del umbral")
                    self.ui.recepBtn.setEnabled(True)

                
                elif geo_threshold_index == 1: #Linea vertical x=a
                    x = self.ui.doubleSpinBox_12.value()
                    symbol1 = self.ui.text_3.toPlainText() #Simbolo 1
                    symbol2 = self.ui.text_4.toPlainText() #Simbolo 2

                    if symbol1 == "" or symbol2 == "":
                        self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                        self.ui.recepBtn.setEnabled(True)

                    elif symbol1 != "" and symbol2 != "":
                        try:
                            MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)
                            point1 = complex(symbol1) #Cuidado con los eval
                            point2 = complex(symbol2)
                            esquema = 'CUSTOM'
                            print("Puntos ingresados")
                            thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="vertical", selector2="vertical", offset_x=x, offset_y=0, angle=0, offset_x2=0, offset_y2=0, angle2=0)
                            self.thresholds_plot = thresholds
                            print("umbrales custom creados")
                            thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                            print("umbrales custom interpolados")
                            self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2)
                            print("constelacion custom creada")
                            regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                            print("regiones custom creadas")
                            print(regions)
                            
                            MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)

                        except Exception as e:
                            print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                            print(e)
                            self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                            self.ui.recepBtn.setEnabled(True)
                    
                    
                elif geo_threshold_index == 2: #Linea vertical x=-a
                    x = self.ui.doubleSpinBox_14.value()
                    symbol1 = self.ui.text_3.toPlainText() #Simbolo 1
                    symbol2 = self.ui.text_4.toPlainText() #Simbolo 2

                    if symbol1 == "" or symbol2 == "":
                        self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                        self.ui.recepBtn.setEnabled(True)

                    elif symbol1 != "" and symbol2 != "":
                        try:
                            MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)
                            point1 = complex(symbol1) #Cuidado con los eval
                            point2 = complex(symbol2)
                            esquema = 'CUSTOM'
                            print("Puntos ingresados")
                            thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="vertical", selector2="vertical", offset_x=x, offset_y=0, angle=0, offset_x2=0, offset_y2=0, angle2=0)
                            self.thresholds_plot = thresholds
                            print("umbrales custom creados")
                            thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                            print("umbrales custom interpolados")
                            self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2)
                            print("constelacion custom creada")
                            regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                            print("regiones custom creadas")
                            print(regions)
                            
                            MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)                            

                        except Exception as e:
                            print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                            print(e)
                            self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                            self.ui.recepBtn.setEnabled(True)

                    
                    
                elif geo_threshold_index == 3: #Linea horizontal y=b
                    y = self.ui.doubleSpinBox_16.value()
                    symbol1 = self.ui.text_3.toPlainText() #Simbolo 1
                    symbol2 = self.ui.text_4.toPlainText() #Simbolo 2

                    if symbol1 == "" or symbol2 == "":
                        self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                        self.ui.recepBtn.setEnabled(True)

                    elif symbol1 != "" and symbol2 != "":
                        try:
                            point1 = complex(symbol1) #Cuidado con los eval
                            point2 = complex(symbol2)
                            print("Puntos ingresados")
                            esquema = 'CUSTOM'
                            thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="horizontal", selector2="horizontal", offset_x=0, offset_y=y, angle=0, offset_x2=0, offset_y2=0, angle2=0)
                            self.thresholds_plot = thresholds
                            print("umbrales custom creados")
                            thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                            print("umbrales custom interpolados")
                            self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2)
                            print("constelacion custom creada")
                            regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                            print("regiones custom creadas")
                            print(regions)
                            
                            MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)                              

                        except Exception as e:
                            print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                            print(e)
                            self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                            self.ui.recepBtn.setEnabled(True)

                    
                    
                elif geo_threshold_index == 4: #Linea Horizontal y=-b
                    y = self.ui.doubleSpinBox_18.value()
                    symbol1 = self.ui.text_3.toPlainText() #Simbolo 1
                    symbol2 = self.ui.text_4.toPlainText() #Simbolo 2

                    if symbol1 == "" or symbol2 == "":
                        self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                        self.ui.recepBtn.setEnabled(True)

                    elif symbol1 != "" and symbol2 != "":
                        try:
                            point1 = complex(symbol1) #Cuidado con los eval
                            point2 = complex(symbol2)
                            esquema = 'CUSTOM'
                            print("Puntos ingresados")
                            thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="horizontal", selector2="vertical", offset_x=0, offset_y=y, angle=0, offset_x2=0, offset_y2=0, angle2=0)
                            self.thresholds_plot = thresholds
                            print("umbrales custom creados")
                            thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                            print("umbrales custom interpolados")
                            self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2)
                            print("constelacion custom creada")
                            regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                            print("regiones custom creadas")
                            print(regions)
                            
                            MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)  

                        except Exception as e:
                            print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                            print(e)
                            self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                            self.ui.recepBtn.setEnabled(True)
                    
                    
                elif geo_threshold_index == 5: #Linea inclinada
                    ang = self.ui.doubleSpinBox_20.value()
                    offx = self.ui.doubleSpinBox_21.value()
                    offy = self.ui.doubleSpinBox_22.value()
                    symbol1 = self.ui.text_3.toPlainText() #Simbolo 1
                    symbol2 = self.ui.text_4.toPlainText() #Simbolo 2

                    if symbol1 == "" or symbol2 == "":
                        self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                        self.ui.recepBtn.setEnabled(True)

                    elif symbol1 != "" and symbol2 != "":
                        try:
                            point1 = complex(symbol1) #Cuidado con los eval
                            point2 = complex(symbol2)
                            esquema = 'CUSTOM'
                            print("Puntos ingresados")
                            thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="inclinada", selector2="vertical", offset_x=offx, offset_y=offy, angle=ang, offset_x2=0, offset_y2=0, angle2=0)
                            self.thresholds_plot = thresholds
                            print("umbrales custom creados")
                            thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                            print("umbrales custom interpolados")
                            self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2)
                            print("constelacion custom creada")
                            regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                            print("regiones custom creadas")
                            print(regions)
                            
                            MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)  

                        except Exception as e:
                            print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                            print(e)
                            self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                            self.ui.recepBtn.setEnabled(True)
                    
                                 
                
            elif n_symbol_index == 2:
                geo_threshold_index2 = self.ui.codelineBox_2.currentIndex()
                geo_threshold_index3 = self.ui.codelineBox_3.currentIndex()
                n_symbol = 4

                if geo_threshold_index2 == 0 or geo_threshold_index3 == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir la geometría de uno de los umbrales")
                    self.ui.recepBtn.setEnabled(True)

                elif geo_threshold_index2 != 0 or geo_threshold_index3 != 0:

                    if geo_threshold_index3 == 1: #Primer umbral linea vertical x=a
                        x = self.ui.doubleSpinBox_12.value()
                        print("umbral 1 es: ", x)

                        if geo_threshold_index2 == 1: #linea vertical x=a y linea vertical x=a
                            x2 = self.ui.doubleSpinBox.value()
                            symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                            symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                            symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                            symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4

                            if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                                self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                                self.ui.recepBtn.setEnabled(True)

                            elif symbol1 != "" and symbol2 != "" and symbol3 != "" and symbol4 != "":
                                try:
                                    point1 = complex(symbol1) 
                                    point2 = complex(symbol2)
                                    point3 = complex(symbol3)
                                    point4 = complex(symbol4)
                                    esquema = 'CUSTOM'
                                    print("Puntos ingresados")
                                    thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="vertical", selector2="vertical", offset_x=x, offset_y=0, angle=0, offset_x2=x2, offset_y2=0, angle2=0)
                                    self.thresholds_plot = thresholds
                                    print("umbrales custom creados")
                                    thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                    print("umbrales custom interpolados")
                                    self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                    print("constelacion custom creada")
                                    regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                    print("regiones custom creadas")
                                    print(regions)
                            
                                    MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)

                                except Exception as e:
                                    print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                    print(e)
                                    self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                    self.ui.recepBtn.setEnabled(True)
                                
                                
                        elif geo_threshold_index2 == 2: #linea vertical x=a y linea vertical x=-a
                            x2 = self.ui.doubleSpinBox_4.value()
                            print("umbral 2 es: ", x2)
                            symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                            symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                            symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                            symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4

                            if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                                self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                                self.ui.recepBtn.setEnabled(True)

                            elif symbol1 != "" and symbol2 != "" and symbol3 != "" and symbol4 != "":
                                try:
                                    point1 = complex(symbol1) 
                                    point2 = complex(symbol2)
                                    point3 = complex(symbol3)
                                    point4 = complex(symbol4)
                                    esquema = 'CUSTOM'
                                    print("Puntos ingresados")
                                    thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="vertical", selector2="vertical", offset_x=x, offset_y=0, angle=0, offset_x2=x2, offset_y2=0, angle2=0)
                                    self.thresholds_plot = thresholds
                                    print("umbrales custom creados")
                                    thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                    print("umbrales custom interpolados")
                                    self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                    print("constelacion custom creada")
                                    regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                    print("regiones custom creadas")
                                    print(regions)
                            
                                    MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)
                                    
                                except Exception as e:
                                    print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                    print(e)
                                    self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                    self.ui.recepBtn.setEnabled(True)
                                
                                
                        elif geo_threshold_index2 == 3: #linea vertical x=a y linea horizontal y=b
                            y2 = self.ui.doubleSpinBox_6.value()
                            symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                            symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                            symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                            symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4

                            if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                                self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                                self.ui.recepBtn.setEnabled(True)

                            elif symbol1 != "" and symbol2 != "" and symbol3 != "" and symbol4 != "":
                                try:
                                    point1 = complex(symbol1) 
                                    point2 = complex(symbol2)
                                    point3 = complex(symbol3)
                                    point4 = complex(symbol4)
                                    esquema = 'CUSTOM'
                                    print("Puntos ingresados")
                                    thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="vertical", selector2="horizontal", offset_x=x, offset_y=0, angle=0, offset_x2=0, offset_y2=y2, angle2=0)
                                    self.thresholds_plot = thresholds
                                    print("umbrales custom creados")
                                    thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                    print("umbrales custom interpolados")
                                    self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                    print("constelacion custom creada")
                                    regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                    print("regiones custom creadas")
                                    print(regions)
                            
                                    MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)                                    

                                except:
                                    print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                    self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                    self.ui.recepBtn.setEnabled(True)
                                
                                
                        elif geo_threshold_index2 == 4: #linea vertical x=a y linea horizontal y=-b
                            y2 = self.ui.doubleSpinBox_8.value()
                            symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                            symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                            symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                            symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4

                            if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                                self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                                self.ui.recepBtn.setEnabled(True)

                            elif symbol1 != "" and symbol2 != "" and symbol3 != "" and symbol4 != "":
                                try:
                                    point1 = complex(symbol1) 
                                    point2 = complex(symbol2)
                                    point3 = complex(symbol3)
                                    point4 = complex(symbol4)
                                    esquema = 'CUSTOM'
                                    print("Puntos ingresados")
                                    thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="vertical", selector2="horizontal", offset_x=x, offset_y=0, angle=0, offset_x2=0, offset_y2=y2, angle2=0)
                                    self.thresholds_plot = thresholds
                                    print("umbrales custom creados")
                                    thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                    print("umbrales custom interpolados")
                                    self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                    print("constelacion custom creada")
                                    regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                    print("regiones custom creadas")
                                    print(regions)
                            
                                    MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)                                    

                                except Exception as e:
                                    print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                    print(e)
                                    self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                    self.ui.recepBtn.setEnabled(True)
                                
                                
                        elif geo_threshold_index2 == 5: #linea vertical x=a y linea inclinada
                            ang2 = self.ui.doubleSpinBox_10.value()
                            offx2 = self.ui.doubleSpinBox_11.value()
                            offy2 = self.ui.doubleSpinBox_9.value()
                            symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                            symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                            symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                            symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4

                            if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                                self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                                self.ui.recepBtn.setEnabled(True)

                            elif symbol1 != "" and symbol2 != "" and symbol3 != "" and symbol4 != "":
                                try:
                                    point1 = complex(symbol1) 
                                    point2 = complex(symbol2)
                                    point3 = complex(symbol3)
                                    point4 = complex(symbol4)
                                    esquema = 'CUSTOM'
                                    print("Puntos ingresados")
                                    thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1="vertical", selector2="inclinada", offset_x=x, offset_y=0, angle=0, offset_x2=offx2, offset_y2=offy2, angle2=ang2)
                                    self.thresholds_plot = thresholds
                                    print("umbrales custom creados")
                                    thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                    print("umbrales custom interpolados")
                                    self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                    print("constelacion custom creada")
                                    regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                    print("regiones custom creadas")
                                    print(regions)
                            
                                    MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)
                                    
                                except Exception as e:
                                    print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                    print(e)
                                    self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                    self.ui.recepBtn.setEnabled(True)
                                    

                    elif geo_threshold_index3 == 2: #primer umbral Linea vertical x=-a
                        x = self.ui.doubleSpinBox_14.value()
                        symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                        symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                        symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                        symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4
                        selector1 = "vertical"
                        
                        if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                            self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                            self.ui.recepBtn.setEnabled(True)
                            
                        else:
                        
                            if geo_threshold_index2 == 1: #linea vertical x=-a con vertical x=a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 2: #linea vertical x=-a con vertical x=-a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox_4.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 3: #linea vertical x=-a con horizontal y=b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_6.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 4: #linea vertical x=-a con horizontal y=-b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_8.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 5: #linea vertical x=-a con inclinada
                                selector2 = "inclinada"
                                offx2 = self.ui.doubleSpinBox_11.value()
                                offy2 = self.ui.doubleSpinBox_9.value()
                                ang2 = self.ui.doubleSpinBox_10.value()
                        
                            try:
                                point1 = complex(symbol1) 
                                point2 = complex(symbol2)
                                point3 = complex(symbol3)
                                point4 = complex(symbol4)
                                esquema = 'CUSTOM'
                                print("Puntos ingresados")
                                MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)
                                thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1=selector1, selector2=selector2, offset_x=x, offset_y=0, angle=0, offset_x2=offx2, offset_y2=offy2, angle2=ang2)
                                self.thresholds_plot = thresholds
                                print("umbrales custom creados")
                                print("offx2, offy2, ang2: {}, {}, {}".format(offx2,offy2,ang2))
                                thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                print("umbrales custom interpolados")
                                self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                print("constelacion custom creada")
                                regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                print("regiones custom creadas")
                                print(regions)
                            
                                MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)
                            
                            except Exception as e:
                                print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                print(e)
                                self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                self.ui.recepBtn.setEnabled(True)                               
                            
                            
                        

                    elif geo_threshold_index3 == 3: #Primer umbral linea horizontal y=b
                        y = self.ui.doubleSpinBox_16.value()
                        symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                        symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                        symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                        symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4
                        selector1 = "horizontal"
                        
                        if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                            self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                            self.ui.recepBtn.setEnabled(True)
                            
                        else:
                        
                            if geo_threshold_index2 == 1: #linea horizontal y=b con vertical x=a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 2: #linea horizontal y=b con vertical x=-a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox_4.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 3: #linea horizontal y=b con horizontal y=b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_6.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 4: #linea horizontal y=b con horizontal y=-b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_8.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 5: #linea horizontal y=b con inclinada
                                selector2 = "inclinada"
                                offx2 = self.ui.doubleSpinBox_11.value()
                                offy2 = self.ui.doubleSpinBox_9.value()
                                ang2 = self.ui.doubleSpinBox_10.value()
                        
                            try:
                                point1 = complex(symbol1) 
                                point2 = complex(symbol2)
                                point3 = complex(symbol3)
                                point4 = complex(symbol4)
                                esquema = 'CUSTOM'
                                print("Puntos ingresados")
                                MainFunctions.configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer)
                                thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1=selector1, selector2=selector2, offset_x=0, offset_y=y, angle=0, offset_x2=offx2, offset_y2=offy2, angle2=ang2)
                                self.thresholds_plot = thresholds
                                print("umbrales custom creados")
                                print("offx2, offy2, ang2: {}, {}, {}".format(offx2,offy2,ang2))
                                print("umbrales:",thresholds)
                                print("umbrales[0]",thresholds[0])
                                print("umbrales[1]",thresholds[1])
                                thresholds = np.array([thresholds[0][0], thresholds[1][0]])
                                print("umbrales modificado:",thresholds)
                                thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                print("umbrales custom interpolados")
                                self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                print("constelacion custom creada")
                                regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                print("regiones custom creadas")
                                print(regions)
                            
                                MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)
                            
                            except Exception as e:
                                print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                print(e)
                                self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                self.ui.recepBtn.setEnabled(True)                                
                                

                    elif geo_threshold_index3 == 4: #Primer umbral horizontal y=-b
                        y = self.ui.doubleSpinBox_18.value()
                        symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                        symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                        symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                        symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4
                        selector1 = "horizontal"
                        
                        if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                            self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                            self.ui.recepBtn.setEnabled(True)
                            
                        else:
                        
                            if geo_threshold_index2 == 1: #linea horizontal y=-b con vertical x=a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 2: #linea horizontal y=-b con vertical x=-a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox_4.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 3: #linea horizontal y=-b con horizontal y=b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_6.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 4: #linea horizontal y=-b con horizontal y=-b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_8.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 5: #linea horizontal y=-b con inclinada
                                selector2 = "inclinada"
                                offx2 = self.ui.doubleSpinBox_11.value()
                                offy2 = self.ui.doubleSpinBox_9.value()
                                ang2 = self.ui.doubleSpinBox_10.value()
                        
                            try:
                                point1 = complex(symbol1) 
                                point2 = complex(symbol2)
                                point3 = complex(symbol3)
                                point4 = complex(symbol4)
                                esquema = 'CUSTOM'
                                print("Puntos ingresados")
                                thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1=selector1, selector2=selector2, offset_x=0, offset_y=y, angle=0, offset_x2=offx2, offset_y2=offy2, angle2=ang2)
                                self.thresholds_plot = thresholds
                                print("umbrales custom creados")
                                print("offx2, offy2, ang2: {}, {}, {}".format(offx2,offy2,ang2))
                                thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                print("umbrales custom interpolados")
                                self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                print("constelacion custom creada")
                                regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                print("regiones custom creadas")
                                print(regions)
                            
                                MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)
                            
                            except Exception as e:
                                print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                print(e)
                                self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                self.ui.recepBtn.setEnabled(True)

                    elif geo_threshold_index3 == 5: #Primer umbral linea inclinada
                        ang = self.ui.doubleSpinBox_20.value()
                        offx = self.ui.doubleSpinBox_21.value()
                        offy = self.ui.doubleSpinBox_22.value()
                        symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                        symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                        symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                        symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4
                        selector1 = "inclinada"
                        
                        if symbol1 == "" or symbol2 == "" or symbol3 == "" or symbol4 == "":
                            self.ui.simWarnTxt.setText("Alguno de los simbolos no está escrito. Por favor revise")
                            self.ui.recepBtn.setEnabled(True)
                            
                        else:
                        
                            if geo_threshold_index2 == 1: #linea inclinadacon vertical x=a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 2: #linea inclinada con vertical x=-a
                                selector2 = "vertical"
                                offx2 = self.ui.doubleSpinBox_4.value()
                                offy2 = 0
                                ang2 = 0
                            elif geo_threshold_index2 == 3: #linea inclinada con horizontal y=b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_6.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 4: #linea inclinada con horizontal y=-b
                                selector2 = "horizontal"
                                offx2 = 0
                                offy2 = self.ui.doubleSpinBox_8.value()
                                ang2 = 0
                            elif geo_threshold_index2 == 5: #linea inclinadacon inclinada
                                selector2 = "inclinada"
                                offx2 = self.ui.doubleSpinBox_11.value()
                                offy2 = self.ui.doubleSpinBox_9.value()
                                ang2 = self.ui.doubleSpinBox_10.value()
                        
                            try:
                                point1 = complex(symbol1) 
                                point2 = complex(symbol2)
                                point3 = complex(symbol3)
                                point4 = complex(symbol4)
                                esquema = 'CUSTOM'
                                print("Puntos ingresados")
                                thresholds, etiquetas = MainFunctions.threshold_user(self, n_symbol, selector1=selector1, selector2=selector2, offset_x=offx, offset_y=offy, angle=ang, offset_x2=offx2, offset_y2=offy2, angle2=ang2)
                                self.thresholds_plot = thresholds
                                print("umbrales custom creados")
                                print("offx2, offy2, ang2: {}, {}, {}".format(offx2,offy2,ang2))
                                thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                                print("umbrales custom interpolados")
                                self.constellation_rx = MainFunctions.create_constellation_tx_user(self, n_symbol, point1 = point1, point2 = point2, point3 = point3, point4 = point4)
                                print("constelacion custom creada")
                                regions, bits_save = MainFunctions.check_regions_user(self, n_symbol, etiquetas, thresholds_interpolate, thresholds_interpolate_i, thresholds, self.constellation_rx)
                                print("regiones custom creadas")
                                print(regions)
                            
                                MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, esquema)
                            
                            except Exception as e:
                                print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                                print(e)
                                self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")
                                self.ui.recepBtn.setEnabled(True)
                                


    def transmit_signal_pluto(self):
        print("Enviando...")
        self.configured_signal = False

        threadpool = QThreadPool()
        worker = Worker_transmit_signal(self.symbols_to_send_pluto, self.sdr)
        worker.signals.finished.connect(self.transmit_signal_pluto_action)

        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        threadpool.start(worker)


    def transmit_signal_pluto_action(self):

        MainFunctions.transmit_motion_btn(self, 30, True) 
        print("Transmisión completada")
        self.ui.simWarnTxt.setText("Transmisión completada")
        self.ui.ConfBtn.setEnabled(True)       







    def transmit_signal(self,  fsample, tsim, fport, fsim):
        self.symbols_to_send_pluto = None

        print("Se llamo transmit signal")
        print("Se llamo transmit_motion")
        self.ui.simWarnTxt.setText("")
        
        if self.text_flag_message == True:
            message = self.ui.text.toPlainText()

        elif self.filepath_flag_message == True:
            message = self.filePath[0]

            #message = np.fromfile(self.filePath[0], dtype=np.uint8)
            #int_message = message
            #message = np.unpackbits(message)
            #message = np.asarray(message, dtype=bool)
        
        if message == "":
            self.ui.simWarnTxt.setText("Hace falta definir al mensaje")
        
        if message != "":
            
        ############# MODULACIÓN Y CONSTELACIONES PREDEFINIDAS
#            if self.defined_const_flag == False or self.user_defined_const_flag == False:
#                self.ui.simWarnTxt.setText("Hace falta definir el modo de configuración de la señal")
            
            if self.defined_const_flag == True:
                index_n_symbols = self.ui.simPBitBox.currentIndex()
                print('Index modulacion elegido', self.ui.modBox.currentIndex())
                print('Index n symbol es:',index_n_symbols)
                if index_n_symbols == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir el número de bits codificados por simbolo y tipo de modulación correspondiente")
                
                elif index_n_symbols == 1:
                    index_2_symbols_type_of_modulation = self.ui.modBox.currentIndex()
                    print('El index es:',index_2_symbols_type_of_modulation)
                    n_symbol = 2
                    if index_2_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_2_symbols_type_of_modulation != 0:
                        #Creo la constelación
                        constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_2_symbols_type_of_modulation)
                        constellation = MainFunctions.normalize_constellation(self, constellation)
                        #Le asigno símbolos a los bits. Los modulo
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        #print(message)
                        self.ui.mSim.display(int(len(bits_array)))
                        symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)

                        for inx,packet in enumerate(symbols_to_send):
                            symbols_to_send[inx] = np.multiply(packet,2**14)
                        
                        print(len(symbols_to_send))
                        if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                            add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                            symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                        #now = time.time()

                        self.symbols_to_send_pluto = symbols_to_send
                        
                        #for packet_symbols in symbols_to_send:
                        #    self.sdr.tx(packet_symbols)
                        #print("ENVIANDO")
                        #print(int_message[0:10])
                        #print(int_message[-10:])
                        #after = time.time()
                        #print('Estimado {}', after-now)
                    
                    
                elif index_n_symbols == 2:
                    index_4_symbols_type_of_modulation = self.ui.modBox_2.currentIndex()
                    n_symbol = 4
                    if index_4_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_4_symbols_type_of_modulation != 0:
                        now = time.time()
                        #Creo la constelación
                        constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_4_symbols_type_of_modulation)
                        constellation = MainFunctions.normalize_constellation(self, constellation)
                        #Le asigno símbolos a los bits. Los modulo
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        self.ui.mSim.display(int(len(bits_array)))
                        symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
                        
                        for inx,packet in enumerate(symbols_to_send):
                            symbols_to_send[inx] = np.multiply(packet,2**14)
                        
                        #fig, ax = plt.subplots(3)
                        #ax[0].plot(symbols_to_send[0].real)
                        #ax[0].plot(symbols_to_send[0].imag)
                        #ax[0].set_title('a')
                        #ax[1].plot(symbols_to_send[1].real)
                        #ax[1].plot(symbols_to_send[1].imag)
                        #ax[1].set_title('b')
                        #ax[2].plot(symbols_to_send[7].real)
                        #ax[2].plot(symbols_to_send[7].imag)
                        #plt.show()
                        
                        #El Buffer de muestras de envío se coloca automaticamente por el Pluto. Se debe mantener constante a lo largo de la transmisión. La última parte puede tener menos muestras que las anteriores, se le agregan cero para completar las muestras del buffer configurado.
                        print(len(symbols_to_send))
                        if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                            add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                            symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                        
                        self.symbols_to_send_pluto = symbols_to_send
                        
                        #for packet_symbols in symbols_to_send:
                        #    self.sdr.tx(packet_symbols)
                        #print("ENVIANDO")
                        #print(int_message)
                        #after = time.time()
                        #print('Estimado {}', after-now)
                    
                elif index_n_symbols == 3:
                    index_8_symbols_type_of_modulation = self.ui.modBox_3.currentIndex()
                    n_symbol = 8
                    
                    if index_8_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_8_symbols_type_of_modulation != 0:
                    
                        if index_8_symbols_type_of_modulation == 1 or index_8_symbols_type_of_modulation == 2:
                        
                            #Creo la constelación
                            constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation)
                            constellation = MainFunctions.normalize_constellation(self, constellation)
                            #Le asigno símbolos a los bits. Los modulo
                            bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                            #print(message)
                            self.ui.mSim.display(int(len(bits_array)))
                            symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
    
                            for inx,packet in enumerate(symbols_to_send):
                                symbols_to_send[inx] = np.multiply(packet,2**14)
                            
                            print(len(symbols_to_send))
                            if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                
                            self.symbols_to_send_pluto = symbols_to_send
                            
                            #now = time.time()
                            #for packet_symbols in symbols_to_send:
                            #    self.sdr.tx(packet_symbols)
                            #print("ENVIANDO")
                            #print(int_message[0:10])
                            #print(int_message[-10:])
                            #after = time.time()
                            #print('Estimado {}', after-now)
                            
                        elif index_8_symbols_type_of_modulation == 3:
                            if self.ui.radioButton_2.isChecked() == True:
                                index_variant_8 = 1
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
                                constellation = MainFunctions.normalize_constellation(self, constellation)
                                #Le asigno símbolos a los bits. Los modulo
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                #print(message)
                                self.ui.mSim.display(int(len(bits_array)))
                                symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
        
                                for inx,packet in enumerate(symbols_to_send):
                                    symbols_to_send[inx] = np.multiply(packet,2**14)
                                
                                print(len(symbols_to_send))
                                if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                    add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                    symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                    
                                self.symbols_to_send_pluto = symbols_to_send
                                
                                #now = time.time()
                                #for packet_symbols in symbols_to_send:
                                #    self.sdr.tx(packet_symbols)
                                #print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                #after = time.time()
                                #print('Estimado {}', after-now)
                                
                            elif self.ui.radioButton_3.isChecked() == True:
                                index_variant_8 = 2
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
                                constellation = MainFunctions.normalize_constellation(self, constellation)
                                #Le asigno símbolos a los bits. Los modulo
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                #print(message)
                                self.ui.mSim.display(int(len(bits_array)))
                                symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
        
                                for inx,packet in enumerate(symbols_to_send):
                                    symbols_to_send[inx] = np.multiply(packet,2**14)
                                
                                print(len(symbols_to_send))
                                if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                    add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                    symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                    
                                self.symbols_to_send_pluto = symbols_to_send
                                
                                #now = time.time()
                                #for packet_symbols in symbols_to_send:
                                #    self.sdr.tx(packet_symbols)
                                #print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                #after = time.time()
                                #print('Estimado {}', after-now)
                                
                            elif self.ui.radioButton_4.isChecked() == True:
                                index_variant_8 = 3
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
                                constellation = MainFunctions.normalize_constellation(self, constellation)
                                #Le asigno símbolos a los bits. Los modulo
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                #print(message)
                                self.ui.mSim.display(int(len(bits_array)))
                                symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
        
                                for inx,packet in enumerate(symbols_to_send):
                                    symbols_to_send[inx] = np.multiply(packet,2**14)
                                
                                print(len(symbols_to_send))
                                if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                    add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                    symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                    
                                self.symbols_to_send_pluto = symbols_to_send
                                
                                #now = time.time()
                                #for packet_symbols in symbols_to_send:
                                #    self.sdr.tx(packet_symbols)
                                #print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                #after = time.time()
                                #print('Estimado {}', after-now)
                            
                    
                elif index_n_symbols == 4:
                    index_16_symbols_type_of_modulation = self.ui.modBox_4.currentIndex()
                    n_symbol = 16
                    
                    if index_16_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_16_symbols_type_of_modulation != 0:
                    
                        if index_16_symbols_type_of_modulation == 1:
                        
                            #Creo la constelación
                            constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation)
                            constellation = MainFunctions.normalize_constellation(self, constellation)
                            #Le asigno símbolos a los bits. Los modulo
                            bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                            #print(message)
                            self.ui.mSim.display(int(len(bits_array)))
                            symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
        
                            for inx,packet in enumerate(symbols_to_send):
                                symbols_to_send[inx] = np.multiply(packet,2**14)
                                
                            print(len(symbols_to_send))
                            if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                
                            self.symbols_to_send_pluto = symbols_to_send
                            
                            #now = time.time()
                            #for packet_symbols in symbols_to_send:
                            #    self.sdr.tx(packet_symbols)
                            #print("ENVIANDO")
                            #print(int_message[0:10])
                            #print(int_message[-10:])
                            #after = time.time()
                            #print('Estimado {}', after-now)
                        
                        elif index_16_symbols_type_of_modulation == 2:
                            if self.ui.radioButton_5.isChecked() == True:
                                index_variant_16 = 1
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
                                constellation = MainFunctions.normalize_constellation(self, constellation)
                                #Le asigno símbolos a los bits. Los modulo
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                #print(message)
                                self.ui.mSim.display(int(len(bits_array)))
                                symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
        
                                for inx,packet in enumerate(symbols_to_send):
                                    symbols_to_send[inx] = np.multiply(packet,2**14)
                                
                                print(len(symbols_to_send))
                                if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                    add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                    symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                    
                                self.symbols_to_send_pluto = symbols_to_send
                                
                                #now = time.time()
                                #for packet_symbols in symbols_to_send:
                                #    self.sdr.tx(packet_symbols)
                                #print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                #after = time.time()
                                #print('Estimado {}', after-now)
                                
                            elif self.ui.radioButton_6.isChecked() == True:
                                index_variant_16 = 2
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
                                constellation = MainFunctions.normalize_constellation(self, constellation)
                                #Le asigno símbolos a los bits. Los modulo
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                #print(message)
                                self.ui.mSim.display(int(len(bits_array)))
                                symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
        
                                for inx,packet in enumerate(symbols_to_send):
                                    symbols_to_send[inx] = np.multiply(packet,2**14)
                                
                                print(len(symbols_to_send))
                                if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                    add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                    symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                    
                                self.symbols_to_send_pluto = symbols_to_send
                                
                                #now = time.time()
                                #for packet_symbols in symbols_to_send:
                                #    self.sdr.tx(packet_symbols)
                                #print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                #after = time.time()
                                #print('Estimado {}', after-now)

                            elif self.ui.radioButton_7.isChecked() == True:
                                index_variant_16 = 3
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
                                constellation = MainFunctions.normalize_constellation(self, constellation)
                                #Le asigno símbolos a los bits. Los modulo
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                #print(message)
                                self.ui.mSim.display(int(len(bits_array)))
                                symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)
        
                                for inx,packet in enumerate(symbols_to_send):
                                    symbols_to_send[inx] = np.multiply(packet,2**14)
                                
                                print(len(symbols_to_send))
                                if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                                    add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                                    symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                                
                                self.symbols_to_send_pluto = symbols_to_send
                                
                                #now = time.time()
                                #for packet_symbols in symbols_to_send:
                                #    self.sdr.tx(packet_symbols)
                                #print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                #after = time.time()
                                #print('Estimado {}', after-now)     
        
            
        ############ CONSTELACIÓN DEFINIDA POR EL USUARIO (HACE FALTA AGREGAR LA OPCIÓN DE SI EL USUARIO NO ESCRIBE EN EL FORMATO QUE CORRESPONDE, LANZAR EL AVISO PARA QUE NO PUEDA TRASNMITIR Y AVISE AL USUARIO)
                      
            elif self.user_defined_const_flag == True:
                index_n_symbols = self.ui.simPBitBox_2.currentIndex()

                if index_n_symbols == 1:
                    symbol1 = self.ui.text_3.toPlainText() #SIMBOLO 1
                    symbol2 = self.ui.text_4.toPlainText() #SIMBOLO 2
                    n_symbol = 2

                    try:
                        point1 = complex(symbol1) #Cuidado con los eval
                        point2 = complex(symbol2)

                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")


                    constellation = MainFunctions.create_constellation_tx_user(self, 2, point1 = point1, point2 = point2)
                    constellation = MainFunctions.normalize_constellation(self, constellation)
                    bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                    self.ui.mSim.display(int(len(bits_array)))
                    symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)

                    for inx,packet in enumerate(symbols_to_send):
                        symbols_to_send[inx] = np.multiply(packet,2**14)

                    if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                        add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                        symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                        
                    self.symbols_to_send_pluto = symbols_to_send
                    
                    #for packet_symbols in symbols_to_send:
                    #    self.sdr.tx(packet_symbols)
                            
                
                elif index_n_symbols == 2:
                    symbol1 = self.ui.text_5.toPlainText() #SIMBOLO 1
                    symbol2 = self.ui.text_7.toPlainText() #SIMBOLO 2
                    symbol3 = self.ui.text_8.toPlainText() #SIMBOLO 3
                    symbol4 = self.ui.text_9.toPlainText() #SIMBOLO 4
                    n_symbol = 4

                    try:
                        point1 = complex(symbol1) 
                        point2 = complex(symbol2)
                        point3 = complex(symbol3)
                        point4 = complex(symbol4)

                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")

                    constellation = MainFunctions.create_constellation_tx_user(self, 4, point1 = point1, point2 = point2, point3=point3, point4=point4)
                    constellation = MainFunctions.normalize_constellation(self, constellation)
                    bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                    self.ui.mSim.display(int(len(bits_array)))
                    symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)

                    for inx,packet in enumerate(symbols_to_send):
                        symbols_to_send[inx] = np.multiply(packet,2**14)

                    if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                        add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                        symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)
                    
                    self.symbols_to_send_pluto = symbols_to_send
                    
                    #for packet_symbols in symbols_to_send:
                    #    self.sdr.tx(packet_symbols)
                    
        #MainFunctions.transmit_motion_btn(self, 30, True) #Muestra boton de Transmitir señal luego de haberla configurado por completo       


    def graph_modulated_signal_prev(self):
        fsample = self.fsample
        self.ui.simWarnTxt.setText("")
    
        fsim = self.ui.fbit.value()
        tsim = self.ui.tbit.value()
        fport = self.ui.fport.value()

        if self.text_flag_message == True:
            message = self.ui.text.toPlainText()

        if self.filepath_flag_message == True:
            message = self.filePath[0]

            #message = np.fromfile(self.filePath[0], dtype=np.uint8)
            #int_message = message
            #message = np.unpackbits(message)
            #message = np.asarray(message, dtype=bool)
        
        if message == "":
            self.ui.simWarnTxt.setText("Hace falta definir al mensaje")
        
        if message != "":
            
        ############# MODULACIÓN Y CONSTELACIONES PREDEFINIDAS  ---------------------- ACA SYMBOLS TO SEND AL PULSE SHAPING           
#            if self.defined_const_flag == False or self.user_defined_const_flag == False:
#                self.ui.simWarnTxt.setText("Hace falta definir el modo de configuración de la señal")

            if self.defined_const_flag == True:
                index_n_symbols = self.ui.simPBitBox.currentIndex()
                if index_n_symbols == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir el número de bits codificados por simbolo y tipo de modulación correspondiente")
                
                elif index_n_symbols == 1:
                    index_2_symbols_type_of_modulation = self.ui.modBox.currentIndex()
                    n_symbol = 2
                    
                    if index_2_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_2_symbols_type_of_modulation != 0:
                        constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_2_symbols_type_of_modulation)
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        self.ui.mSim.display(int(len(bits_array)))
                        #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                        symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                        MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample) 
                    
                elif index_n_symbols == 2:
                    index_4_symbols_type_of_modulation = self.ui.modBox_2.currentIndex()
                    n_symbol = 4
                    
                    if index_4_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_4_symbols_type_of_modulation != 0:
                        constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_4_symbols_type_of_modulation)
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        self.ui.mSim.display(int(len(bits_array)))
                        #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                        symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                        
                        MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample) 
                    
                elif index_n_symbols == 3:
                    index_8_symbols_type_of_modulation = self.ui.modBox_3.currentIndex()
                    n_symbol = 8
                    
                    if index_8_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_8_symbols_type_of_modulation != 0:
                    
                        if index_8_symbols_type_of_modulation == 1 or index_8_symbols_type_of_modulation == 2:
                        
                            constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation)
                            bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                            self.ui.mSim.display(int(len(bits_array)))
                            #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                            symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                            MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample) 
                        
                        elif index_8_symbols_type_of_modulation == 3:
                            if self.ui.radioButton_2.isChecked() == True:
                                index_variant_8 = 1

                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                self.ui.mSim.display(int(len(bits_array)))
                                #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                                symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                                MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                                
                                
                            elif self.ui.radioButton_3.isChecked() == True:
                                index_variant_8 = 2
                                
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                self.ui.mSim.display(int(len(bits_array)))
                                #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                                symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                                MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                                
                            elif self.ui.radioButton_4.isChecked() == True:
                                index_variant_8 = 3
                                
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                self.ui.mSim.display(int(len(bits_array)))
                                #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                                symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                                MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                            
                    
                elif index_n_symbols == 4:
                    index_16_symbols_type_of_modulation = self.ui.modBox_4.currentIndex()
                    n_symbol = 16
                    
                    if index_16_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_16_symbols_type_of_modulation != 0:
                    
                        if index_16_symbols_type_of_modulation == 1:
                        
                            constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation)
                            bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                            self.ui.mSim.display(int(len(bits_array)))
                            #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                            symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                            MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                        
                        elif index_16_symbols_type_of_modulation == 2:
                            if self.ui.radioButton_5.isChecked() == True:
                                index_variant_16 = 1
                                
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                self.ui.mSim.display(int(len(bits_array)))
                                #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                                symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                                MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                                
                                
                            elif self.ui.radioButton_6.isChecked() == True:
                                index_variant_16 = 2
                                
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                self.ui.mSim.display(int(len(bits_array)))
                                #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                                symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                                MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                                
                            elif self.ui.radioButton_7.isChecked() == True:
                                index_variant_16 = 3
                                
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
                                bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                                self.ui.mSim.display(int(len(bits_array)))
                                #symbols_to_send = np.asarray(MainFunctions.add_tsimb(self, tsim, fsample, bits_array), dtype=complex)
                                symbols_to_send = MainFunctions.pulse_shape(self,bits_array, tsim, fsample, beta=0.35)
                                MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)        
                        
        ############ CONSTELACIÓN DEFINIDA POR EL USUARIO (HACE FALTA AGREGAR LA OPCIÓN DE SI EL USUARIO NO ESCRIBE EN EL FORMATO QUE CORRESPONDE, LANZAR EL AVISO PARA QUE NO PUEDA TRASNMITIR Y AVISE AL USUARIO)         
                   
            elif self.user_defined_const_flag == True:
                index_n_symbols = self.ui.simPBitBox_2.currentIndex()
                self.ui.simWarnTxt.setText("")

                if index_n_symbols == 1:
                    symbol1 = self.ui.text_3.toPlainText()
                    symbol2 = self.ui.text_4.toPlainText()
                    self.ui.simWarnTxt.setText("")

                    try:
                        point1 = complex(symbol1) #Cuidado con los eval
                        point2 = complex(symbol2)

                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguna de las bases escrita tiene un error. Por favor revise e intente otra vez")


                    constellation = MainFunctions.create_constellation_tx_user(self, 2, point1 = point1, point2 = point2)
                    bits_array = MainFunctions.prepare_to_send(self, message, 2, constellation)
                    self.ui.mSim.display(int(len(bits_array)))
                    symbols_to_send = MainFunctions.pulse_shape(self, bits_array, tsim, fsample)
                            
                    MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                            
          
                elif index_n_symbols == 2:
                    symbol1 = self.ui.text_5.toPlainText()
                    symbol2 = self.ui.text_7.toPlainText()
                    symbol3 = self.ui.text_8.toPlainText()
                    symbol4 = self.ui.text_9.toPlainText()

                    try:
                        point1 = complex(symbol1) 
                        point2 = complex(symbol2)
                        point3 = complex(symbol3)
                        point4 = complex(symbol4)

                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguno de los simbolos escritos tiene un error. Por favor revise e intente otra vez")


                    constellation = MainFunctions.create_constellation_tx_user(self, 4, point1 = point1, point2 = point2, point3=point3, point4=point4)
                    bits_array = MainFunctions.prepare_to_send(self, message, 4, constellation)
                    self.ui.mSim.display(int(len(bits_array)))
                    symbols_to_send = MainFunctions.pulse_shape(self, bits_array, tsim, fsample)
                        
                    MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)


    def defined_const(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_12)
        
        if self.defined_const_flag == False:
            self.defined_const_flag = True
            if self.user_defined_const_flag == False:
                MainFunctions.number_of_symbols_transmition(self, 100, True)
                
        if self.user_defined_const_flag == True:
            self.user_defined_const_flag = False
            
            if self.number_of_symbols_flag == True:
                self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_18)
                MainFunctions.type_of_modulation(self, 100, True)
                self.number_of_symbols_flag = False

            self.ui.simPBitBox_2.setCurrentIndex(0)
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_21)
            self.ui.text_9.setPlainText("")
            self.ui.text_3.setPlainText("")
            self.ui.text_4.setPlainText("")
            self.ui.text_5.setPlainText("")
            self.ui.text_8.setPlainText("")
            self.ui.text_7.setPlainText("")
            
            
        
    def user_defined_const(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_14)    
        
        if self.user_defined_const_flag == False:
            self.user_defined_const_flag = True
            if self.defined_const_flag == False:
                MainFunctions.number_of_symbols_transmition(self, 100, True)
                
        if self.defined_const_flag == True:
            self.defined_const_flag = False

            if self.number_of_symbols_flag == True:
                self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_18)
                MainFunctions.type_of_modulation(self, 100, True)
                self.number_of_symbols_flag = False 

            self.ui.simPBitBox.setCurrentIndex(0)
            self.ui.modBox.setCurrentIndex(0)
            self.ui.modBox_2.setCurrentIndex(0)
            self.ui.modBox_3.setCurrentIndex(0)
            self.ui.modBox_4.setCurrentIndex(0)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)
                
                
    def user_defined_const_complex(self, index):
        
        if index == 0 and self.user_defined_const_complex_flag == True:
            self.user_defined_const_complex_flag = False
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_21)

            
        if index == 1:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_19)
            if self.user_defined_const_complex_flag == False:
                self.user_defined_const_complex_flag = True
                
        if index == 2:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_20)
            if self.user_defined_const_complex_flag == False:
                self.user_defined_const_complex_flag = True
                
            
    
    def type_of_modulation(self, index):
        if index == 0 and self.number_of_symbols_flag == True:
            
            self.ui.modBox.setCurrentIndex(0)
            self.ui.modBox_2.setCurrentIndex(0)
            self.ui.modBox_3.setCurrentIndex(0)
            self.ui.modBox_4.setCurrentIndex(0)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)
            
            self.number_of_symbols_flag = False
            MainFunctions.type_of_modulation(self, 100, True)
            
        if index == 1:
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_13)
            
            self.ui.modBox_2.setCurrentIndex(0)
            self.ui.modBox_3.setCurrentIndex(0)
            self.ui.modBox_4.setCurrentIndex(0)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)
                
            if self.number_of_symbols_flag == False:
                self.number_of_symbols_flag = True
                MainFunctions.type_of_modulation(self, 100, True)
                
        if index == 2:
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_15)
            
            self.ui.modBox.setCurrentIndex(0)
            self.ui.modBox_3.setCurrentIndex(0)
            self.ui.modBox_4.setCurrentIndex(0)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)
            
            if self.number_of_symbols_flag == False:
                self.number_of_symbols_flag = True
                MainFunctions.type_of_modulation(self, 100, True)
                
        if index == 3:
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_16)
            
            self.ui.modBox.setCurrentIndex(0)
            self.ui.modBox_2.setCurrentIndex(0)
            self.ui.modBox_4.setCurrentIndex(0)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)      

            
            if self.number_of_symbols_flag == False:
                self.number_of_symbols_flag = True
                MainFunctions.type_of_modulation(self, 100, True)
                
        if index == 4:
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_17)
            
            self.ui.modBox.setCurrentIndex(0)
            self.ui.modBox_2.setCurrentIndex(0)
            self.ui.modBox_3.setCurrentIndex(0)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)

            
            if self.number_of_symbols_flag == False:
                self.number_of_symbols_flag = True
                MainFunctions.type_of_modulation(self, 100, True)
                

    def eight_symbols_options(self, index):
        if index == 0:
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)

        if index == 1:
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)

        if index == 2:
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)
            
        if index == 3:            
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_25)
            
        
    def sixteen_symbols_options(self, index):            
        if index == 0:
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)

        if index == 1:
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_24)
            
        if index == 2:            
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_26)
            
               
    def format_box_animation_desicion(self, index):
        
        if index == 0 and self.format_path_flag_received == True:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = False
            
        if index == 1 and self.format_path_flag_received == True:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = False
            
        if index == 2 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
            
        if index == 3 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
            
        if index == 4 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
            
        if index == 5 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
            
        if index == 6 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
            
        if index == 7 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
            
        if index == 8 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
            
        if index == 9 and self.format_path_flag_received == False:
            MainFunctions.format_rec(self, 70, True)
            self.format_path_flag_received = True
      
        
    def graph_original_bits(self):

        fsample = self.fsample
        tsim = self.ui.tbit.value() 

        if self.defined_const_flag == True:
            index_n_symbols = self.ui.simPBitBox.currentIndex()

        if self.user_defined_const_flag == True:
            index_n_symbols = self.ui.simPBitBox_2.currentIndex()

        amplitude = 2
        codeline = self.ui.codeBox.currentIndex()
        
        if self.text_flag_message == True:
            message = self.ui.text.toPlainText()

        if self.filepath_flag_message == True:
            message = self.filePath[0]

            #message = np.fromfile(self.filePath[0], dtype=np.uint8)
            #int_message = message
            #message = np.unpackbits(message)
            #message = np.asarray(message, dtype=bool)
        
        if message == "" and index_n_symbols == 0:
            self.ui.simWarnTxt.setText("Hace falta definir al mensaje y número de simbolos por bit")
        elif message == "":
            self.ui.simWarnTxt.setText("Hace falta definir al mensaje")
        elif index_n_symbols == 0:
            self.ui.simWarnTxt.setText("Hace falta definir el número de simbolos por bit")  
        elif message != "" and index_n_symbols != 0:
            self.ui.simWarnTxt.setText("")
            message = MainFunctions.string_to_bits(self, message)
            MainFunctions.graph_original_bits(self, message, fsample, amplitude, codeline, index_n_symbols, tsim)     
        

    def bit_frecuency(self, d1):
        float_value = float(d1.replace(',', '.'))
        try:    
            bit_value = float(1/float_value)
        except:
            self.ui.tbit.setValue(0)
        try:      
            self.ui.tbit.setValue(bit_value)
        except:
            self.ui.tbit.setValue(0)
        
    def bit_duration(self, d2):
        float_value = float(d2.replace(',', '.'))
        try:    
            frec_value = float(1/float_value)
        except:
            self.ui.fbit.setValue(0)
        try:     
            self.ui.fbit.setValue(frec_value)
        except:
            self.ui.fbit.setValue(0)
        
        
        
    def getArchive(self):
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\')
        if self.filePath[0]:
            self.ui.archivePath.setText(self.filePath[0])
            
    def setArchive(self):
        self.filePath_message_received = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open file', 'C:\\')
        filePath = self.filePath_message_received

        if filePath:
            self.ui.archivePath.setText(filePath)
            
    def defined_threshold(self):
        if self.defined_threshold_flag == False and self.user_defined_threshold_flag == False:
            MainFunctions.symbols_rec(self, 100, True)
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_7)           
            self.defined_threshold_flag = True
            
        if self.defined_threshold_flag == False and self.user_defined_threshold_flag == True:
            self.defined_threshold_flag = True
            self.user_defined_threshold_flag = False
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_7)
            
            if self.user_df_threshold_options == True:
                MainFunctions.user_defined_threshold_rec(self, 150, True)
                self.user_df_threshold_options = False
                self.ui.simPBitBox.setCurrentIndex(0)
                self.ui.simPBitBox_2.setCurrentIndex(0)
                self.ui.codelineBox_4.setCurrentIndex(0)
                self.ui.codelineBox_3.setCurrentIndex(0)
                
            if self.add_threshold_2_symbols_flag == True or self.add_threshold_4_symbols_flag == True or (self.add_threshold_4_symbols_flag == True and self.add_threshold_4_symbols_2_flag == True):
                self.add_threshold_2_symbols_flag = False
                self.add_threshold_4_symbols_flag = False
                self.add_threshold_4_symbols_2_flag = False
                self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_25)
                self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_26)
                self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_32)
                self.ui.codelineBox_4.setCurrentIndex(0)
                self.ui.codelineBox_3.setCurrentIndex(0)
                self.ui.codelineBox_2.setCurrentIndex(0)
            
    def user_defined_threshold(self):
        if self.user_defined_threshold_flag == False and self.defined_threshold_flag == False:
            MainFunctions.symbols_rec(self, 100, True)
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_8)           
            self.user_defined_threshold_flag = True
            
        if self.user_defined_threshold_flag == False and self.defined_threshold_flag == True:
            self.user_defined_threshold_flag = True
            self.defined_threshold_flag = False
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_8)
            
            if self.df_threshold_options == True:
                MainFunctions.defined_threshold_rec(self, 150, True)
                self.df_threshold_options = False
                self.ui.simPBitBox_2.setCurrentIndex(0)
                self.ui.simPBitBox.setCurrentIndex(0)
                self.ui.geoBox_1.setCurrentIndex(0)
                self.ui.geoBox_2.setCurrentIndex(0)
                self.ui.geoBox_3.setCurrentIndex(0)
                self.ui.geoBox_4.setCurrentIndex(0)
                
            
    def symbols_per_bit_DT(self, index):

        if index == 0 and self.df_threshold_options == True:
            MainFunctions.defined_threshold_rec(self, 120, True)
            self.df_threshold_options = False
        if index == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)
            if self.df_threshold_options == False:
                MainFunctions.defined_threshold_rec(self, 120, True)
                self.df_threshold_options = True
        if index == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            if self.df_threshold_options == False:
                MainFunctions.defined_threshold_rec(self, 120, True)
                self.df_threshold_options = True
        if index == 3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
            if self.df_threshold_options == False:
                MainFunctions.defined_threshold_rec(self, 120, True)
                self.df_threshold_options = True
        if index == 4:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
            if self.df_threshold_options == False:
                MainFunctions.defined_threshold_rec(self, 120, True)
                self.df_threshold_options = True
                
                 
    def symbols_per_bit_UDT(self, index):

        if index == 0 and self.user_df_threshold_options == True:
            MainFunctions.user_defined_threshold_rec(self, 150, True)
            self.user_df_threshold_options = False           
        if index == 1:
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_12)
            if self.user_df_threshold_options == False:
                MainFunctions.user_defined_threshold_rec(self, 150, True)
                self.user_df_threshold_options = True 
            if self.add_threshold_4_symbols_flag == True:
                self.add_threshold_4_symbols_flag = False
                self.add_threshold_2_symbols_flag = True
                self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_25)
                self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_26)
                self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_32)
                self.ui.codelineBox_4.setCurrentIndex(0)
                self.ui.codelineBox_3.setCurrentIndex(0)
                self.ui.codelineBox_2.setCurrentIndex(0)
                       
        if index == 2:
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_13)
            if self.user_df_threshold_options == False:
                MainFunctions.user_defined_threshold_rec(self, 150, True)
                self.user_df_threshold_options = True
            if self.add_threshold_2_symbols_flag == True:
                self.add_threshold_2_symbols_flag = False
                self.add_threshold_4_symbols_flag = True
                self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_25)
                self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_26)
                self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_32)
                self.ui.codelineBox_4.setCurrentIndex(0)
                self.ui.codelineBox_3.setCurrentIndex(0)
                self.ui.codelineBox_2.setCurrentIndex(0)
        
            
    def add_threshold_2_symbols(self, index):

        if index == 0 and self.add_threshold_2_symbols_flag == True:
            self.add_threshold_2_symbols_flag = False
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_26)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_32)
            
        if index == 1:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_20)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_33)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
         
        if index == 2:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_21)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_33)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
            
        if index == 3:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_22)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_33)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
            
        if index == 4:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_23)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_33)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
            
        if index == 5:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_24)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_33)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
                        
        
    def add_threshold_4_symbols(self, index):

        if index == 0 and self.add_threshold_4_symbols_flag == True:
            self.add_threshold_4_symbols_flag = False
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_26)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_32)
            
        if index == 1:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_20)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True
         
        if index == 2:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_21)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True
                
        if index == 3:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_22)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True
            
        if index == 4:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_23)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True    
        
        if index == 5:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_24)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True

        
    def add_threshold_4_symbols_2(self, index):
        
        if index == 0 and self.add_threshold_4_symbols_2_flag == True:
            self.add_threshold_4_symbols_2_flag = False
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_25)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_32)

        if index == 1:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_15)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True
                 
        if index == 2:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_16)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True
            
        if index == 3:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_17)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True

        if index == 4:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_19)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True            
            
        if index == 5:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_18)
            self.ui.stackedWidget_8.setCurrentWidget(self.ui.page_34)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True 
        
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    dirname = os.path.abspath(os.getcwd())
    filename = os.path.join(dirname, '/prof_blue.ico')

    app.setWindowIcon(QIcon(filename))
    window.setWindowIcon(QIcon (filename))
    
    sys.exit(app.exec_())
    
    
    
