#Animation Libraries
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# GUI FILE
from ui_homepage import Ui_MainWindow
from ui_reception import Ui_reception
from ui_transmission1 import Ui_transmission1
from ui_transmission2 import Ui_transmission2
from ui_functions import *

#Other libraries
#import ctypes
#myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import pyqtgraph as pg
import time

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
        
        self.fsample = 522000
        
        #REAL TIME GRAPH NECESARY OBJECTS
        self.timer = QtCore.QTimer()
        self.graphWidget = pg.PlotWidget(background= "w")
        self.graphWidget_2 = pg.PlotWidget(background= "w")
        self.graphWidget_3 = pg.PlotWidget(background= "w")
        
        #FLAGS
        self.BB_graph_flag = False
        self.delete_status = False
        self.format_path_flag_received = False
        self.defined_threshold_flag = False
        self.user_defined_threshold_flag = False
        self.df_threshold_options = False
        self.user_df_threshold_options = False
        self.add_threshold_page_flag = False
        
        self.add_threshold_2_symbols_flag = False
        self.add_threshold_4_symbols_flag = False
        self.add_threshold_4_symbols_2_flag = False
        
        self.reception_initiated = False   
        
        #WINDOW ICON
        self.ventana.setWindowTitle("Digital Comunications Toolkit - Reception Mode")
        
        ## TOGGLE/MENU
        ########################################################################
        self.ui.menuBtn.clicked.connect(lambda: MainFunctions.toggleMenu(self, 180, True))
        
        #BUTTON ACTIONS
        ############################################################################################# 
              
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
        
        #CHOOSE PATH
        self.ui.ArchiveBtn.clicked.connect(self.setArchive)

        #RECEIVED MESSAGE FORMAT
        self.ui.formatBox.activated.connect(self.format_box_animation_desicion)
        
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
        
        ## SYMBOL DETECTION
        ########################################################################
        
        #DEFINED THRESHOLD
        self.ui.UmbPreBtn.pressed.connect(self.defined_threshold)
        self.ui.simPBitBox.activated.connect(self.symbols_per_bit_DT)   
        
        #USER DEFINED THRESHOLD
        self.ui.UmbDisBtn.pressed.connect(self.user_defined_threshold)
        self.ui.simPBitBox_2.activated.connect(self.symbols_per_bit_UDT)
        self.ui.addBtn.pressed.connect(self.add_threshold)
        self.ui.noaddBtn.pressed.connect(self.no_add_threshold)

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
        self.ui.prevBBBTN.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3))
        
        #PREV BAND PASS
        self.ui.prevPBBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4))
        
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
        self.ui.TransBtn.clicked.connect(self.transmit_signal)
        
            
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
        self.ui.prevBBBTN.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3))
        
        #PREV CARRIER
        self.ui.prevPBBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4))
        
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
        self.ui.TransBtn.clicked.connect(self.transmit_signal)
        
        
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
    def configure_signal(self):
        if self.configured_signal == False:
            self.configured_signal = True
            
            fsim = self.ui.fbit.value()
            tsim = self.ui.tbit.value()
            fport = self.ui.fport.value()
            fsample = self.fsample
            print('fsample configurada', fsample)
            print('tsim elegido:', tsim)   
        
            self.sdr = adi.Pluto("ip:192.168.2.1")        
            self.sdr.tx_hardwaregain_chan0 = 0
            self.sdr.tx_lo = int(fport*1e6)
            self.sdr.sample_rate = int(fsample)
            self.sdr.tx_rf_bandwidth = int(fsample)
            
            MainFunctions.transmit_motion_btn(self, 30, True)
    
    
    
    def graph_received_result(self):
        t = np.arange(0,len(self.muestras))
        plt.cla()
        plt.plot(self.muestras.real,self.muestras.imag,"*")
        plt.show()
        
        print(len(self.muestras))

    
    def reception_signal(self):
        message_format = self.ui.formatBox.currentIndex()
        self.muestras = np.array([])
        
        fsample = self.fsample
        frequency_carrier = self.ui.fport.value()
        tsim = self.ui.tbit.value()
        gain_rx = self.ui.gananRx.value()
        buffer = 30000
        
        #frequency_carrier = 400e6
        #tsim = 0.0001
        print("1. CONFIGURANDO PLUTO PARA RECEPCIÓN")
        self.sdr = adi.Pluto("ip:192.168.2.1")
        self.sdr.gain_control_mode_chan0 = "manual"
        self.sdr.rx_hardwaregain_chan0 = gain_rx
        self.sdr.rx_lo = int(frequency_carrier*1e6)
        self.sdr.sample_rate = int(fsample)
        self.sdr.rx_rf_bandwidth = int(fsample) # filter width, just set it to the same as sample rate for now
        self.sdr.rx_buffer_size = buffer
        print("1- PLUTO CONFIGURADO")
        print("2. CONFIGURANDO UMBRALES Y REGIONES")
        
        ######## UMBRALES PREDEFINIDOS
        
        if self.ui.UmbPreBtn.isChecked() == True:
            n_symbol_index = self.ui.simPBitBox.currentIndex()                  
            
            if n_symbol_index == 1:
                threshold_index = self.ui.geoBox_1.currentIndex()
                n_symbol = 2
                
                thresholds = MainFunctions.threshold_defined(self, n_symbol, threshold_index)
                regions, bits_save = MainFunctions.define_regions(self, n_symbol, threshold_index)
                thresholds_interpolate, thresholds_interpolate_i = MainFunctions.interpolate_umbrales(self, thresholds)
                print("2- UMBRALES Y REGIONES CONFIGURADOS")
                print("3. RECIBIENDO...")
                MainFunctions.start_rx(self, frequency_carrier, fsample, tsim, buffer, thresholds, thresholds_interpolate, thresholds_interpolate_i, regions, bits_save, n_symbol, threshold_index)
                
            elif n_symbol_index == 2:
                threshold_index = self.ui.geoBox_2.currentIndex()
                n_symbol = 4
                
                
                
            elif n_symbol_index == 3:
                threshold_index = self.ui.geoBox_3.currentIndex()
                n_symbol = 8
                
                
            elif n_symbol_index == 4:
                threshold_index = self.ui.geoBox_4.currentIndex()
                n_symbol = 16
                
        ######## UMBRALES DEFINIDOS POR EL USUARIO
 
        if self.ui.UmbDisBtn.isChecked() == True:
            n_symbol_index = self.ui.simPBitBox_2.currentIndex()
            
            if n_symbol_index == 1:
                geo_threshold_index = self.ui.codelineBox_4.currentIndex()
                
                if geo_threshold_index == 1:
                    x = self.ui.doubleSpinBox_12.value()
                    off = self.ui.doubleSpinBox_13.value()
                    
                    
                elif geo_threshold_index == 2:
                    x = self.ui.doubleSpinBox_14.value()
                    off = self.ui.doubleSpinBox_15.value()
                    
                    
                elif geo_threshold_index == 3:
                    y = self.ui.doubleSpinBox_16.value()
                    off = self.ui.doubleSpinBox_17.value()
                    
                    
                elif geo_threshold_index == 4:
                    y = self.ui.doubleSpinBox_18.value()
                    off = self.ui.doubleSpinBox_19.value()
                    
                    
                elif geo_threshold_index == 5:
                    ang = self.ui.doubleSpinBox_20.value()
                    offx = self.ui.doubleSpinBox_21.value()
                    offy = self.ui.doubleSpinBox_22.value()
                    
                    
                    
                
            elif n_symbol_index == 2:
                geo_threshold_index = self.ui.codelineBox_3.currentIndex()
                
                if geo_threshold_index == 1:
                    x = self.ui.doubleSpinBox_12.value()
                    off = self.ui.doubleSpinBox_13.value()
                    
                    
                elif geo_threshold_index == 2:
                    x = self.ui.doubleSpinBox_14.value()
                    off = self.ui.doubleSpinBox_15.value()
                    
                    
                elif geo_threshold_index == 3:
                    y = self.ui.doubleSpinBox_16.value()
                    off = self.ui.doubleSpinBox_17.value()
                    
                    
                elif geo_threshold_index == 4:
                    y = self.ui.doubleSpinBox_18.value()
                    off = self.ui.doubleSpinBox_19.value()
                    
                    
                elif geo_threshold_index == 5:
                    ang = self.ui.doubleSpinBox_20.value()
                    offx = self.ui.doubleSpinBox_21.value()
                    offy = self.ui.doubleSpinBox_22.value()
                    
                    
                
                if self.ui.addBtn.isChecked() == True:
                    geo_threshold_index2 = self.ui.codelineBox_2.currentIndex()
                    
                    if geo_threshold_index2 == 1:
                        off = self.ui.doubleSpinBox_2.value()
                        x = self.ui.doubleSpinBox.value()
                        
                        
                    elif geo_threshold_index2 == 2:
                        off = self.ui.doubleSpinBox_3.value()
                        x = self.ui.doubleSpinBox_4.value()
                        
                        
                    elif geo_threshold_index2 == 3:
                        off = self.ui.doubleSpinBox_5.value()
                        y = self.ui.doubleSpinBox_6.value()
                        
                        
                    elif geo_threshold_index2 == 4:
                        off = self.ui.doubleSpinBox_7.value()
                        y = self.ui.doubleSpinBox_8.value()
                        
                        
                    elif geo_threshold_index2 == 5:
                        ang = self.ui.doubleSpinBox_10.value()
                        offx = self.ui.doubleSpinBox_11.value()
                        offy = self.ui.doubleSpinBox_9.value()
                        
                        

    def transmit_signal(self):
        self.configured_signal = False
        MainFunctions.transmit_motion_btn(self, 30, True)
        self.ui.simWarnTxt.setText("")
            
        fsim = self.ui.fbit.value()
        tsim = self.ui.tbit.value()
        fport = self.ui.fport.value()
        fsample = self.fsample   
        
        if self.text_flag_message == True:
            message = self.ui.text.toPlainText()
        elif self.filepath_flag_message == True:
            message = np.fromfile(self.filePath[0], dtype=np.uint8)
            int_message = message
            message = np.unpackbits(message)
            message = np.asarray(message, dtype=bool)
        
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
                    self.ui.simWarnTxt.setText("Hace falta definir el número de simbolos por bit y tipo de modulación correspondiente")
                
                elif index_n_symbols == 1:
                    index_2_symbols_type_of_modulation = self.ui.modBox.currentIndex()
                    print('El index es:',index_2_symbols_type_of_modulation)
                    n_symbol = 2
                    if index_2_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_2_symbols_type_of_modulation != 0:
                        #Creo la constelación
                        constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_2_symbols_type_of_modulation)
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
                        now = time.time()
                        for packet_symbols in symbols_to_send:
                            self.sdr.tx(packet_symbols)
                        print("ENVIANDO")
                        print(int_message[0:10])
                        print(int_message[-10:])
                        after = time.time()
                        print('Estimado {}', after-now)
                    
                    
                elif index_n_symbols == 2:
                    index_4_symbols_type_of_modulation = self.ui.modBox_2.currentIndex()
                    n_symbol = 4
                    if index_4_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_4_symbols_type_of_modulation != 0:
                        now = time.time()
                        #Creo la constelación
                        constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_4_symbols_type_of_modulation)
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
                        
                        for packet_symbols in symbols_to_send:
                            self.sdr.tx(packet_symbols)
                        print("ENVIANDO")
                        print(int_message)
                        after = time.time()
                        print('Estimado {}', after-now)
                    
                elif index_n_symbols == 3:
                    index_8_symbols_type_of_modulation = self.ui.modBox_3.currentIndex()
                    n_symbol = 8
                    
                    if index_8_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_8_symbols_type_of_modulation != 0:
                    
                        if index_8_symbols_type_of_modulation == 1 or index_8_symbols_type_of_modulation == 2:
                        
                            #Creo la constelación
                            constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation)
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
                            now = time.time()
                            for packet_symbols in symbols_to_send:
                                self.sdr.tx(packet_symbols)
                            print("ENVIANDO")
                            #print(int_message[0:10])
                            #print(int_message[-10:])
                            after = time.time()
                            print('Estimado {}', after-now)
                            
                        elif index_8_symbols_type_of_modulation == 3:
                            if self.ui.radioButton_2.isChecked() == True:
                                index_variant_8 = 1
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
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
                                now = time.time()
                                for packet_symbols in symbols_to_send:
                                    self.sdr.tx(packet_symbols)
                                print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                after = time.time()
                                print('Estimado {}', after-now)
                                
                            elif self.ui.radioButton_3.isChecked() == True:
                                index_variant_8 = 2
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
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
                                now = time.time()
                                for packet_symbols in symbols_to_send:
                                    self.sdr.tx(packet_symbols)
                                print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                after = time.time()
                                print('Estimado {}', after-now)
                                
                            elif self.ui.radioButton_4.isChecked() == True:
                                index_variant_8 = 3
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_8_symbols_type_of_modulation, index_variant_8)
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
                                now = time.time()
                                for packet_symbols in symbols_to_send:
                                    self.sdr.tx(packet_symbols)
                                print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                after = time.time()
                                print('Estimado {}', after-now)
                            
                    
                elif index_n_symbols == 4:
                    index_16_symbols_type_of_modulation = self.ui.modBox_4.currentIndex()
                    n_symbol = 16
                    
                    if index_16_symbols_type_of_modulation == 0:
                        self.ui.simWarnTxt.setText("Hace falta definir el tipo de modulación correspondiente")
                    
                    elif index_16_symbols_type_of_modulation != 0:
                    
                        if index_16_symbols_type_of_modulation == 1:
                        
                            #Creo la constelación
                            constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation)
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
                            now = time.time()
                            for packet_symbols in symbols_to_send:
                                self.sdr.tx(packet_symbols)
                            print("ENVIANDO")
                            #print(int_message[0:10])
                            #print(int_message[-10:])
                            after = time.time()
                            print('Estimado {}', after-now)
                        
                        elif index_16_symbols_type_of_modulation == 2:
                            if self.ui.radioButton_5.isChecked() == True:
                                index_variant_16 = 1
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
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
                                now = time.time()
                                for packet_symbols in symbols_to_send:
                                    self.sdr.tx(packet_symbols)
                                print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                after = time.time()
                                print('Estimado {}', after-now)
                                
                            elif self.ui.radioButton_6.isChecked() == True:
                                index_variant_16 = 2
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
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
                                now = time.time()
                                for packet_symbols in symbols_to_send:
                                    self.sdr.tx(packet_symbols)
                                print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                after = time.time()
                                print('Estimado {}', after-now)

                            elif self.ui.radioButton_7.isChecked() == True:
                                index_variant_16 = 3
                                
                                #Creo la constelación
                                constellation = MainFunctions.create_constellation_tx(self, n_symbol, index_16_symbols_type_of_modulation, qam16_selector = index_variant_16)
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
                                now = time.time()
                                for packet_symbols in symbols_to_send:
                                    self.sdr.tx(packet_symbols)
                                print("ENVIANDO")
                                #print(int_message[0:10])
                                #print(int_message[-10:])
                                after = time.time()
                                print('Estimado {}', after-now)     
                    
            
        ############ CONSTELACIÓN DEFINIDA POR EL USUARIO (HACE FALTA AGREGAR LA OPCIÓN DE SI EL USUARIO NO ESCRIBE EN EL FORMATO QUE CORRESPONDE, LANZAR EL AVISO PARA QUE NO PUEDA TRASNMITIR Y AVISE AL USUARIO)
                      
            elif self.user_defined_const_flag == True:
                index_n_symbols = self.ui.simPBitBox_2.currentIndex()

                if index_n_symbols == 1:
                    base1 = self.ui.text_3.toPlainText() #BASE 1
                    base2 = self.ui.text_4.toPlainText() #BASE 2
                    try:
                        point1 = eval(base1) #Cuidado con los eval
                        point2 = eval(base2)
                        #Colocar condicional que verifique que lo ingresado sea un numero?????
                        constellation = MainFunctions.create_constellation_tx_user(self, 2, point1 = point1, point2 = point2)
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        self.ui.mSim.display(int(len(bits_array)))
                        symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)

                        for inx,packet in enumerate(symbols_to_send):
                            symbols_to_send[inx] = np.multiply(packet,2**14)

                        if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                            add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                            symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)

                        for packet_symbols in symbols_to_send:
                            self.sdr.tx(packet_symbols)
                            
                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguna de las bases escrita tiene un error. Por favor revise e intente otra vez")
                
                elif index_n_symbols == 2:
                    base1 = self.ui.text_5.toPlainText() #BASE 1
                    base2 = self.ui.text_7.toPlainText() #BASE 2
                    base3 = self.ui.text_8.toPlainText() #BASE 3
                    base4 = self.ui.text_9.toPlainText() #BASE 4

                    try:
                        point1=eval(base1)
                        point2=eval(base2)
                        point3=eval(base3)
                        point4=eval(base4)
                        #Colocar condicional para verificar que lo ingresado sea un numero??????
                        constellation = MainFunctions.create_constellation_tx_user(self, 4, point1 = point1, point2 = point2, point3=point3, point4=point4)
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        self.ui.mSim.display(int(len(bits_array)))
                        symbols_to_send = MainFunctions.define_parts(self, bits_array, tsim, fsample, n_sym_parts = 100)

                        for inx,packet in enumerate(symbols_to_send):
                            symbols_to_send[inx] = np.multiply(packet,2**14)

                        if len(symbols_to_send[len(symbols_to_send)-1]) < len(symbols_to_send[0]):
                            add_zeros = np.zeros(len(symbols_to_send[0]) - len(symbols_to_send[len(symbols_to_send)-1]), dtype=complex)
                            symbols_to_send[len(symbols_to_send)-1] = np.append(symbols_to_send[len(symbols_to_send)-1], add_zeros)

                        for packet_symbols in symbols_to_send:
                            self.sdr.tx(packet_symbols)

                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguna de las bases escrita tiene un error. Por favor revise e intente otra vez")
        


    def graph_modulated_signal_prev(self):
        fsample = self.fsample
        self.ui.simWarnTxt.setText("")
    
        fsim = self.ui.fbit.value()
        tsim = self.ui.tbit.value()
        fport = self.ui.fport.value()
        
        
        if self.text_flag_message == True:
            message = self.ui.text.toPlainText()
        if self.filepath_flag_message == True:
            message = np.fromfile(self.filePath[0], dtype=bool)
        
        if message == "":
            self.ui.simWarnTxt.setText("Hace falta definir al mensaje")
        
        if message != "":
            
        ############# MODULACIÓN Y CONSTELACIONES PREDEFINIDAS  ---------------------- ACA SYMBOLS TO SEND AL PULSE SHAPING           
#            if self.defined_const_flag == False or self.user_defined_const_flag == False:
#                self.ui.simWarnTxt.setText("Hace falta definir el modo de configuración de la señal")

            if self.defined_const_flag == True:
                index_n_symbols = self.ui.simPBitBox.currentIndex()
                if index_n_symbols == 0:
                    self.ui.simWarnTxt.setText("Hace falta definir el número de simbolos por bit y tipo de modulación correspondiente")
                
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

                if index_n_symbols == 1:
                    base1 = self.ui.text_3.toPlainText()
                    base2 = self.ui.text_4.toPlainText()
                    try:
                        point1 = eval(base1) #Cuidado con los eval
                        point2 = eval(base2)
                        #Colocar condicional que verifique que lo ingresado sea un numero?????
                        constellation = MainFunctions.create_constellation_tx_user(self, 2, point1 = point1, point2 = point2)
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        self.ui.mSim.display(int(len(bits_array)))
                        symbols_to_send = MainFunctions.pulse_shape(self, bits_array, tsim, fsample, n_sym_parts = 100)
                        
                        MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)
                            
                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguna de las bases escrita tiene un error. Por favor revise e intente otra vez")
                
                elif index_n_symbols == 2:
                    base1 = self.ui.text_5.toPlainText()
                    base2 = self.ui.text_7.toPlainText()
                    base3 = self.ui.text_8.toPlainText()
                    base4 = self.ui.text_9.toPlainText()

                    try:
                        point1=eval(base1)
                        point2=eval(base2)
                        point3=eval(base3)
                        point4=eval(base4)
                        #Colocar condicional para verificar que lo ingresado sea un numero??????
                        constellation = MainFunctions.create_constellation_tx_user(self, 4, point1 = point1, point2 = point2, point3=point3, point4=point4)
                        bits_array = MainFunctions.prepare_to_send(self, message, n_symbol, constellation)
                        self.ui.mSim.display(int(len(bits_array)))
                        symbols_to_send = MainFunctions.pulse_shape(self, bits_array, tsim, fsample, n_sym_parts = 100)
                        
                        MainFunctions.graph_signal(self, constellation, symbols_to_send, tsim, fsample)

                    except:
                        print("VUELVA A INGRESAR") #Cambiar por aviso en interfaz
                        self.ui.simWarnTxt.setText("Alguna de las bases escrita tiene un error. Por favor revise e intente otra vez")

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
        MainFunctions.graph_original_bits(self)     
        

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
        filePath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open file', 'C:\\')
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
                self.ui.codelineBox_4.setCurrentIndex(0)
                self.ui.codelineBox_3.setCurrentIndex(0)
                self.ui.codelineBox_2.setCurrentIndex(0)

      
    def add_threshold(self):
        if self.add_threshold_page_flag == False: 
            self.add_threshold_page_flag = True
            MainFunctions.user_threshold_add(self, 100, True)
        
    def no_add_threshold(self):
        if self.add_threshold_page_flag == True:
            self.add_threshold_page_flag = False
            MainFunctions.user_threshold_add(self, 100, True)
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_25)
            self.ui.codelineBox_2.setCurrentIndex(0)
            
    def add_threshold_2_symbols(self, index):

        if index == 0 and self.add_threshold_2_symbols_flag == True:
            self.add_threshold_2_symbols_flag = False
            
        if index == 1:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_20)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
         
        if index == 2:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_21)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
            
        if index == 3:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_22)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
            
        if index == 4:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_23)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
            
        if index == 5:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_24)
            if self.add_threshold_2_symbols_flag == False:
                self.add_threshold_2_symbols_flag = True
                        
        
    def add_threshold_4_symbols(self, index):

        if index == 0 and self.add_threshold_4_symbols_flag == True:
            self.add_threshold_4_symbols_flag = False
            
        if index == 1:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_20)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True
         
        if index == 2:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_21)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True
                
        if index == 3:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_22)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True
            
        if index == 4:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_23)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True    
        
        if index == 5:
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_24)
            if self.add_threshold_4_symbols_flag == False:
                self.add_threshold_4_symbols_flag = True

        
    def add_threshold_4_symbols_2(self, index):
        
        if index == 0 and self.add_threshold_4_symbols_2_flag == True:
            self.add_threshold_4_symbols_2_flag = False

        if index == 1:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_15)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True
                 
        if index == 2:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_16)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True
            
        if index == 3:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_17)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True

        if index == 4:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_19)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True            
            
        if index == 5:
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_18)
            if self.add_threshold_4_symbols_2_flag == False:
                self.add_threshold_4_symbols_2_flag = True 
        
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    app.setWindowIcon(QtGui.QIcon(r'C:/Users/edmun/Desktop/Programas/QT pruebas/Principal/prof_blue.png'))
    window.setWindowIcon(QtGui.QIcon (r'C:/Users/edmun/Desktop/Programas/QT pruebas/Principal/prof_blue.png'))
    
    sys.exit(app.exec_())
    
    
    
