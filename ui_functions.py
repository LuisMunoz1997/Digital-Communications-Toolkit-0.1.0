

from main import *


class MainFunctions(MainWindow):
    
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.leftMenuSubContainer.width()
            maxExtend = maxWidth
            standard = 55

            # SET MAX WIDTH
            if width == 55:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuSubContainer, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
    def info(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.centerMenuSubContaniner.width()
            maxExtend = maxWidth
            standard = 0
            
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.centerMenuSubContaniner, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


    def info_2(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.centerMenuSubContaniner_2.width()
            maxExtend = maxWidth
            standard = 0
            
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.centerMenuSubContaniner_2, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
    def format_rec(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget_6.height()
            maxExtend = maxWidth
            standard = 0
            
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget_6, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def symbols_rec(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget.height()
            maxExtend = maxWidth
            standard = 0
            
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def defined_threshold_rec(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget_7.height()
            maxExtend = maxWidth
            standard = 0
            
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget_7, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def user_defined_threshold_rec(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget_2.height()
            maxExtend = maxWidth
            standard = 0
            
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget_2, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


    def user_threshold_add_data_1(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget_11.height()
            maxExtend = maxWidth
            standard = 0
            
            if self.user_threshold_add_data_1_flag == False:
                self.user_threshold_add_data_1_flag = True
            else:
                self.user_threshold_add_data_1_flag = False
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget_11, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


    def number_of_symbols_transmition(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget_3.height()
            maxExtend = maxWidth
            standard = 0
            
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget_3, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def type_of_modulation(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget.height()
            maxExtend = maxWidth
            standard = 0
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

               
    def user_defined_const(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget_4.height()
            maxExtend = maxWidth
            standard = 0
            
            if self.user_defined_const_complex_motion_flag == False:
                self.user_defined_const_complex_motion_flag = True
            else:
                self.user_defined_const_complex_motion_flag = False
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget_4, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def transmit_motion_btn(self, maxWidth, enable):
        if enable:

            # GET HEIGHT
            width = self.ui.widget_5.height()
            maxExtend = maxWidth
            standard = 0
            
            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

                    
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.widget_5, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            

#######################################################################################################################################


    #Método recibir numero de simbolos, esquema ---> graficar constelación y retornar constelacion para posterior preparación de señal a enviar
    def create_constellation_tx(self, nsimb,esquema, qam8_selector = 1, qam16_selector = 1): 
        if nsimb == 2: #ask 1, ook 2, bpsk 3, fsk 4
            if esquema == 1: #ASK
                constellation = np.array([1+0j,2+0j]) #El orden es bit 0 y bit 1
            elif esquema == 2: #OOK
                constellation = np.array([0+0j, 1+0j])
            elif esquema == 3: #BPSK
                constellation = np.array([-1+0j, 1+0j])
            elif esquema == 4: #FSK. ESTA CONSTELACION ES REFERENCIA, SE TIENEN QUE GENERAR OTRAS MUESTRAS IQ PARA ESTA MODULACIÓN
                constellation = np.array([1+0j, 0+1j])
            else:
                print("ERROR SELECCIÓN")
        elif nsimb == 4: #4ask 1, qpsk 2, qpsk_ejes 3. #SE PODRIA AGREGAR ASK BIPOLAR QUIZAS
            if esquema == 3: #4ASK
                constellation = np.array([1+0j, 2+0j, 3+0j, 4+0j]) # El orden es 00, 01, 10, 11 
            elif esquema == 2: #QPSK
                constellation = np.array([-1-1j, -1+1j, 1-1j, 1+1j])
            elif esquema == 1: #QPSK_EJES
                constellation = np.array([-1+0j, 1+0j, 0-1j, 0+1j])
            else:
                print("ERROR SELECCIÓN")
        elif nsimb == 8: #8ask 1, 8psk 2, 8qam 3.
            if esquema == 1: #8ASK BIPOLAR #ORDEN 111, 110, 010, 011, 001, 000, 100, 101
                constellation = np.array([2+0j, 1+0j, -1+0j, -2+0j, -3+0j, -4+0j, 4+0j, 3+0j])
            elif esquema == 2: #8PSK    #ORDEN 111, 110, 010, 011, 001, 000, 100, 101
                psk8_domain= np.arange(0,8)
                constellation = np.exp(2j*np.pi*psk8_domain/8)
            elif esquema == 3: #8QAM VARIANTES
                if qam8_selector == 1: #8QAM "RECTANGULAR"
                    constellation = np.array([1-1j, 1+1j, -1+1j, -1-1j, -3-1j, -3+1j, 3+1j, 3-1j])
                elif qam8_selector == 2: #8QAM CIRCULAR
                    constellation = np.array([-1-1j, -1-np.sqrt(3)+0j, -1+1j, 0+(1+np.sqrt(3))*1j, 1+1j, 1+np.sqrt(3)+0j, 1-1j, 0-(1+np.sqrt(3))*1j])
                elif qam8_selector == 3: #8QAM DIAGONAL
                    constellation = np.array([3+3j, 1+1j, 1-1j, 3-3j, -3-3j, -1-1j, -1+1j, -3+3j])
                else:
                    print("ERROR SELECCIÓN")
            else:
                print("ERROR SELECCIÓN")
        elif nsimb == 16:  #16PSK 1, 16QAM 1 3 variantes
            if esquema == 1: #16PSK
                psk16_domain= np.arange(0,16)
                constellation = 1*np.exp(2j*np.pi*psk16_domain/16)
                #ORDEN 0000, 1000, 1001, 1011, 1010, 1110, 1111, 1101, 1100, 0100, 0101, 0111, 0110, 0010, 0011, 0001
            elif esquema == 2:
                if qam16_selector == 1: #16QAM RECTANGULAR
                    constellation = np.array([-3+3j, 3+3j, 3+1j, 3-1j, 3-3j, 1-3j, 1-1j, 1+1j, 1+3j, -1+3j, -1+1j, -1-1j, -1-3j, -3-3j, -3-1j, -3+1j])
                    #ORDEN 0000, 1000, 1001, 1011, 1010, 1110, 1111, 1101, 1100, 0100, 0101, 0111, 0110, 0010, 0011, 0001
                elif qam16_selector == 2: #16QAM CIRCULAR
                    qam16_circular_domain= np.arange(0,4)
                    qam16_r1 = np.exp(2j*np.pi*qam16_circular_domain/4)
                    qam16_r2 = 2*np.exp(2j*np.pi*qam16_circular_domain/4) * np.exp(1j*np.pi/4)
                    qam16_r3 = 3*np.exp(2j*np.pi*qam16_circular_domain/4)
                    qam16_r4 = 4*np.exp(2j*np.pi*qam16_circular_domain/4) * np.exp(1j*np.pi/4)
                    constellation = np.append(qam16_r1, qam16_r2)
                    constellation = np.append(constellation,qam16_r3)
                    constellation =np.append(constellation, qam16_r4)
                    #ORDEN 0000, 1000, 1001, 1011, 1010, 1110, 1111, 1101, 1100, 0100, 0101, 0111, 0110, 0010, 0011, 0001
                    constellation = np.array([
                        -1+0j, -1.414214-1.414214j, -2.828427-2.828427j, -2.828427+2.828427j,
                        -1.414214+1.414214j, 1.414214-1.414214j, 2.828427-2.828427j, 2.828427+2.828427j,
                        1.414214+1.414214j, 1+0j, 3+0j, 0-3j,
                        0-1j, 0+1j, 0+3j, -3+0j
                    ])
                    
                elif qam16_selector == 3: #16QAM ESTRELLA
                    qam16_star_domain= np.arange(0,8)
                    qam16_star_int = np.exp(2j*np.pi*qam16_star_domain/8)
                    qam16_star_ext = 2*np.exp(2j*np.pi*qam16_star_domain/8)
                    constellation = np.append(qam16_star_int,qam16_star_ext)
                    #ORDEN 0000, 1000, 1001, 1011, 1010, 1110, 1111, 1101, 1100, 0100, 0101, 0111, 0110, 0010, 0011, 0001
                    constellation = np.array([
                        1+0j, 0.70711-0.70711j, 1.41421-1.41421j, -2+0j,
                        -1+0j, -0.70711-0.70711j, -1.41421-1.41421j, 0-2j,
                        0-1j, 0.70711+0.70711j, 1.41421+1.41421j, 0+2j,
                        0+1j, -0.70711+0.70711j, -1.41421+1.41421j, 2+0j
                    ])
                    
                else:
                    print("ERROR SELECCIÓN")
            else:
                print("ERROR SELECCIÓN")
        else:
            print("ERROR SELECCIÓN")
        
        return constellation

    #Método asignar bits a un símbolo de la constelación. Retorna arreglo con simbolos. La conversión a "bits" se hace con npbromfile dtype bool
    def prepare_to_send(self, message, nsimb, constellation):
        #Qué pasa si envío 3 bits por simbolo, y resulta que en los ultimos bits a enviar solo me faltan 2 o 1? Por no ser par
        #Acá si se quiere no se trabaja con nsimb sino con len(constellation)
        #Si el mensaje no es de np.fromfile dtype=bool, es string, convierto a bits sin comprimir, o buscar forma de comprimir.
        if type(message)is str:
            message = MainFunctions.string_to_bits(self, message)

        if nsimb == 2:
            bits_condition = [~(message), (message)] #Bit 0, Bit 1
            bits_save = [constellation[0], constellation[1]] #Simbolo a bit 1, Simbolo a bit 0
            bits_array = np.select(bits_condition, bits_save, default=None)
        
        elif nsimb == 4: #Orden indices constellation 00, 01, 10, 11
            message = message.reshape(-1, 2)
            bits_condition = [~(message[:,0])&~(message[:,1]), ~(message[:,0])&(message[:,1]), (message[:,0])&~(message[:,1]), (message[:,0])&(message[:,1])] #00, 01, 10, 11
            bits_save = [constellation[0], constellation[1], constellation[2], constellation[3]]
            bits_array = np.select(bits_condition, bits_save, default=None)

        elif nsimb == 8: #ORDEN 111, 110, 010, 011, 001, 000, 100, 101
            message = message.reshape(-1, 3)
            bits_condition = [
                message[:,0] & message[:,1] & message[:,2], #111
                message[:,0] & message[:,1] & ~message[:,2], #110
                ~message[:,0] & message[:,1] & ~message[:,2], #010
                ~message[:,0] & message[:,1] & message[:,2], #011
                ~message[:,0] & ~message[:,1] & message[:,2], #001
                ~message[:,0] & ~message[:,1] & ~message[:,2], #000
                message[:,0] & ~message[:,1] & ~message[:,2], #100
                message[:,0] & ~message[:,1] & message[:,2], #101
            ]
            bits_save = [
                constellation[0],
                constellation[1],
                constellation[2],
                constellation[3],
                constellation[4],
                constellation[5],
                constellation[6],
                constellation[7],
            ]
            bits_array= np.select(bits_condition, bits_save, default=None)
        
        elif nsimb == 16:
            #ORDEN 0000, 1000, 1001, 1011, 1010, 1110, 1111, 1101, 1100, 0100, 0101, 0111, 0110, 0010, 0011, 0001
            message = message.reshape(-1,4)
            bits_condition = [
                ~message[:,0] & ~message[:,1] & ~message[:,2] & ~message[:,3], #0000
                message[:,0] & ~message[:,1] & ~message[:,2] & ~message[:,3], #1000
                message[:,0] & ~message[:,1] & ~message[:,2] & message[:,3], #1001
                message[:,0] & ~message[:,1] & message[:,2] & message[:,3], #1011
                message[:,0] & ~message[:,1] & message[:,2] & ~message[:,3], #1010
                message[:,0] & message[:,1] & message[:,2] & ~message[:,3], #1110
                message[:,0] & message[:,1] & message[:,2] & message[:,3], #1111
                message[:,0] & message[:,1] & ~message[:,2] & message[:,3], #1101
                message[:,0] & message[:,1] & ~message[:,2] & ~message[:,3], #1100
                ~message[:,0] & message[:,1] & ~message[:,2] & ~message[:,3], #0100
                ~message[:,0] & message[:,1] & ~message[:,2] & message[:,3], #0101
                ~message[:,0] & message[:,1] & message[:,2] & message[:,3], #0111
                ~message[:,0] & message[:,1] & message[:,2] & ~message[:,3], #0110
                ~message[:,0] & ~message[:,1] & message[:,2] & ~message[:,3], #0010
                ~message[:,0] & ~message[:,1] & message[:,2] & message[:,3], #0011
                ~message[:,0] & ~message[:,1] & ~message[:,2] & message[:,3], #0001
            ]
            bits_save = [
                constellation[0],
                constellation[1],
                constellation[2],
                constellation[3],
                constellation[4],
                constellation[5],
                constellation[6],
                constellation[7],
                constellation[8],
                constellation[9],
                constellation[10],
                constellation[11],
                constellation[12],
                constellation[13],
                constellation[14],
                constellation[15],
            ]
            bits_array= np.select(bits_condition, bits_save, default=20+20j)

        return bits_array

#Recibe tsimb, fsample, simbolos a graficar y retorna dominio para graficar y la señal modulada a graficar (no enviar)
    def plot_modulated(self, tsimb, fsample, signal):
        n_per_symbol = int(fsample*tsimb)
        n_graph = n_per_symbol*20 #Graficar solo primeros 20 simbolos
        t = np.arange(len(signal)) / fsample
        #if len(t) > len(signal):
        #    t = t[:-1] #Cosas del redondeo, se quita 1 muestra a t si es mayor a la de signal 
        fsimb = (1/tsimb)
        fc = 3*fsimb
        print("FSIMB ES:", fsimb)
        print("FC ES:", fc)
        print("FSAMPLES ES:",fsample)
        modulated = np.cos(2*np.pi*fc*t)[:n_graph] * signal.real[:n_graph] + np.sin(2*np.pi*fc*t)[:n_graph] * signal.imag[:n_graph]
        print("\n")
        print(len(modulated))
        print(len(t))
    
        return t[:n_graph], modulated


    def add_tsimb(self, tsimb, fsample, bits_array): #Puede recibir tsimb o fsimb
        repeat = int(fsample*tsimb)
        print("Muestras por símbolo: ", repeat)
        print("Cantidad de símbolos ", len(bits_array))
        
        self.ui.mSim.display(int(len(bits_array)/repeat))
        
        return np.repeat(bits_array,repeat)

    def pulse_shape(self, samples_symbols, tsim, fsample, beta=0.35):
        #print('tsim en shape es:', tsim)
        #print('samples symbols tiene:', len(samples_symbols))
        sps = int(fsample * tsim)
        #print('sps calculado en shape es:', sps)
        samples = np.array([], dtype=complex)
        for bit in samples_symbols:
            pulse = np.zeros(sps, dtype=complex)
            try:
                pulse[0] = bit
            except:
                self.ui.simWarnTxt.setText("Hace falta definir tsim y fsim")
                self.ui.mSim.display(0)
    
            samples = np.concatenate((samples, pulse))
    
        num_symbols = len(samples_symbols)
        num_taps = sps * num_symbols
        #print('Len samples es:', len(samples))
        #print('num_taps es:', num_taps)
        Ts = sps / fsample
        t = np.arange(num_taps) * Ts - (num_taps - 1) * Ts / 2
        
        h = rrcosfilter(num_taps, alpha=beta, Ts=sps/fsample, Fs = fsample)[1]
    
        shaped = np.convolve(samples,h,mode='same')

        return shaped
        
    def add_preamble(self,samples, fsample = 522000, freq = 80e3, n_samples = 100):
        preambulo = 1*np.exp(2j*np.pi*freq*np.arange(n_samples) / fsample) #Esto estaba antes en 0.5
        return np.append(preambulo,samples)

    #Dividir por partes la señal a enviar. Cada parte con su preámbulo. Se divide por cantidad de símbolos.
    def define_parts(self, samples_symbols, tsim, fsample, n_sym_parts = 100): #Recibe los pulsos de los simbolos sin añadir tiempo simb creo
        #Crea arreglo que cada volumna contiene un arreglo que representa la parte a enviar
        packets = np.split(samples_symbols, np.arange(n_sym_parts,len(samples_symbols),n_sym_parts))
        
        #Por cada parte, se realiza el pulse shape y se le agrega un preambulo. Se prueba con 1 solo preambulo con duration tsimb tambien a ver.
        for inx,part in enumerate(packets):
             print('Preparing part {} of {}'.format(inx, len(packets)-1))
             packets[inx] = MainFunctions.add_preamble(self,MainFunctions.pulse_shape(self, part, tsim, fsample, beta=0.35), fsample = 522000, freq = 80e3, n_samples = 100)
            
        return packets
    
    #CUSTOM TX and RX - Crea constelacion con información de fase y cuadratura dada por usuario.
    def create_constellation_tx_user(self, nsimb, point1 = 0, point2 = 0, point3 = 0, point4 = 0):
        if nsimb == 2:
            constellation = np.array([point1,point2])
        elif nsimb == 4:
            constellation = np.array([point1,point2,point3,point4])
        else:
            print("ERROR CREACION CONSTELACION USUARIO")
        return constellation
    
    #Método TX para normalizar símbolos en constelación antes de pulse shape y prepare to send, antes de enviarlos al Pluto. Entra la constelación apenas creada en TX
    def normalize_constellation(self, constellation):
        factor_real = np.max(abs(constellation.real))
        factor_imag = np.max(abs(constellation.imag))
        if factor_real != 0:
            constellation.real = constellation.real / factor_real
        else:
            constellation.real = constellation.real
        if factor_imag != 0:
            constellation.imag = constellation.imag / factor_imag
        else:
            constellation.imag = constellation.imag
        return constellation
           
    
    #Método para pasar string a bits arreglo
    def string_to_bits(self, message):
        message = message.encode('utf-8')
        message = np.frombuffer(message, dtype=np.uint8)
        message = np.unpackbits(message)
        message = np.asarray(message, dtype=bool)
        return message

                       
    def graph_original_bits(self, bits, fs, amplitude, codeline, index_n_symbol, tsim):

        if index_n_symbol == 1:
            n_bits = 1
        if index_n_symbol == 2:
            n_bits = 2
        if index_n_symbol == 3:
            n_bits = 3
        if index_n_symbol == 4:
            n_bits = 4

        tbit = tsim / n_bits

        spb = int(tbit * fs)

        clk = np.arange(0, len(bits)) % 2 # clock samples
        clk_sequence = np.repeat(clk, spb)

        data_sequence = np.repeat(bits, spb) #Basic bits
        t = np.arange(len(data_sequence)) / fs

        if codeline == 0:
            MainFunctions.graph_widget_setting(self, data_sequence, t, tbit)

        elif codeline == 1:
            unipolar_nrz = amplitude * data_sequence #Unipolar non-return-to-zero level
            MainFunctions.graph_widget_setting(self, unipolar_nrz, t, tbit)

        elif codeline == 2:
            nrz_bipolar = amplitude * (2 * data_sequence - 1) #Bipolar Non-return-to-zero level
            MainFunctions.graph_widget_setting(self, nrz_bipolar, t, tbit)

        elif codeline == 3:
            unipolar_rz = amplitude * (data_sequence * (1 - clk_sequence)) #Unipolar return-to-zero
            MainFunctions.graph_widget_setting(self, unipolar_rz, t, tbit)

        elif codeline == 4:
            rz_bipolar = amplitude * (data_sequence * (1 - clk_sequence) - 0.5) #Unipolar return-to-zero
            MainFunctions.graph_widget_setting(self, rz_bipolar, t, tbit)


        elif codeline == 5:
            ami = 1 * bits
            previousOne = 0 

            for i in range(0,len(bits)):

                if (ami[i]==1) and (previousOne==0):
                    ami[i] = amplitude
                    previousOne=1
                
                if (ami[i]==1) and (previousOne==1):
                    ami[i]= -amplitude
                    previousOne = 0

            ami_sequence = np.repeat(ami, spb) #Alternate Mark Inversion (AMI)
            MainFunctions.graph_widget_setting(self, ami_sequence, t, tbit)


        elif codeline == 6:
            manchester_encoded = amplitude * (2 * np.logical_xor(data_sequence,clk_sequence).astype(int) - 1) #Manchester Encoded - IEEE 802.3
            MainFunctions.graph_widget_setting(self, manchester_encoded, t, tbit)


    def graph_widget_setting(self, coded_bits, t, tbit):

        if self.BB_graph_flag == False:
            self.BB_graph_flag = True

            self.grafica = plt_bits_coded(coded_bits, t, tbit) #Banda Base
            self.toolbar = NavigationToolbar(self.grafica, self)

            self.ui.prevPBlayout.addWidget(self.grafica)
            self.ui.prevPBlayout.addWidget(self.toolbar)

        else:
            self.ui.prevPBlayout.itemAt(0).widget().deleteLater()
            self.ui.prevPBlayout.itemAt(1).widget().deleteLater()

            self.grafica = plt_bits_coded(coded_bits, t, tbit) #Banda Base
            self.toolbar = NavigationToolbar(self.grafica, self)

            self.ui.prevPBlayout.addWidget(self.grafica)
            self.ui.prevPBlayout.addWidget(self.toolbar)

                     
                        
    def graph_signal(self, constellation, symbols, tsim, fsample):    

        if self.signal_graph_flag == False:
            self.signal_graph_flag = True
            
            t1 = np.arange(len(symbols)) / fsample  

            #estimated_time = (len(symbols) / fsample)
            #t1 = np.arange(0, estimated_time, 1/fsample)
            #if len(t1) > len(symbols):
            #    t1 = t1[:-1]
            
            t2, modulated = MainFunctions.plot_modulated(self, tsim, fsample, symbols)
            

            self.grafica1 = plt_modulated_signal2(t1, symbols.real, t1, symbols.imag) #Banda Base IQ with pulse Shaping
            self.toolbar1 = NavigationToolbar(self.grafica1, self)
            
            self.grafica2 = plt_modulated_signal(symbols, fsample) #DEP 
            self.toolbar2 = NavigationToolbar(self.grafica2, self)

            self.grafica3 = plt_modulated_signal3(constellation.real, constellation.imag) #Constelacion
            self.toolbar3 = NavigationToolbar(self.grafica3, self)
            
            self.grafica4 = plt_modulated_signal4(t2, modulated) #Modulada al aire referencia
            self.toolbar4 = NavigationToolbar(self.grafica4, self)
            
            self.ui.prevBBlayout.addWidget(self.grafica1)
            self.ui.prevBBlayout.addWidget(self.toolbar1)
            self.ui.prevDEPlayout.addWidget(self.grafica2)
            self.ui.prevDEPlayout.addWidget(self.toolbar2)
            self.ui.prevConstlayout.addWidget(self.grafica3)
            self.ui.prevConstlayout.addWidget(self.toolbar3)
            self.ui.prevMSlayout.addWidget(self.grafica4)
            self.ui.prevMSlayout.addWidget(self.toolbar4)
            
        else:
            self.ui.prevBBlayout.itemAt(0).widget().deleteLater()
            self.ui.prevBBlayout.itemAt(1).widget().deleteLater()    
            #self.ui.prevBBlayout.removeWidget(self.grafica1)
            #self.ui.prevBBlayout.removeWidget(self.toolbar1)

            self.ui.prevDEPlayout.itemAt(0).widget().deleteLater()
            self.ui.prevDEPlayout.itemAt(1).widget().deleteLater()
            #self.ui.prevDEPlayout.removeWidget(self.grafica2)
            #self.ui.prevDEPlayout.removeWidget(self.toolbar2)

            self.ui.prevConstlayout.itemAt(0).widget().deleteLater()
            self.ui.prevConstlayout.itemAt(1).widget().deleteLater()
            #self.ui.prevConstlayout.removeWidget(self.grafica3)
            #self.ui.prevConstlayout.removeWidget(self.toolbar3)

            self.ui.prevMSlayout.itemAt(0).widget().deleteLater()
            self.ui.prevMSlayout.itemAt(1).widget().deleteLater()
            #self.ui.prevMSlayout.removeWidget(self.grafica4)
            #self.ui.prevMSlayout.removeWidget(self.toolbar4)
            
            
            #estimated_time = (len(symbols) / fsample)
            #t1 = np.arange(0, estimated_time, 1/fsample)
            #if len(t1) > len(symbols):
            #    t1 = t1[:-1]
            
            t1 = np.arange(len(symbols)) / fsample

            t2, modulated = MainFunctions.plot_modulated(self, tsim, fsample, symbols)
            
            
            self.grafica1 = plt_modulated_signal2(t1, symbols.real, t1, symbols.imag)
            self.toolbar1 = NavigationToolbar(self.grafica1, self)
            
            self.grafica2 = plt_modulated_signal(symbols, fsample)
            self.toolbar2 = NavigationToolbar(self.grafica2, self)

            self.grafica3 = plt_modulated_signal3(constellation.real, constellation.imag) 
            self.toolbar3 = NavigationToolbar(self.grafica3, self)
            
            self.grafica4 = plt_modulated_signal4(t2, modulated) 
            self.toolbar4 = NavigationToolbar(self.grafica4, self)
            
            self.ui.prevBBlayout.addWidget(self.grafica1)
            self.ui.prevBBlayout.addWidget(self.toolbar1)
            self.ui.prevDEPlayout.addWidget(self.grafica2)
            self.ui.prevDEPlayout.addWidget(self.toolbar2)
            self.ui.prevConstlayout.addWidget(self.grafica3)
            self.ui.prevConstlayout.addWidget(self.toolbar3)
            self.ui.prevMSlayout.addWidget(self.grafica4)
            self.ui.prevMSlayout.addWidget(self.toolbar4)    
        

    def slope(self, a):
        radians = a*np.pi/180
        return np.tan(radians)
    
    def threshold_defined(self, nsimb, esquema): #Amplificador en algunos casos suma y en otros multiplica
        real_domain = np.linspace(-20,20,num=2, dtype=complex) #Dominios real e imag
        imag_domain = np.linspace(-20j,20j,num=2, dtype=complex) #Para simular la formula y = mx + c de cierta forma
        real_circle = np.linspace(0,1, num=16, dtype=complex)

        if nsimb == 2: # 1 Pendiente, 2 X y 3 Y
            if esquema == 4: #Inclinada 
                umbral1 = imag_domain * MainFunctions.slope(self, 45) + real_domain
            elif esquema == 5: #Horizontal
                umbral1 = imag_domain * 0 + real_domain
            elif esquema == 3: #Vertical, sirve para BPSK
                umbral1 = imag_domain + real_domain * 0
            elif esquema == 1: #Para 2ASK
                umbral1 = imag_domain + real_domain * 0 + 1.5
            elif esquema == 2: #Para OOK
                umbral1 = imag_domain + real_domain * 0 + 0.5
            else:
                print("ERROR SELECCIÓN")
            umbrales = np.array([umbral1])
        
        elif nsimb == 4: #1 rectas 2 diagonales, 2 rectas 2 ejes
            if esquema == 1: #2 Diagonales - Se cambio numero esquema por correcion en define_regions y create constellation
                umbral1 = imag_domain * MainFunctions.slope(self, 45) + real_domain
                umbral2 = imag_domain * -MainFunctions.slope(self, 45) + real_domain
                umbrales = np.array([umbral1, umbral2])
            elif esquema == 2: #2 Rectas Ejes
                umbral1 = imag_domain * 0 + real_domain
                umbral2 = imag_domain + real_domain * 0
                umbrales = np.array([umbral1, umbral2])
            elif esquema == 3:  # AGREGAR OPCION UMBRALES ASK EN RX 4 NSIMB - Verificar porque escribi esto o si ya se corrigio
                umbral1 = imag_domain + real_domain * 0 + 1.5
                umbral2 = imag_domain + real_domain * 0 + 2.5
                umbral3 = imag_domain + real_domain * 0 + 3.5
                umbrales = np.array([umbral1, umbral2, umbral3])
            elif esquema == 4: #Para 4ASK
                umbral1 = imag_domain + real_domain * 0 + 1.5
                umbral2 = imag_domain + real_domain * 0 + 2.5
                umbral1 = imag_domain + real_domain * 0 + 3.5
                umbrales = np.array([umbral1, umbral2, umbral3])
            else:
                print("ERROR SELECCIÓN")
        
        elif nsimb == 8:
            if esquema == 1: #2 Diagonales y 1 Circulo
                umbral1 = imag_domain * 0 + real_domain
                umbral2 = imag_domain + real_domain * 0
                umbral3 = 2.5 * np.exp(2j*np.pi*real_circle) #Pendiente con los circulos y la detección
                umbrales = np.array([umbral1, umbral2, umbral3], dtype = object)
            elif esquema == 2: #4 Diagonales. Sirve para 8psk y un 8qam
                umbral1 = imag_domain * MainFunctions.slope(self, 45+22.5) + real_domain
                umbral2 = imag_domain * MainFunctions.slope(self, 45-22.5) + real_domain
                umbral3 = imag_domain * MainFunctions.slope(self, -45-22.5) + real_domain
                umbral4 = imag_domain * MainFunctions.slope(self, -45+22.5) + real_domain
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4])
            elif esquema == 3: #3 Horizontales 1 Vertical --------- NO ESTA EN TX
                umbral1 = imag_domain * 0 + real_domain
                umbral2 = imag_domain * 0 + real_domain + 2j
                umbral3 = imag_domain * 0 + real_domain - 2j
                umbral4 = imag_domain + real_domain * 0
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4])
            elif esquema == 4: #3 Verticales 1 Horizontal
                umbral1 = imag_domain + real_domain * 0
                umbral2 = imag_domain + real_domain * 0 + 2
                umbral3 = imag_domain + real_domain * 0 - 2
                umbral4 = imag_domain * 0 + real_domain
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4])
            elif esquema == 5: #Para 8ASK Bipolar
                umbral1 = imag_domain + real_domain * 0 + 1.5
                umbral2 = imag_domain + real_domain * 0 + 2.5
                umbral3 = imag_domain + real_domain * 0 + 3.5
                umbral4 = imag_domain + real_domain * 0 - 1.5
                umbral5 = imag_domain + real_domain * 0 - 2.5
                umbral6 = imag_domain + real_domain * 0 - 3.5
                umbral7 = imag_domain + real_domain * 0
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4, umbral5, umbral6, umbral7])
            else:
                print("ERROR SELECCIÓN")

        elif nsimb == 16:
            if esquema == 1: #8 Diagonales
                reference_domain_16 = np.arange(0,16)
                reference_16 = np.exp(2j*np.pi*reference_domain_16/16)
                angles_reference_16 = np.angle(reference_16, deg=True)
                umbral1 = imag_domain * MainFunctions.slope(self, angles_reference_16[1]+11.25) + real_domain #+11.25 de umbral para cada dirección, por simbolo
                umbral2 = imag_domain * MainFunctions.slope(self, angles_reference_16[1]-11.25) + real_domain
                umbral3 = imag_domain * MainFunctions.slope(self, angles_reference_16[3]+11.25) + real_domain
                umbral4 = imag_domain * MainFunctions.slope(self, angles_reference_16[3]-11.25) + real_domain
                umbral5 = imag_domain * MainFunctions.slope(self, angles_reference_16[5]+11.25) + real_domain
                umbral6 = imag_domain * MainFunctions.slope(self, angles_reference_16[5]-11.25) + real_domain
                umbral7 = imag_domain * MainFunctions.slope(self, angles_reference_16[7]+11.25) + real_domain
                umbral8 = imag_domain * MainFunctions.slope(self, angles_reference_16[7]-11.25) + real_domain            
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4, umbral5, umbral6, umbral7, umbral8])
            elif esquema == 2: #4 Diagonales 1 Circulo R=2.5
                reference_domain_16 = np.arange(0,8)
                reference_16 = np.exp(2j*np.pi*reference_domain_16/8)
                angles_reference_16 = np.angle(reference_16, deg=True)
                umbral1 = imag_domain * MainFunctions.slope(self, angles_reference_16[1]+22.5) + real_domain #+-22.5° de umbral
                umbral2 = imag_domain * MainFunctions.slope(self, angles_reference_16[1]-22.5) + real_domain
                umbral3 = imag_domain * MainFunctions.slope(self, angles_reference_16[3]+22.5) + real_domain
                umbral4 = imag_domain * MainFunctions.slope(self, angles_reference_16[3]-22.5) + real_domain
                umbral5 = 2.5 * np.exp(2j*np.pi*real_circle)
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4, umbral5], dtype=object)
            elif esquema == 3:
                reference_domain_16 = np.arange(0,8)
                reference_16 = np.exp(2j*np.pi*reference_domain_16/8)
                angles_reference_16 = np.angle(reference_16, deg=True)
                umbral1 = imag_domain * MainFunctions.slope(self, angles_reference_16[1]+22.5) + real_domain #+-22.5° de umbral
                umbral2 = imag_domain * MainFunctions.slope(self, angles_reference_16[1]-22.5) + real_domain
                umbral3 = imag_domain * MainFunctions.slope(self, angles_reference_16[3]+22.5) + real_domain
                umbral4 = imag_domain * MainFunctions.slope(self, angles_reference_16[3]-22.5) + real_domain
                umbral5 = 1.5 * np.exp(2j*np.pi*real_circle)
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4, umbral5], dtype=object)           
            elif esquema == 4: #3 Horizontales y 3 Verticales
                umbral1 = imag_domain * 0 + real_domain
                umbral2 = imag_domain * 0 + real_domain + 2j
                umbral3 = imag_domain * 0 + real_domain - 2j
                umbral4 = imag_domain + real_domain * 0
                umbral5 = imag_domain + real_domain * 0 + 2
                umbral6 = imag_domain + real_domain * 0 - 2
                umbrales = np.array([umbral1, umbral2, umbral3, umbral4, umbral5, umbral6])
            else:
                print("ERROR SELECCIÓN")
        return umbrales

    def is_inside_sm(self, polygon, point): #0 is outside, 1 is inside, 2 is in boundary
        length = len(polygon)
        dy2 = point.imag - polygon[0].imag
        intersections = 0
        ii = 0
        jj = 1

        while ii < length - 1:
            dy = dy2
            dy2 = point.imag - polygon[jj].imag

            # Consider only lines which are not completely above/below/right from the point
            if dy * dy2 <= 0.0 and (point.real >= polygon[ii].real or point.real >= polygon[jj].real):

                # Non-horizontal line
                if dy < 0 or dy2 < 0:
                    F = dy * (polygon[jj].real - polygon[ii].real) / (dy - dy2) + polygon[ii].real

                    if point.real > F:  # If line is left from the point - the ray moving towards left will intersect it
                        intersections += 1
                    elif point.real == F:  # Point on line
                        return 2

                # Point on upper peak (dy2=dx2=0) or horizontal line (dy=dy2=0 and dx*dx2<=0)
                elif dy2 == 0 and (point.real == polygon[jj].real or (dy == 0 and (point.real - polygon[ii].real) * (point.real - polygon[jj].real) <= 0)):
                    return 2

            ii = jj
            jj += 1

        # Check the intersection with the line formed by the last and first vertices
        dy = dy2
        dy2 = point.imag - polygon[0].imag

        # Consider only lines which are not completely above/below/right from the point
        if dy * dy2 <= 0.0 and (point.real >= polygon[-1].real or point.real >= polygon[0].real):
            F = dy * (polygon[0].real - polygon[-1].real) / (dy - dy2) + polygon[-1].real

            if point.real > F:  # If line is left from the point - the ray moving towards left will intersect it
                intersections += 1
            elif point.real == F:  # Point on line
                return 2

        # Handle the case where the last vertex is not connected to the first vertex
        if polygon[0] != polygon[-1]:
            # Check the intersection with the line formed by the last and first vertices
            dy = dy2
            dy2 = point.imag - polygon[-1].imag

            # Consider only lines which are not completely above/below/right from the point
            if dy * dy2 <= 0.0 and (point.real >= polygon[-1].real or point.real >= polygon[0].real):
                F = dy * (polygon[0].real - polygon[-1].real) / (dy - dy2) + polygon[-1].real

                if point.real > F:  # If line is left from the point - the ray moving towards left will intersect it
                    intersections += 1
                elif point.real == F:  # Point on line
                    return 2

        return intersections & 1

    def define_regions(self, nsimb, esquema):
        if nsimb == 2:
            if esquema == 1: #Regiones FSK
                regiones = [
                    'samples.imag < umbrales[0](samples.real)', #0
                    'samples.imag > umbrales[0](samples.real)', #1
                    ]
                bits_save = [
                        'False',
                        'True',
                    ]
            elif esquema ==2: #Regiones no Usadas de momento
                regiones = [
                    'samples.imag < umbrales[0](samples.real)', #0
                    'samples.imag > umbrales[0](samples.real)', #1
                    ]
                bits_save = [
                        '0',
                        '1',
                    ]
            elif esquema ==3: #Regiones BPSK
                regiones = [
                    'samples.real < umbrales_no[0][0].real', #0
                    'samples.real > umbrales_no[0][0].real', #1
                    ]
                bits_save = [
                        '0',
                        '1',
                    ]
            elif esquema ==4: # Regiones 2ASK
                regiones = [
                    'samples.real < umbrales_no[0][0].real', #0
                    'samples.real > umbrales_no[0][0].real', #1
                    ]
                bits_save = [
                        '0',
                        '1',
                    ]
                
        elif nsimb == 4:
            if esquema ==1:  #Regiones QPSK Ejes
                regiones = [
                    '(samples.real < 0) & (samples.imag > umbrales[0](samples.real)) & (samples.imag < umbrales[1](samples.real))', #00
                    '(samples.real > 0) & (samples.imag < umbrales[0](samples.real)) & (samples.imag > umbrales[1](samples.real))', #01
                    '(samples.imag < 0) & (samples.real > umbrales_i[0](samples.imag)) & (samples.real < umbrales_i[1](samples.imag))', #10
                    '(samples.imag > 0) & (samples.real < umbrales_i[0](samples.imag)) & (samples.real > umbrales_i[1](samples.imag))', #11
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
            elif esquema ==2: #Regiones QPSK
                regiones = [
                    '(samples.real < 0) & (samples.imag < 0)', #00
                    '(samples.real < 0) & (samples.imag > 0)', #01
                    '(samples.real > 0) & (samples.imag < 0)', #10
                    '(samples.real > 0) & (samples.imag > 0)', #11
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
            elif esquema ==3: # Regiones 4ASK, se corrigió a esquema 1, en create constellation está asi y si se cambia alli es cambio interfaz
                regiones = [
                    '(samples.real < 1.5)', #00
                    '(samples.real > 1.5) & (samples.real < 2.5)', #01
                    '(samples.real > 2.5) & (samples.imag < 3.5)', #10
                    '(samples.real > 4)', #11
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]

        elif nsimb == 8:
            if esquema ==1: #Regiones 8QAM Diagonal. En caso de circunferencia tengo que verificar antes el is_inside_sm
                regiones = [
                    '(samples.imag > 0) & (samples.real > 0) & ~(circle)', #111 3+3j
                    '(samples.imag > 0) & (samples.real > 0) & (circle)', #110 1+1j
                    '(samples.imag < 0) & (samples.real > 0) & (circle)', #010 1-1j
                    '(samples.imag < 0) & (samples.real > 0) & ~(circle)', #011 3-3j
                    '(samples.imag < 0) & (samples.real < 0) & ~(circle)', #001 -3-3j
                    '(samples.imag < 0) & (samples.real < 0) & (circle)', #000 -1-1j
                    '(samples.imag > 0) & (samples.real < 0) & (circle)', #100 -1+1j
                    '(samples.imag > 0) & (samples.real < 0) & ~(circle)', #101 -3+3j
                    ]
                bits_save = [
                    '111',
                    '110',
                    '010',
                    '011',
                    '001',
                    '000',
                    '100',
                    '101',     
                    ]
            elif esquema ==2: #Regiones para 8PSK. Sirven para un 8QAM pero sé si culpa código Gray este
                regiones = [
                        '(samples.real > 0) & (samples.imag < umbrales[1](samples.real)) & (samples.imag > umbrales[3](samples.real))', #111 1+0j
                        '(samples.real > 0) & (samples.imag < umbrales[0](samples.real)) & (samples.imag > umbrales[1](samples.real))', #110 0.7+0.7j
                        '(samples.imag > 0) & (samples.real < umbrales_i[0](samples.imag)) & (samples.real > umbrales_i[2](samples.imag))', #010 0+1j
                        '(samples.real < 0) & (samples.imag < umbrales[2](samples.real)) & (samples.imag > umbrales[3](samples.real))', #011 -0.7+0.7j
                        '(samples.real < 0) & (samples.imag < umbrales[3](samples.real)) & (samples.imag > umbrales[1](samples.real))', #001 -1+0j
                        '(samples.real < 0) & (samples.imag < umbrales[1](samples.real)) & (samples.imag > umbrales[0](samples.real))', #000 -0.7-0.7j
                        '(samples.imag < 0) & (samples.real < umbrales_i[2](samples.imag)) & (samples.real > umbrales_i[0](samples.imag))', #100 0-1j
                        '(samples.real > 0) & (samples.imag < umbrales[3](samples.real)) & (samples.imag > umbrales[2](samples.real))', #101 0.7-0.7j
                ]
                bits_save = [
                    '111',
                    '110',
                    '010',
                    '011',
                    '001',
                    '000',
                    '100',
                    '101',     
                    ]
            elif esquema == 3: #NO TIENE USO DE MOMENTO
                pass
            elif esquema == 4: #Regiones 8QAM Rectangular
                regiones = [
                    '(samples.real > 0) & (samples.real < umbral_no[1][0].real) & (samples.imag < 0)', #111 1-1j
                    '(samples.real > 0) & (samples.real < umbral_no[1][0].real) & (samples.imag > 0)', #110 1+1j
                    '(samples.real < 0) & (samples.real > umbral_no[2][0].real) & (samples.imag > 0)', #010 -1+1j
                    '(samples.real < 0) & (samples.real > umbral_no[2][0].real) & (samples.imag < 0)', #011 -1-1j
                    '(samples.real < umbrales_no[2][0].real) & (samples.imag < 0)', #001 -3-1j
                    '(samples.real < umbrales_no[2][0].real) & (samples.imag > 0)', #000 -3+1j
                    '(samples.real > umbrales_no[1][0].real) & (samples.imag > 0)', #100 3+1j
                    '(samples.real > umbrales_no[1][0].real) & (samples.imag < 0)', #101 3-1j
                ]
                bits_save = [
                    '111',
                    '110',
                    '010',
                    '011',
                    '001',
                    '000',
                    '100',
                    '101',     
                    ]
            elif esquema ==5: #Regiones 8ASK Bipolar
                regiones = [
                    '(samples.real > 1.5) & (samples.real < 2.5)', #111 2+0j
                    '(samples.real > 0) & (samples.real < 1.5)', #110 1+0j
                    '(samples.real > -1.5) & (samples.real < 0)', #010 -1+0j 
                    '(samples.real > -2.5) & (samples.real < -1.5)', #011 -2+0j 
                    '(samples.real > -3.5) & (samples.real < -2.5)', #001 -3+0j 
                    '(samples.real < -3.5)', #000 -4+0j
                    '(samples.real > 3.5)', #100 4+0j *
                    '(samples.real > 2.5) & (samples.real < 3.5)', #101 3+0j
                ]
                bits_save = [
                    '111',
                    '110',
                    '010',
                    '011',
                    '001',
                    '000',
                    '100',
                    '101',     
                    ]
        elif nsimb == 16:
            if esquema == 1: #Regiones 16PSK
                regiones = [
                        '(samples.real > 0) & (samples.imag < umbrales[1](samples.real)) & (samples.imag > umbrales[6](samples.real))', #0000 1+0j
                        '(samples.real > 0) & (samples.imag < umbrales[0](samples.real)) & (samples.imag > umbrales[1](samples.real))', #1000 0.9 + 0.3j
                        '(samples.real > 0) & (samples.imag < umbrales[3](samples.real)) & (samples.imag > umbrales[0](samples.real))', #1001 0.7+0.7j
                        '(samples.real > 0) & (samples.imag < umbrales[2](samples.real)) & (samples.imag > umbrales[3](samples.real))', #1011 0.3+0.9j
                        '(samples.imag > 0) & (samples.real < umbrales_i[2](samples.imag)) & (samples.real > umbrales_i[5](samples.imag))', #1010 0+1j
                        '(samples.real < 0) & (samples.imag < umbrales[5](samples.real)) & (samples.imag > umbrales[4](samples.real))', #1110 -0.3+0.9j
                        '(samples.real < 0) & (samples.imag < umbrales[4](samples.real)) & (samples.imag > umbrales[7](samples.real))', #1111 -0.7+0.7j
                        '(samples.real < 0) & (samples.imag < umbrales[7](samples.real)) & (samples.imag > umbrales[6](samples.real))', #1101 -0.9+0.3j
                        '(samples.real < 0) & (samples.imag < umbrales[6](samples.real)) & (samples.imag > umbrales[1](samples.real))', #1100 -1+0j
                        '(samples.real < 0) & (samples.imag < umbrales[1](samples.real)) & (samples.imag > umbrales[0](samples.real))', #0100 -0.9-0.3j
                        '(samples.real < 0) & (samples.imag < umbrales[0](samples.real)) & (samples.imag > umbrales[3](samples.real))', #0101 -0.7-0.7j
                        '(samples.real < 0) & (samples.imag < umbrales[3](samples.real)) & (samples.imag > umbrales[2](samples.real))', #0111 -0.3-0.9j
                        '(samples.imag < 0) & (samples.real < umbrales_i[5](samples.imag)) & (samples.real > umbrales_i[2](samples.imag))', #0110  0-1j
                        '(samples.real > 0) & (samples.imag < umbrales[4](samples.real)) & (samples.imag > umbrales[5](samples.real))', #0010 0.3-0.9j
                        '(samples.real > 0) & (samples.imag < umbrales[7](samples.real)) & (samples.imag > umbrales[4](samples.real))', #0011 0.7-0.7j
                        '(samples.real > 0) & (samples.imag < umbrales[6](samples.real)) & (samples.imag > umbrales[7](samples.real))', #0001 0.9-0.3j 
                ]
                bits_save = [
                        '0000',
                        '1000',
                        '1001',
                        '1011',
                        '1010',
                        '1110',
                        '1111',
                        '1101',
                        '1100',
                        '0100',
                        '0101',
                        '0111',
                        '0110',
                        '0010',
                        '0011',
                        '0001',     
                    ]
        
        return str(regiones), (bits_save)
    
    #CUSTOM RX - Define regiones y bits_save para función check conditions, para constelación definida por usuario
    def check_regions_user(self, nsimb, etiquetas, umbrales, umbrales_i, umbrales_no, constellation): #entran umbrales inter, inter en Y y sin inter
        #Se definen regiones y bits_save para la función ya hecha "check_conditions". PERO me parece que con la funcion "is_inside_sm" formando poligonos con: punto interseccion de los umbrales, punto extremo hacia un lado de un umbral, punto extremo hacia un lado del otro umbral, la función retorna directamente si el punto está dentro de la región formada
        
        #Se usa una constelación de referencia RX para definir a que región se traducen los simbolos a bits 0's o 1's
        if nsimb == 2: #2 Regiones formadas por linea vertical u horizontal
            if etiquetas[0] == 1: #Vertical
            
                regiones = [
                    'samples.real < umbrales_no[0][0].real', #0 #Region izquierda es 0
                    'samples.real > umbrales_no[0][0].real', #1
                    ]
                    
                if constellation[0].real < umbrales_no[0][0].real: #Primer simbolo constelación es 0, el segundo es 1
                    bits_save = [
                        '0',
                        '1',
                    ]
                    print("{} esta a la izquiera de umbral y es bit 0".format(constellation[0]))
                else:
                    bits_save = [
                        '1', #En este condicional, region izquierda es 1 y derecha es 0
                        '0',
                    ]
                    print("{} esta a la derecha de umbral y es bit 0".format(constellation[0]))
    
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[0] == 2: #Horizontal
                regiones = [
                    'samples.imag < umbrales_no[0][0].imag', #0 #Region arriba es 0
                    'samples.imag > umbrales_no[0][0].imag', #1
                    ]
                    
                if constellation[0].imag < umbrales_no[0][0].imag:
                    bits_save = [
                        '0',
                        '1',
                        ]
                else:
                    bits_save = [
                        '1',
                        '0',
                        ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[0] == 3: #Inclinada
                regiones = [
                    'samples.imag > umbrales[0](samples.real)', #0 #Region arriba es 0, dependiendo del angulo de inclinacion, algo subjetivo
                    'samples.imag < umbrales[0](samples.real)', #1
                    ]
                    
                if constellation[0] > umbrales[0](samples.real):
                    bits_save = [
                        '0',
                        '1',
                        ]
                else:
                    bits_save = [
                        '1',
                        '0',
                        ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
        elif nsimb == 4: #2 umbrales
            if etiquetas[0] == 1 and etiquetas[1] == 2: #Linea Vertical con Horizontal
                regiones = [
                    '(samples.real < umbrales_no[0][0].real) & (samples.imag > umbrales_no[1][0].imag)', #00 Arriba izquierda
                    '(samples.real > umbrales_no[0][0].real) & (samples.imag > umbrales_no[1][0].imag)', #01 Arriba derecha
                    '(samples.real > umbrales_no[0][0].real) & (samples.imag < umbrales_no[1][0].imag)', #10 Abajo derecha
                    '(samples.real < umbrales_no[0][0].real) & (samples.imag < umbrales_no[1][0].imag)', #11 Abajo izquierda
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[1] == 1 and etiquetas[0] == 2: #Linea Horizontal con Vertical
                regiones = [
                    '(samples.real < umbrales_no[1][0].real) & (samples.imag > umbrales_no[0][0].imag)', #00 Arriba izquierda
                    '(samples.real > umbrales_no[1][0].real) & (samples.imag > umbrales_no[0][0].imag)', #01 Arriba derecha
                    '(samples.real > umbrales_no[1][0].real) & (samples.imag < umbrales_no[0][0].imag)', #10 Abajo derecha
                    '(samples.real < umbrales_no[1][0].real) & (samples.imag < umbrales_no[0][0].imag)', #11 Abajo izquierda
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[0] == 1 and etiquetas[1] == 3: #Linea Vertical con Inclinada
                regiones = [
                    '(samples.real < umbrales_no[0][0].real) & (samples.imag > umbrales[1](samples.real))', #00 Arriba izquierda (subjetivo al angulo)
                    '(samples.real > umbrales_no[0][0].real) & (samples.imag > umbrales[1](samples.real))', #01 Arriba derecha
                    '(samples.real > umbrales_no[0][0].real) & (samples.imag < umbrales[1](samples.real))', #10 Abajo derecha
                    '(samples.real < umbrales_no[0][0].real) & (samples.imag < umbrales[1](samples.real))', #11 Abajo izquierda
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[0] == 3 and etiquetas[1] == 1: #Linea Inclinada con Vertical
                regiones = [
                    '(samples.real < umbrales_no[1][0].real) & (samples.imag > umbrales[0](samples.real))', #00 Arriba izquierda (subjetivo al angulo)
                    '(samples.real > umbrales_no[1][0].real) & (samples.imag > umbrales[0](samples.real))', #01 Arriba derecha
                    '(samples.real > umbrales_no[1][0].real) & (samples.imag < umbrales[0](samples.real))', #10 Abajo derecha
                    '(samples.real < umbrales_no[1][0].real) & (samples.imag < umbrales[0](samples.real))', #11 Abajo izquierda
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[0] == 2 and etiquetas[1] == 3: #Linea Horizontal con Inclinada
                regiones = [
                    '(samples.imag > umbrales_no[0][0].imag) & (samples.real < umbrales_i[1](samples.imag))', #00 Arriba izquierda (subjetivo angulo)
                    '(samples.imag > umbrales_no[0][0].imag) & (samples.real > umbrales_i[1](samples.imag))', #01 Arriba derecha
                    '(samples.imag < umbrales_no[0][0].imag) & (samples.real > umbrales_i[1](samples.imag))', #10 Abajo derecha
                    '(samples.imag < umbrales_no[0][0].imag) & (samples.real < umbrales_i[1](samples.imag))', #11 Abajo izquierda
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[0] == 3 and etiquetas[1] == 2: #Linea Inclinada con Horizontal
                regiones = [
                    '(samples.imag > umbrales_no[1][0].imag) & (samples.real < umbrales_i[0](samples.imag))', #00 Arriba izquierda (subjetivo angulo)
                    '(samples.imag > umbrales_no[1][0].imag) & (samples.real > umbrales_i[0](samples.imag))', #01 Arriba derecha
                    '(samples.imag < umbrales_no[1][0].imag) & (samples.real > umbrales_i[0](samples.imag))', #10 Abajo derecha
                    '(samples.imag < umbrales_no[1][0].imag) & (samples.real < umbrales_i[0](samples.imag))', #11 Abajo izquierda
                    ]
                bits_save = [
                        '00',
                        '01',
                        '10',
                        '11',
                    ]
                #result = np.select(regiones, bits_save, default=random.choice(bits_save))
                
            elif etiquetas[0] == 3 and etiquetas[1] == 3: #Linea Inclinada con Inclinada
                #hallar punto interseccion pues va a ayudar mucho
                #luego ver cual umbral es mayor o menor al otro a la izquierda, arriba, abajo y derecha, y a partir de alli definir las regiones
                #para cumplir con el orden de asignación de bits a las regiones
                #aunque creo que es mejor irse por los angulos... Que los ingresa el usuario pero para no extender mas la funcion se pueden calcular
                
                if np.angle(umbrales_no[0][1]) > np.angle(umbrales_no[1][1]): #Umbral 1 tiene mayor angulo que umbral 2
                #Esto quiere decir que, a la derecha umbral1 > umbral2, y a la izquierda lo opuesto
                #Arriba lo mas probable es que umbral2 este a la izquierda y umbral1 a la derecha, y abajo lo opuesto
                
                    point = find_intersection(umbrales_no[0].real, umbrales_no[0].imag, umbrales_no[1].real, umbrales_no[1].imag) #punto interseccion
                
                #ARREGLAR ESTAS REGIONES :((
                    regiones = [
                        '(samples.real < point.real) & (samples.imag < umbrales[1](samples.real)) & (samples.imag > umbrales[0](samples.real))', #00 Arriba izquierda (subjetivo angulo)
                        '(samples.imag > point.imag) & (samples.real > umbrales_i[1](samples.imag)) & (samples.real < umbrales_i[0](samples.imag))',#01 Arriba derecha
                        '(samples.imag < point.imag) & (samples.real < umbrales_i[1](samples.imag)) & (samples.real > umbrales_i[0](samples.imag))',   #10 Abajo derecha
                        '(samples.imag < point.imag) & (samples.real < umbrales[1](samples.imag)) & (samples.real > umbrales[0](samples.imag))', #11 Abajo izquierda
                        ]
                    bits_save = [
                            '00',
                            '01',
                            '10',
                            '11',
                        ]
                    #result = np.select(regiones, bits_save, default=random.choice(bits_save))                              
            
        return str(regiones), (bits_save) 
    
    
    
    
    
    def check_conditions(self, samples, regiones, bits_save, umbrales, umbrales_i, umbrales_no, nsimb, esquema): #Umbrales de entrada tienen que ser los umbrales interpolados
        
        if nsimb == 8 and esquema == 1: #Si hay circulo tengo que verificar sus condiciones antes. Toma más tiempo
            circle = np.empty(len(samples), dtype=bool)
            for i, point in enumerate(samples):
                print(point)
                circle[i] = MainFunctions.is_inside_sm(self, umbrales_no[2], point)
        #print(circle)

        regiones = eval(regiones)
        for index,region in enumerate(regiones):
            regiones[index] = eval(region)

        #bits_save = eval(bits_save)
        #for index,bits in enumerate(bits_save):
        #    bits_save[index] = eval(bits)
        
        result = np.select(regiones, bits_save, default=random.choice(bits_save))

        #Se puede poner lo siguiente para retornar None en default y despues, fuera de la función, quitarle esos None
        #result = result[~np.isnan(result)]

        return result
        
    #Función para umbral definido por usuario. Retorna umbrales y etiquetas identificadoras 
    def threshold_user(self, nsimb, selector1="vertical", selector2="vertical", offset_x=0, offset_y=0, angle=0, offset_x2=0, offset_y2=0, angle2=0): 

        def linea_vertical(point):
            real_domain = np.linspace(-20,20,num=2, dtype=complex) 
            imag_domain = np.linspace(-20j,20j,num=2, dtype=complex)
            umbral = imag_domain + real_domain * 0 + 1*point
            return umbral

        def linea_horizontal(point):
            real_domain = np.linspace(-20,20,num=2, dtype=complex) 
            imag_domain = np.linspace(-20j,20j,num=2, dtype=complex)
            umbral = imag_domain * 0 + real_domain + 1j*point
            return umbral

        def linea_inclinada(angle, offset_x, offset_y):
            real_domain = np.linspace(-500,500,num=2, dtype=complex) 
            imag_domain = np.linspace(-500j,500j,num=2, dtype=complex) #Parece que si aumentas el numero extremo es mas preciso el calculo de algunas cosas???
            umbral = imag_domain * MainFunctions.slope(self,angle) + real_domain + 1*offset_x + 1j*offset_y
            return umbral

        etiquetas = [] #Identificador del tipo de línea creado

        if nsimb == 2: #Un solo umbral si 2 simbolos
            if selector1 == "vertical":
                umbrales = np.array([linea_vertical(offset_x)])
                etiquetas.append(1)
            elif selector1 == "horizontal":
                umbrales = np.array([linea_horizontal(offset_y)])
                etiquetas.append(2)
            elif selector1 == "inclinada":
                umbrales = np.array([linea_inclinada(angle, offset_x, offset_y)])
                etiquetas.append(3)
            else:
                print("ERROR SELECCION DE LINEA PARA UMBRAL")
            
        elif nsimb == 4: #Aca creo que es mejor hacer que el usuario obligatoriamente defina 2 umbrales
            if selector1 == "vertical":
                umbral1 = np.array([linea_vertical(offset_x)])
                etiquetas.append(1)
            elif selector1 == "horizontal":
                umbral1 = np.array([linea_horizontal(offset_y)])
                etiquetas.append(2)
            elif selector1 == "inclinada":
                umbral1 = np.array([linea_inclinada(angle, offset_x, offset_y)])
                print("Inclinada 1 lista")
                etiquetas.append(3)
            if selector2 == "vertical":
                umbral2 = np.array([linea_vertical(offset_x2)])
                etiquetas.append(1)
            elif selector2 == "horizontal":
                umbral2 = np.array([linea_horizontal(offset_y2)])
                etiquetas.append(2)
            elif selector2 == "inclinada":
                umbral2 = np.array([linea_inclinada(angle2, offset_x2, offset_y2)])
                print("inclinada 2 lista")
                etiquetas.append(3)
            umbrales = np.array([umbral1,umbral2])
    
        return umbrales, etiquetas #Se retornan los umbrales y las etiquetas que los identifican, necesarias para el chequeo de regiones formadas  
   
   
   
    def bits_to_string(self,bits):
        binary_string = ''.join(bits)
        text = ''.join((chr(int(binary_string[i:i+8],2))) for i in range(0,len(binary_string),8))
        return text
        


    def interpolate_umbrales(self, umbrales):
        umbrales_interpolate = np.array([])
        umbrales_interpolate_i = np.array([])
        for umbral in umbrales:
            umbrales_interpolate = np.append(umbrales_interpolate, interpolate.interp1d(umbral.real,umbral.imag))
        for umbral in umbrales:
            umbrales_interpolate_i = np.append(umbrales_interpolate_i, interpolate.interp1d(umbral.imag,umbral.real))
        return umbrales_interpolate, umbrales_interpolate_i


    def separate_preamble(self, received, fc_signal = 50000, fc_preamble = 110000, fsample = 522000, n_samples = 100): #Quito el preambulo.
        #Con FC_Signal filtro la señal para quitarle ruido. Con FC_preamble filtro preambulo para quitarle ruido.
        #Las frecuencias de corte deberían ir en función al bando de ancho de la modulación.
        received = received[n_samples:]
        preamble = received[0:n_samples]

        w_received = fc_signal / (fsample / 2) # Normalize the frequency
        w_preamble = fc_preamble / (fsample / 2)
        b_received, a_received = signal.butter(5, w_received, 'low')
        b_preamble, a_preamble = signal.butter(5, w_preamble, 'low')

        received = signal.filtfilt(b_received, a_received, received) #Señal de interes filtrada
        preamble = signal.filtfilt(b_preamble, a_preamble, preamble)
        return received, preamble #Retorna lo recibido filtrado sin preambulo, y el preambulo solito filtrado

    """
    def coarse_frequency_correction(self,preamble, referencia = 80e3, Fs = 522000): #Corrijo offset frecuencia en base a la frecuencia del preambulo
        #Entre el preambulo y le calculo su offset en frecuencia en función a la frecuencia fijada para el preambulo
        # Calculate the FFT of the signal
        signal_fft = np.fft.fft(preamble)

        # Find the peak frequency
        peak_freq = np.argmax(np.abs(signal_fft))

        # Convert the peak frequency to Hz
        peak_freq_hz = peak_freq * Fs / len(preamble)
    
        #referencia = 80e3
        diferencia = referencia - peak_freq_hz

        # Create a frequency correction signal
        correction_signal = np.exp(1j * 2 * np.pi * diferencia * np.arange(len(preamble)) / Fs)

        # Apply the correction
        corrected_signal = signal * correction_signal

        return corrected_signal, peak_freq_hz, diferencia #Retorna el preambulo corregido, la frecuencia maxima detectada y el offset en frecuencia
    """
    
    def coarse_frequency_correction(self,signal, Fs, nsimb = 4):

        #Sin elevar a la potencia
        signal_fft = np.fft.fftshift(np.abs(np.fft.fft(signal)))
        f = np.linspace(-Fs/2.0, Fs/2.0, len(signal_fft))
        
        #fig1, ax1 = plt.subplots(2)
        #ax1[0].plot(f,signal_fft)
        #ax1[0].set_title('FFT Signal sin potencia')
    
        #Elevo a la potencia del esquema de modulacion la señal
        signal_potencia = np.power(signal,nsimb)
    
        # Calculate the FFT of the signal con potencia
        signal_fft = np.fft.fftshift(np.abs(np.fft.fft(signal_potencia)))
        
        f = np.linspace(-Fs/2.0, Fs/2.0, len(signal_fft))
    
        #ax1[1].plot(f,signal_fft)
        #ax1[1].set_title('FFT Signal con potencia')
        #plt.show()
        
        # Find the peak frequency
        peak_freq_hz = f[np.argmax(signal_fft)] / nsimb
    
        # Convert the peak frequency to Hz
        #peak_freq_hz = peak_freq * Fs / len(signal)   #VERIFICAR ACÁ A VER QUÉ PASA, DIFERENCIAS
    
        # Create a frequency correction signal
        correction_signal = np.exp(-1j * 2 *np.pi * peak_freq_hz * np.arange(len(signal)) / Fs)
    
        # Apply the correction
        corrected_signal = signal * correction_signal
    
        return corrected_signal, peak_freq_hz
        
    def coarse_phase_correction(self,signal_interes, preambulo, peak_hz, fsample):
        t = np.arange(100) / fsample
        preambulo_original = 0.5*np.exp(2j*np.pi*80e3*t)
        
        
        #Filtro el preambulo, de momento este es una sinusoide a 80kHz.
        fc = 120000  # Cut-off frequency of the filter
        w = fc / (fsample / 2) # Normalize the frequency
        b, a = signal.butter(5, w, 'low')
        preambulo = signal.filtfilt(b, a, preambulo) #Preambulo filtrado para quitar ruido
        
        #Se corrige la frecuencia del preambulo con el offset obtenido el coarse freq
        preambulo = preambulo * np.exp(-2j*np.pi*peak_hz*t)
        
        #Estimados desfase
        delta_phi = np.angle(np.mean(preambulo * np.conj(preambulo_original)))
        print("Desfase coarse estimado ", delta_phi)
        
        #Se corrige esa fase estimada en la señal de interes
        signal_interes = signal_interes * np.exp(-1j*delta_phi)
        
        #fig3, ax3 = plt.subplots(2)
        #ax3[0].plot(preambulo_original.real)
        #ax3[0].plot(preambulo_original.imag) 
        #ax3[1].plot(preambulo.real) 
        #ax3[1].plot(preambulo.imag)
        #plt.show() 
        
        return signal_interes, delta_phi
        
    def fine_frequency_correction(self,signal, loop_bandwidth, initial_freq_offset=0.0, modulation_scheme = 'BPSK'):
        # Define loop parameters
        loop_filter = np.array([1, -1], dtype=complex) * loop_bandwidth / (4 * np.pi)
        vco = np.exp(-1j * 2 * np.pi * initial_freq_offset * np.arange(len(signal)))
    
        # Initialize variables
        output_signal = np.zeros_like(signal)
        error = np.zeros_like(signal)
        phase_estimate = 0.0
    
        # Costas loop
        for i in range(1, len(signal)):
            # Multiply the input signal with the VCO output
            output_signal[i] = signal[i] * vco[i]
    
            # Calculate the phase error
            if modulation_scheme == 'BPSK':
                error[i] = np.real(output_signal[i]) * np.imag(output_signal[i]) # This is the error formula for 2nd order Costas Loop (e.g. for BPSK)
            elif modulation_scheme == 'QPSK':
                error[i] = MainFunctions.phase_detector_4(self,output_signal[i])
            elif modulation_scheme == '16PSK':
                #error[i] = MainFunctions.phase_detector_16psk(self,output_signal[i])
                pass
            elif modulation_scheme == 'CUSTOM':
                pass
    
            # Update the loop filter and VCO
            loop_filter[0] = loop_filter[0] + error[i]
            phase_estimate = np.real(loop_filter).sum() + 1j * np.imag(loop_filter).sum()
            vco[i + 1 : i + 3] = np.exp(-1j * phase_estimate)
    
        return output_signal
        
    def muller_muller_clock_recovery(self,samples, samples_per_symbol, initial_phase=0.0):
        # Normalize the samples
        samples /= np.abs(samples).max()
    
        # Interpolate the signal
        samples_interpolated = signal.resample_poly(samples, samples_per_symbol, 1)
    
    
        mu = initial_phase
        out = np.zeros(len(samples_interpolated) + 10, dtype=complex)
        out_rail = np.zeros(len(samples_interpolated) + 10, dtype=complex)
        i_in = 0
        i_out = 2
    
        while i_out < len(samples) and i_in + samples_per_symbol < len(samples):
            out[i_out] = samples_interpolated[i_in*samples_per_symbol + int(mu*samples_per_symbol)]
            out_rail[i_out] = int(np.real(out[i_out]) > 0) + 1j * int(np.imag(out[i_out]) > 0)
            x = (out_rail[i_out] - out_rail[i_out-2]) * np.conj(out[i_out-1])
            y = (out[i_out] - out[i_out-2]) * np.conj(out_rail[i_out-1])
            mm_val = np.real(y - x)
            mu += samples_per_symbol + 0.3 * mm_val
            i_in += int(np.floor(mu))
            mu = mu - np.floor(mu)
            i_out += 1
    
        out = out[2:i_out]
        return out
        
    def phase_detector_4(self,sample): #Error para fine QPSK
        if sample.real > 0:
            a = 1.0
        else:
            a = -1.0
        if sample.imag > 0:
            b = 1.0
        else:
            b = -1.0
        return a * sample.imag - b * sample.real
    
    def phase_detector_16psk(self,sample): #Error para fine 16PSK
        psk16_domain = np.arange(0,16)
        constellation = np.exp(2j* np.pi * psk16_domain / 16)
        
        closest_point = constellation[np.argmin(np.abs(constellation - sample))]
        
        #error = np.angle(closest_point * np.conj(sample))
        
        error = closest_point.imag * sample.imag - closest_point.real * sample.real 
        #print(error)
        
        return error
    
    def phase_detector_16psk_2(self,sample, estimated_phase, loop_filter_coeffs):
        error = 0.5 * sample * np.exp(-1j * estimated_phase)
        k_values = np.arange(1,9)
        additional_terms = -loop_filter_coeffs * np.sin(2 * k_values * np.pi * estimated_phase)
        error += np.sum(additional_terms)
        error_value = np.real(error)
        return error_value
        
    def phase_detector_custom(self, sample):
        constellation = self.constellation_rx
        closest_point = constellation[np.argmin(np.abs(constellation - sample))]
        error = closest_point.imag * sample.imag - closest_point.real * sample.real
        return error
    
    def fine_frequency_correction2(self,samples, fs = 522000, modulation_scheme='QPSK', alpha=0.132, beta=0.00932, freq=0):
        N = len(samples)
        phase = 0
        freq = 0
        # These next two params is what to adjust, to make the feedback loop faster or slower (which impacts stability)
        alpha = alpha
        beta = beta
        out = np.zeros(N, dtype=complex)
        freq_log = []
        for i in range(N):
            out[i] = samples[i] * np.exp(-1j*phase) # adjust the input sample by the inverse of the estimated phase offset
            
            if modulation_scheme == 'BPSK':
                error = np.real(out[i]) * np.imag(out[i]) # This is the error formula for 2nd order Costas Loop (e.g. for BPSK)
            elif modulation_scheme == 'QPSK':
                error = MainFunctions.phase_detector_4(self,out[i])
            elif modulation_scheme == '16PSK':
                #error = MainFunctions.phase_detector_16psk(self,out[i])
                error = 0
            elif modulation_scheme == 'CUSTOM':
                error = 0
            
            #print('error:',error)
        
            # Advance the loop (recalc phase and freq offset)
            freq += (beta * error)
            freq_log.append(freq * fs / (2*np.pi)) # convert from angular velocity to Hz for logging
            phase += freq + (alpha * error)
            
            # Optional: Adjust phase so its always between 0 and 2pi, recall that phase wraps around every 2pi
            while phase >= 2*np.pi:
                phase -= 2*np.pi
            while phase < 0:
                phase += 2*np.pi
        return out, freq_log

    def apply_frequency_correction(self, signal, diferencia, Fs=522000):
        corrected_signal = signal * 0.5*np.exp(2j * np.pi * diferencia * np.arange(len(signal)) / Fs)
        return corrected_signal

    def apply_phase_correction(self, signal, preambulo, preambulo_original):
        delta_phi = np.angle(np.mean(preambulo * np.conj(preambulo_original)))
        return signal * np.exp(-1j*delta_phi)
        
    def real_time_plt_stopped(self, fsample, tsimb, umbrales, umbrales_interpolate, umbrales_interpolate_i, regiones, bits_save, nsimb, esquema):
        
        self.stop_realtime_flag = True
        
        self.realtime_buffer.join()
        
        self.ui.stackedWidget_15.setCurrentWidget(self.ui.page_29)

        self.timer.stop()

        #self.ui.SRlayout.removeWidget(self.graphWidget_2)

        self.ui.DEPlayout.itemAt(0).widget().deleteLater()
        #self.ui.DEPlayout.removeWidget(self.graphWidget_3)

        self.ui.Constlayout.itemAt(0).widget().deleteLater()
        #self.ui.Constlayout.removeWidget(self.graphWidget)

        self.ui.recBBlayout.itemAt(0).widget().deleteLater()
        #self.ui.recBBlayout.removeWidget(self.graphWidget_4)



        print("3- RECEPCIÓN TERMINADA")
        """
        #Como primer paso separo la señal del preambulo y los filtro un poco para eliminar ruido
        self.muestras, preambulo = self.separate_preamble(self, self.muestras, fc_signal = 50000, fc_preamble = 110000, fsample = 522000, n_samples = 100)

        #Como segundo paso, calculo el offset en frecuencia del preambulo
        preambulo_corregido, peak_freq_hz, diferencia = self.coarse_frequency_correction(self, preambulo, referencia = 80e3, Fs = 522000)

        #Como tercer paso, aplico la correcion de frecuencia en base al offset calculado en el paso anterior con el preambulo
        self.muestras = apply_frequency_correction(self, self.muestras, diferencia, Fs=522000)

        #Como cuarto paso calculo la diferencia de fase entre el preambulo corregido recibido y el original, y aplico la correcion a la señal
        preambulo_original = np.array([], dtype=complex)
        preambulo_original = add_preamble(self,preambulo_original, fsample = 522000, freq = 80e3, n_samples = 100)
        self.muestras = apply_phase_correction(self, self.muestras, preambulo_corregido, preambulo_original)

        #Como quinto paso, se harían todos los procesos de detección para obtener los bits de los simbolos
        
        regiones, bits_save = define_regions(4,1)
        umbrales = threshold_defined(4,1)
        umbrales_interpolate, umbrales_interpolate_i = interpolate_umbrales(umbrales)
        resultado_total = check_conditions(simbolos, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, 2, 3)
        

        #Como sexto paso, se calcularía la probabilidad de error

        #Como septimo paso, se graficaría todo
        sample_rate = 522000
        t = np.arange(len(self.muestras)) / sample_rate
        """
        
        #Primer paso: Separo el ruido de la señal que me interesa para quedarme con esta última
        print("4. OBTENIENDO SEÑAL DE INTERES")
        margen = 4
        resultado = np.where(~(self.muestras.real <=margen) | ~(self.muestras.real >=-margen) | ~(self.muestras.imag <=margen) | ~(self.muestras.imag >=-margen))
        print(resultado)
        print(self.muestras)
        start = resultado[0][0]
        end = resultado[0][-1:]
        end = int(end[0])

        resultado_interes = self.muestras[start:end]
        
        #Segundo paso: Se separan las partes o "paquetes" de la señal de interés
        print("5. SEPARANDO PARTES OBTENIDAS")
        sps = int(fsample * tsimb)
        size = sps*100 + 100 #Muestras por simbolo * 100 = 100 simbolos + 100 muestras del preambulo
        resultado_packets = np.split(resultado_interes, np.arange(size, len(resultado_interes), size))
        print("5- SE RECIBIERON {} PARTES".format(len(resultado_packets)))
        
        #Tercer paso: Realizo esquema RX para cada "paquete" recibido. Se juntan al final.
        resultado_total = np.array([]) #Sin muller, con coarse y fine freq
        resultado_total2 = np.array([]) #Con muller, con coarse y fine freq
        resultado_total3 = np.array([]) #Solo filtrando sin hacer nada más
        resultado_total4 = np.array([]) #Solo freq coarse
        resultado_total5 = np.array([]) #Solo freq coarse y phase "coarse"
        resultado_total6 = np.array([]) #Sin muller, con freq coarse y phase "coarse", y con fine freq2 creo
        resultado_total7 = np.array([]) #Sin muller, con freq coarse y phase "coarse", y con fine freq el otro
        
        self.graph_filtered = np.array([])
        self.graph_corrected = np.array([])
        self.graph_sincro = np.array([])
        self.graph_sincro_corrected = np.array([])
        
        #Selección del esquema acorde a la modulación utilizada, para la corrección de errores y normalización de los símbolos.
        if nsimb == 2 and esquema == 3: #BPSK normal
            mod_scheme = "BPSK"
        elif nsimb == 4 and esquema == 2: #QPSK normal
            mod_scheme = "QPSK"
        elif nsimb == 16 and esquema == 1: #16PSK normal
            mod_scheme = "16PSK"
        elif esquema == "CUSTOM":
            mod_scheme = "CUSTOM"
        else:
            mod_scheme = "CUSTOM"
        
        if esquema == "CUSTOM":
            factor_real = np.max(abs(self.constellation_rx.real))
            factor_imag = np.max(abs(self.constellation_rx.imag))
        else:
            factor_real = np.max(abs(MainFunctions.create_constellation_tx(self, nsimb,esquema).real)) #Verificar si para nsimb 8 o 16 hace falta cambiar algo acá, como poner más condicionales
            factor_imag = np.max(abs(MainFunctions.create_constellation_tx(self, nsimb,esquema).imag))
        print("Esquema es: ",esquema)
        print("mod_scheme es: ", mod_scheme)
        print("Factores normalización real - imag: ", factor_real, factor_imag)
        #(Linea para seleccion de esquema de modulación basado en nsimb y esquema de umbral elegido)
        print("6. INICIALIZANDO ESQUEMA CORRECCION Y DETECCION RX")
        for paquete in resultado_packets:
            resultado = paquete[100:] #Se separa el preambulo y la señal de "datos"
            preambulo = paquete[0:100]
            num_taps = len(resultado)
            h = rrcosfilter(num_taps, alpha = 0.35, Ts = sps/fsample, Fs = fsample)[1]
            filtered = np.convolve(resultado,h,mode='same') #Se aplica el filtro raiz coseno en recepción
            
            sin_nada = filtered #Muestras para señal solo filtrada
            
            filtered, peak_hz = MainFunctions.coarse_frequency_correction(self, filtered, fsample, nsimb) #Se aplica correción de Frecuencia Portadora
            #Verificar la formula con nsimb para esta función, por favor. Documentación en pysdr.org
            
            solo_freq_coarse = filtered #Muestras para señal con solo Frecuencia corregida
            
            filtered_phase, delta_phi = MainFunctions.coarse_phase_correction(self, filtered, preambulo, peak_hz, fsample) #Muestras para Freq Coarse y Phase Coarse
            
            #Sincronización en tiempo (No Muller). RECORDAR QUE LA NORMALIZACIÓN VARÍA CON LA CONSTELACIÓN
            symbolindices = np.arange(0, len(filtered), sps) #Indices para tomar muestra cada Sps
            
            simbolos = filtered[symbolindices] #Señal sin muller, con coarse y fine freq
            simbolos.real = simbolos.real/np.max(abs(simbolos.real))
            simbolos.imag = simbolos.imag/np.max(abs(simbolos.imag))
            simbolos.real = simbolos.real * factor_real
            simbolos.imag = simbolos.imag * factor_imag
            
            simbolos_sin_nada = sin_nada[symbolindices] #Solo señal Filtrada
            simbolos_sin_nada.real = simbolos_sin_nada.real / np.max(abs(simbolos_sin_nada.real))
            simbolos_sin_nada.imag = simbolos_sin_nada.imag / np.max(abs(simbolos_sin_nada.imag))
            simbolos_sin_nada.real = simbolos_sin_nada.real * factor_real
            simbolos_sin_nada.imag = simbolos_sin_nada.imag * factor_imag
            
            simbolos_solo_freq_coarse = solo_freq_coarse[symbolindices] #Señal con solo Frecuencia corregida
            simbolos_solo_freq_coarse.real = simbolos_solo_freq_coarse.real / np.max(abs(simbolos_solo_freq_coarse.real))
            simbolos_solo_freq_coarse.imag = simbolos_solo_freq_coarse.imag / np.max(abs(simbolos_solo_freq_coarse.imag))
            simbolos_solo_freq_coarse.real = simbolos_solo_freq_coarse.real * factor_real
            simbolos_solo_freq_coarse.imag = simbolos_solo_freq_coarse.imag * factor_imag
            
            simbolos_phase_freq = filtered_phase[symbolindices] #Señal con Frecuencia y Fase corregida
            simbolos_phase_freq.real = simbolos_phase_freq.real / np.max(abs(simbolos_phase_freq.real))
            simbolos_phase_freq.imag = simbolos_phase_freq.imag / np.max(abs(simbolos_phase_freq.imag))
            simbolos_phase_freq.real = simbolos_phase_freq.real * factor_real
            simbolos_phase_freq.imag = simbolos_phase_freq.imag * factor_imag
            
            #Sincronización en tiempo con Muller
            simbolos2 = MainFunctions.muller_muller_clock_recovery(self, filtered, samples_per_symbol=sps, initial_phase=0.0) #Con muller, con coarse y fine freq
            
            #Se aplica Fine Frequency Correction. PILA CON LOS ESQUEMAS, SE DEBEN SELECCIONAR DE ANTES
            simbolos2, freq_log2 = MainFunctions.fine_frequency_correction2(self, simbolos2, fs=fsample / sps, modulation_scheme = mod_scheme, alpha = 0.132, beta = 0.00932) #Con muller, con coarse y fine freq
            
            simbolos, freq_log = MainFunctions.fine_frequency_correction2(self, simbolos, fs=fsample / sps, modulation_scheme = mod_scheme, alpha=0.132, beta=0.00932) #Señal sin muller, con coarse y fine freq
            
            simbolos3, freq_log3 = MainFunctions.fine_frequency_correction2(self, simbolos_phase_freq, fs=fsample / sps, modulation_scheme = mod_scheme, alpha=0.132, beta=0.00932) #Sin muller, con freq coarse y phase "coarse", y con fine freq2 creo
            
            simbolos4 = MainFunctions.fine_frequency_correction(self, simbolos_phase_freq, (1/tsimb)*2, initial_freq_offset=0.0, modulation_scheme = mod_scheme) #Sin muller, con freq coarse y phase "coarse", y con fine freq el otro
            
            esquema = 1 #Esto es prueba TEMPORAL, lo usa el check conditions solamente para modulaciones con mas de un esquema, implementar o modificar a futuro.
            
            #Se acumulan los resultados obtenidos de todas las partes luego de aplicar esquema RX.
            resultado_total = np.append(resultado_total,MainFunctions.check_conditions(self,simbolos, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, nsimb, esquema)) #Sin muller, con coarse y fine freq
    
            resultado_total2 = np.append(resultado_total2,MainFunctions.check_conditions(self,simbolos2, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, nsimb, esquema)) #Con muller, con coarse y fine freq
    
            resultado_total3 = np.append(resultado_total3,MainFunctions.check_conditions(self,simbolos_sin_nada, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, nsimb, esquema)) #Solo filtrando sin hacer nada más
    
            resultado_total4 = np.append(resultado_total4,MainFunctions.check_conditions(self,simbolos_solo_freq_coarse, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, nsimb, esquema)) #Solo freq coarse
    
            resultado_total5 = np.append(resultado_total5,MainFunctions.check_conditions(self,simbolos_phase_freq, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, nsimb, esquema)) #Solo freq coarse y phase "coarse"
    
            resultado_total6 = np.append(resultado_total6,MainFunctions.check_conditions(self,simbolos3, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, nsimb, esquema)) #Sin muller, con freq coarse y phase "coarse", y con fine freq2 creo
    
            resultado_total7 = np.append(resultado_total7,MainFunctions.check_conditions(self,simbolos4, regiones, bits_save, umbrales_interpolate, umbrales_interpolate_i, umbrales, nsimb, esquema)) #Sin muller, con freq coarse y phase "coarse", y con fine freq el otro
            
            self.graph_filtered = np.append(self.graph_filtered, sin_nada) #Señal tiempo filtrada
            
            self.graph_corrected = np.append(self.graph_corrected, filtered_phase) #Señal tiempo corregida freq y fase
            
            self.graph_sincro = np.append(self.graph_sincro, simbolos_phase_freq) #Señal sincronizada en tiempo
            
            self.graph_sincro_corrected = np.append(self.graph_sincro_corrected, simbolos3) #Señal sincro y corregida en tiempo
            
            #Para graficar: Las variable contienen la señal en tiempo, ejemplo:
            
            #Graficar tiempo: 
            #t = np.arange(len(self.variable)) / fsample
            #plt_received_signal2(t, self.muestras.real, t, self.muestras.imag)
            
            #Graficar DEP:
            #plt_received_signal(self.muestras, 522000)
            
            #Graficar Constelación:
            #plt_received_signal3(self.muestras.real, self.muestras.imag)
            
            #Entonces, cada variable representa una fase de la recepción, las pasas por esas funciones y obtienes los resultados de cada fase correspondiente
            
            
            
            
            #En este punto se obtuvieron un arreglos con strings de 1's y 0's, que representan el resultado del esquema RX para cada método
            #De allí se pueden convertir a texto, imagen, o el formato requerido
            #FIN DEL CICLO FOR
        print("6- ESQUEMA CORRECIONES RX REALIZADO")
        print("")
        print("Resultado 1: No Muller, Coarse y Fine")
        print(MainFunctions.bits_to_string(self,resultado_total))
        print("")
        print("Resultado 2: Muller, Coarse y Fine")
        print(MainFunctions.bits_to_string(self,resultado_total2))
        print("")
        print("Resultado 3: Solo Filtrada")
        print(MainFunctions.bits_to_string(self,resultado_total3))
        print("")
        print("Resultado 4: Solo Coarse")
        print(MainFunctions.bits_to_string(self,resultado_total4))
        print("")
        print("Resultado 5: Coarse y Phase")
        print(MainFunctions.bits_to_string(self,resultado_total5))
        print("")
        print("Resultado 6: Coarse, Phase y Fine")
        print(MainFunctions.bits_to_string(self,resultado_total6))
        print("")
        print("Resultado 7: Coarse, Phase y Fine GPT")
        print(MainFunctions.bits_to_string(self,resultado_total7))
        print("")

        #Cuarto paso: Verificar y seleccionar mejor resultado
        
        #Quinto paso: Se crean las gráficas para todo
            
        self.ui.finalInfo_2.setText("") #AQUÍ COLOCAR INFORMACIÓN ESPECIFICA CON RESPECTO A LA SEÑAL RECIBIDA COMO "PROBABILIDAD DE ERROR", NUMERO DE BITS RECIBIDOS, NUMERO DE BITS CON ERRORES, ENTRE OTROS

        self.grafica1 = plt_received_signal(self.muestras, 522000)  #PASA LAS VARIABLES PARA CONSTRUIR LA DEP DE LA SEÑAL RECIBIDA
        self.toolbar1 = NavigationToolbar(self.grafica1, self)
        
        t = np.arange(len(self.muestras)) / 522000

        #self.grafica2 = plt_received_signal2(t, self.muestras.real, t, self.muestras.imag) #PASA LAS VARIABLES PARA CONSTRUIR LA SEÑAL EN BITS RECONTRUIDOS
        #self.toolbar2 = NavigationToolbar(self.grafica2, self)

        self.grafica3 = plt_received_signal3(self.muestras.real, self.muestras.imag) #PASA LAS VARIABLES PARA CONSTRUIR LA CONSTELACIÓN DE LA SEÑAL RECIBIDA
        self.toolbar3 = NavigationToolbar(self.grafica3, self)
            
        self.grafica4 = plt_received_signal2(t, self.muestras.real, t, self.muestras.imag) #PASA LAS VARIABLES PARA CONSTRUIR LA SEÑAL ORIGINAL RECIBIDA
        self.toolbar4 = NavigationToolbar(self.grafica4, self)
            

        self.ui.DEPlayout.addWidget(self.grafica1)
        self.ui.DEPlayout.addWidget(self.toolbar1)
        #self.ui.SRlayout.addWidget(self.grafica2)
        #self.ui.SRlayout.addWidget(self.toolbar2)
        self.ui.Constlayout.addWidget(self.grafica3)
        self.ui.Constlayout.addWidget(self.toolbar3)
        self.ui.recBBlayout.addWidget(self.grafica4)
        self.ui.recBBlayout.addWidget(self.toolbar4)

    def get_buffer_sdr(self):
        print("Realtime buffer started")
        margen = 4
        while True:
            if not self.stop_realtime_flag:
                self.buffer_plot = self.sdr.rx()
                #resultado = np.where(~(self.buffer_plot <=margen) | ~(self.buffer_plot >=-margen) | ~(self.buffer_plot <=margen) | ~(self.buffer_plot >=-margen))
                
                #if len(resultado) >= 2:
                    #start = resultado[0][0]
                    #end = resultado[0][-1:]
                    #end = int(end[0])
                    #resultado_interes = self.muestras[start:end]
                    #self.muestras = np.append(self.muestras, resultado_interes)
                
                self.muestras = np.append(self.muestras, self.buffer_plot)
                self.buffer_ready_flag = True
            else:
                self.buffer_ready_flag = False
                print("Realtime Buffer Stopped")
                break
     
    def realtime_plot(self):
        print("Realtime plotting started")
        while True:
            if not self.stop_realtime_flag:
                if self.buffer_ready_flag:
                    self.x1 = (np.arange(len(self.buffer_plot)) / self.fsample) + self.x1[-1:] #con el fsample lo pasas a dominio temporal
                    self.y1 = self.buffer_plot.real
        
                    self.y2 = self.buffer_plot.imag
                    self.x2 = self.buffer_plot.real
        
                    self.plot2 = self.buffer_plot[:16384]
                    #self.y3, self.x3, self.a = plt.magnitude_spectrum(self.plot2, Fs = fsample, scale = 'linear')
                    self.y3 = np.abs(np.fft.fftshift(np.fft.fft(self.plot2)))
                    self.x3 = np.linspace(self.fsample/-2, self.fsample/2, len(self.y3)) / 1e3 #kHz
        
                    self.data_line1.setData(self.x2, self.y2)  # Update the data. CONSTELATION
                    self.data_line3.setData(self.x3, self.y3)  # Update the data. DEP
                    self.data_line4.setData(self.x1, self.y1)  # Update the data. SIGNAL RECEIVED
                    
                    self.buffer_ready_flag = False
            else:
                print("Realtime plotting Stopped")
                self.buffer_ready_flag = False
                break

    def start_rx(self, frequency_carrier, fsample, tsimb, buffer, umbrales, umbrales_interpolate, umbrales_interpolate_i, regiones, bits_save, nsimb, esquema):
        
        self.buffer_ready_flag = False
        self.stop_realtime_flag = False

        # Clear buffer just to be safe
        for i in range (0, 10):
           samples = self.sdr.rx()
        
        #Dominio temporal para gráficas
        #t = np.arange(0, len(samples)/fsample, 1/fsample)
        t = np.arange(buffer) / fsample
        
        if len(t) > len(samples):
            t = t[:-1]
            
        print(len(t))
        
        self.x = t
        self.x1 = self.x
        self.y = self.sdr.rx().real
        
        pen1 = pg.mkPen(color=(255, 0, 0), style = QtCore.Qt.NoPen)
        pen2 = pg.mkPen(color=(255, 0, 0))  
        
        self.ui.Constlayout.addWidget(self.graphWidget) 
        self.data_line1 =  self.graphWidget.plot(self.x, self.y, pen=pen1, symbol='+', symbolSize=5, symbolBrush=('b'))
        
        #self.ui.SRlayout.addWidget(self.graphWidget_2)
        #self.data_line2 =  self.graphWidget_2.plot(self.x, self.y, pen=pen2)
        
        self.ui.DEPlayout.addWidget(self.graphWidget_3)
        self.data_line3 =  self.graphWidget_3.plot(self.x, self.y, pen=pen2)

        self.ui.recBBlayout.addWidget(self.graphWidget_4)
        self.data_line4 =  self.graphWidget_4.plot(self.x, self.y, pen=pen2)
        
        self.muestras = np.array([], dtype=complex)
        
        if self.reception_initiated == False:
            self.reception_initiated = True
            #MainFunctions.plt_signal_real_time(self, t, samples.real, fsample)
            
            #Creo que va a ser mejor tener el buffer en hilo normal, y el plot en hilo controlador por timer cada 30ms por ejemplo
            self.realtime_buffer = threading.Thread(target=MainFunctions.get_buffer_sdr, args=(self,), daemon=True)
            print("Se creo hilo buffer")
            self.realtime_plot = threading.Thread(target=MainFunctions.realtime_plot, args=(self,), daemon=True)
            print("Se creo hilo plot")
            
            self.realtime_buffer.start()
            self.realtime_plot.start()
            
            #self.timer.setInterval(10)
            #self.timer.timeout.connect(lambda: MainFunctions.update_plot_data(self, buffer, fsample))
            #self.timer.start()
            print("Se paso el codigo de los Threads")
            
######################################################################################################## REAL TIME BUTTONS
            #STOP RECEPTION
            self.ui.stoprecBtn.clicked.connect(lambda: MainFunctions.real_time_plt_stopped(self, fsample, tsimb, umbrales, umbrales_interpolate, umbrales_interpolate_i, regiones, bits_save, nsimb, esquema))
        
            #DATA SIGNAL RECEIVED 
            #self.ui.SRBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_10))
      
            #DEP
            self.ui.DEPBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11))

            #CONSTELATION
            self.ui.ConstBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_9))
            
        else:
            self.ui.DEPlayout.itemAt(0).widget().deleteLater()
            self.ui.DEPlayout.itemAt(1).widget().deleteLater()
            #self.ui.DEPlayout.removeWidget(self.grafica1)
            #self.ui.DEPlayout.removeWidget(self.toolbar1)

            #self.ui.SRlayout.removeWidget(self.grafica2)
            #self.ui.SRlayout.removeWidget(self.toolbar2)

            self.ui.Constlayout.itemAt(0).widget().deleteLater()
            self.ui.Constlayout.itemAt(1).widget().deleteLater()
            #self.ui.Constlayout.removeWidget(self.grafica3)
            #self.ui.Constlayout.removeWidget(self.toolbar3)

            self.ui.recBBlayout.itemAt(0).widget().deleteLater()
            self.ui.recBBlayout.itemAt(1).widget().deleteLater()
            #self.ui.recBBlayout.removeWidget(self.grafica4)
            #self.ui.recBBlayout.removeWidget(self.toolbar4)

            self.ui.finalInfo_2.setText("")           
            
            #MainFunctions.plt_signal_real_time(self, t, samples.real, fsample)
            self.timer.setInterval(10)
            self.timer.timeout.connect(lambda: MainFunctions.update_plot_data(self, buffer, fsample))
            self.timer.start()
            
######################################################################################################## REAL TIME BUTTONS
            #STOP RECEPTION
            self.ui.stoprecBtn.clicked.connect(lambda: MainFunctions.real_time_plt_stopped(self, fsample, tsimb, umbrales, umbrales_interpolate, umbrales_interpolate_i, regiones, bits_save, nsimb, esquema))
        
            #DATA SIGNAL RECEIVED 
            #self.ui.SRBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_10))
      
            #DEP
            self.ui.DEPBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11))

            #CONSTELATION
            self.ui.ConstBtn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_9))



    def plt_signal_real_time(self, t, samples, fsample):
        
        self.timer.setInterval(10)
        self.timer.timeout.connect(lambda: MainFunctions.update_plot_data(self, buffer, fsample))
        self.timer.start()
        


    def update_plot_data(self, buffer, fsample):
        self.plot = self.sdr.rx()
        
        #self.x = self.x[1:]  # Remove the first y element.
        #self.x = np.append(self.x, self.x[-1] + 1/fsample)  # Add a new value 1 higher than the last.
        #self.y = np.append(self.y, samples[:-10])  # Add a new random value.
        
        #Para graficar en banda base, solo parte real y en muestras, no dominio tiempo definido
        self.x1 = (np.arange(buffer) / fsample) + self.x1[-1:] #con el fsample lo pasas a dominio temporal
        self.y1 = self.plot.real
        
        self.y2 = self.plot.imag
        self.x2 = self.plot.real
        #print(self.y)
        
        self.plot2 = self.plot[:16384]
        #self.y3, self.x3, self.a = plt.magnitude_spectrum(self.plot2, Fs = fsample, scale = 'linear')
        self.y3 = np.abs(np.fft.fftshift(np.fft.fft(self.plot2)))
        self.x3 = np.linspace(self.fsample/-2, self.fsample/2, len(self.y3)) / 1e3 #kHz
        #self.y3 = self.y3/len(self.plot2)
        
        self.data_line1.setData(self.x2, self.y2)  # Update the data. CONSTELATION
        #self.data_line2.setData(self.x1, self.y1)  # Update the data. SIGNAL RECEIVED
        self.data_line3.setData(self.x3, self.y3)  # Update the data. DEP
        self.data_line4.setData(self.x1, self.y1)  # Update the data. SIGNAL RECEIVED
        
        self.muestras = np.append(self.muestras, self.plot)
        
        """
        umbral = 4
        resultado = np.where(~(self.plot.real <=margen) | ~(self.plot.real >=-margen) | ~(self.plot.imag <=margen) | ~(self.plot.imag >=-margen))
        start = resultado[0][0]
        end = resultado[0][-1:]
        end = int(end[0])

        self.muestras = np.append(self.muestras,self.plot[start:end])

        print('muestras es ', self.muestras)
        plt.cla() #Limpio memoria de los plots, esto es una prueba.
        """


    def configure_reception_signal(self, gain_rx, frequency_carrier, fsample, buffer):
    
        if self.reception_configured == False:
            self.reception_configured = True

            try:
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

            except:
                self.reception_configured = False
                self.ui.simWarnTxt.setText("Hace falta conectar el módulo ADALM - PLUTO")

#####################################################################################################################################################
#####################################################################################################################################################

class plt_bits_coded(FigureCanvas):
     
    def __init__(self, y, x, tbit, parent = None):        
        self.fig , self.ax = plt.subplots()
        super().__init__(self.fig)
    
        plt.plot(x[0:40000], y[0:40000])
        plt.grid()
        self.ax.set_title("Primeros bits que componen el mensaje (tbit aprox = " + str(tbit) + ")")
        #self.ax.set_ylabel("Amplitud (Referencial)")
        #self.ax.set_xlabel("Tiempo")

        #self.ax.plot()
        #self.ax.grid()
        
        
class plt_modulated_signal(FigureCanvas):
     
    def __init__(self, x, y, parent = None):  
        self.fig , self.ax = plt.subplots()
        super().__init__(self.fig)
        
        plt.magnitude_spectrum(x, Fs = y, scale = 'linear', Fc = 0)
        
        #self.ax.plot()
        #self.ax.grid()
            
class plt_modulated_signal2(FigureCanvas):
     
    def __init__(self, x, y, x2, y2, parent = None):  
        self.fig , self.ax = plt.subplots()
        super().__init__(self.fig)
        
        self.ax.plot(x, y, x2, y2)
        self.ax.grid()

class plt_modulated_signal3(FigureCanvas):
     
    def __init__(self, x, y, parent = None):  
        self.fig , self.ax = plt.subplots()
        super().__init__(self.fig)
        
        self.ax.plot(x, y, "*", linewidth = 58)
        self.ax.grid()

class plt_modulated_signal4(FigureCanvas):
     
    def __init__(self, x, y, parent = None):  
        self.fig , self.ax = plt.subplots()
        super().__init__(self.fig)
        
        self.ax.plot(x, y)
        self.ax.grid()


###############################################################################################

class plt_received_signal(FigureCanvas):
     
    def __init__(self, x, y, parent = None):  
        self.fig , self.ax = plt.subplots()
        super().__init__(self.fig)
        
        plt.magnitude_spectrum(x, Fs = y, scale = 'linear')
        
        #self.ax.plot(x, y)
        #self.ax.grid()
        
class plt_received_signal2(FigureCanvas):
     
    def __init__(self, x, y, x2, y2, parent = None):  
        self.fig2 , self.ax2 = plt.subplots()
        super().__init__(self.fig2)
        #self.fig2.clf()
        #self.fig2.cla()
        #self.fig2.close()
        
        self.ax2.plot(x, y, x2, y2)
        self.ax2.grid()
        
class plt_received_signal3(FigureCanvas):
     
    def __init__(self, x, y, parent = None):  
        self.fig3 , self.ax3 = plt.subplots()
        super().__init__(self.fig3)
        #self.fig3.clf()
        #self.fig3.cla()
        #self.fig3.close()
        
        self.ax3.plot(x, y, "*", linewidth = 58)
        self.ax3.grid()
        
class plt_received_signal4(FigureCanvas):
     
    def __init__(self, x, y, parent = None):  
        self.fig4 , self.ax4 = plt.subplots()
        super().__init__(self.fig4)
        #self.fig4.clf()
        #self.fig4.cla()
        #self.fig4.close()        
        
        self.ax4.plot(x, y)
        self.ax4.grid()
