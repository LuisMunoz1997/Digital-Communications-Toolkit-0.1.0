import adi
from scipy import interpolate
from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
import math
from commpy.filters import rrcosfilter
import random
from random import randint
from scipy.optimize import fsolve #fsolve retorna las raices (no lineales) de ecuaciones de forma f(x)=0 dado un estimado inicial


#=====================================================================================================
#FUNCIONES TX

#Crea constelacion con información de fase y cuadratura dada por usuario. AÑADIR A PROGRAMA PRINCIPAL
def create_constellation_tx_user(nsimb, point1 = 0, point2 = 0, point3 = 0, point4 = 0):
    if nsimb == 2:
        constellation = np.array([point1,point2])
    elif nsimb == 4:
        constellation = np.array([point1,point2,point3,point4])
    else:
        print("ERROR CREACION CONSTELACION USUARIO")
    return constellation
    
#MISMA FUNCION PRESENTA YA EN EL PROGRAMA PARA TX - Se quitaron partes para +2 simbolos para ahorrar espacio. NO MODIFICAR EN PROGRAMA PRINCIPAL SUSTITUYENDO ESTA FUNCION CON LA QUE YA ESTA
def prepare_to_send(message, nsimb, constellation):
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

        return bits_array

#Funciones de TX que tambien están presentes en el programa principal. NO MODIFICAR EN EL MISMO

def pulse_shape(samples_symbols, tsim, fsample, beta=0.35):
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
        
def add_preamble(samples, fsample = 522000, freq = 80e3, n_samples = 100):
    preambulo = 0.5*np.exp(2j*np.pi*freq*np.arange(n_samples) / fsample)
    return np.append(preambulo,samples)

#Dividir por partes la señal a enviar. Cada parte con su preámbulo. Se divide por cantidad de símbolos.
def define_parts(samples_symbols, tsim, fsample, n_sym_parts = 100): #Recibe los pulsos de los simbolos sin añadir tiempo simb creo
    #Crea arreglo que cada volumna contiene un arreglo que representa la parte a enviar
    packets = np.split(samples_symbols, np.arange(n_sym_parts,len(samples_symbols),n_sym_parts))
        
    #Por cada parte, se realiza el pulse shape y se le agrega un preambulo. Se prueba con 1 solo preambulo con duration tsimb tambien a ver.
    for inx,part in enumerate(packets):
         print('Preparing part {} of {}'.format(inx, len(packets)-1))
         packets[inx] = MainFunctions.add_preamble(self,MainFunctions.pulse_shape(self, part, tsim, fsample, beta=0.35), fsample = 522000, freq = 80e3, n_samples = 100)
            
    return packets

#FIN FUNCIONES PARA TX USUARIO
#=============================================================================================

#=============================================================================================
#FUNCIONES PARA DEFINICION DE PARAMETROS RX USUARIO

def slope(a):
    radians = a*np.pi/180
    return np.tan(radians)

def threshold_user(nsimb, selector1="vertical", selector2="vertical", offset_x=0, offset_y=0, angle=0, offset_x2=0, offset_y2=0, angle2=0): #Pasar a programa principal
    pass
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
        umbral = imag_domain * slope(angle) + real_domain + 1*offset_x + 1j*offset_y
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
        
        
def interpolate_umbrales(umbrales): #Función ya en programa principal
    umbrales_interpolate = np.array([])
    umbrales_interpolate_i = np.array([])
    for umbral in umbrales:
        umbrales_interpolate = np.append(umbrales_interpolate, interpolate.interp1d(umbral.real,umbral.imag, fill_value='extrapolate'))
    for umbral in umbrales:
        umbrales_interpolate_i = np.append(umbrales_interpolate_i, interpolate.interp1d(umbral.imag,umbral.real, fill_value='extrapolate'))
    return umbrales_interpolate, umbrales_interpolate_i
    
    
def find_intersection(x1, y1, x2, y2): #Añadir a programa principal, esta función encuentra punto intersección entre dos rectas. Usada para gráfica de regiones creadas por el usuario
    # Create interpolating functions for the data
    f1 = interpolate.interp1d(x1, y1, fill_value='extrapolate')
    f2 = interpolate.interp1d(x2, y2, fill_value='extrapolate')
 

    # Define the overlapping region of the x-values
    x_min = max(min(x1), min(x2))
    x_max = min(max(x1), max(x2))

    # Define a new function as the difference between the two
    def diff(xy):
        x, y = xy
        return [f1(x) - f2(x), f1(x) - y]  # Add y difference as second equation

    # Use fsolve to find the root of the new function within the overlapping region
    x_initial = max(x_min, x1[0])  # Initial guess for x-coordinate

    try:
        intersection = fsolve(diff, [x_initial, f1(x_initial)], xtol=1e-8, args=(), fprime=None, full_output=False)

        # Check if the intersection is within the valid range
        if x_min <= intersection[0] <= x_max:
            # Return intersection point as a complex number
            return complex(intersection[0], intersection[1])

    except Exception as e:
        pass
        print("Error encontrando intersección:")
        print(str(e))
        return False
    return False   
    
#Recibe el arreglo de umbrales y las etiquetas que los identifican. En funcion a estas etiquetas determina las regiones formadas, utilizadas para asignar bits a los símbolos que son recibidos. Agregar al programa principal esta función, en este caso esta grafica, la de abajo hace los check
def graph_regions_user(umbrales, etiquetas):

#Si se crearon 2 umbrales. CORREGIR ACA, PORQUE LO MEJOR ES QUE HAYA 2 O 4 REGIONES ESTRICTAMENTE (es decir, que se intersecten las rectas si hay más de 1)
    if len(umbrales) == 2:
        if etiquetas[0]==1 and etiquetas[1]==1: #Dos lineas verticales
            region1 = '(real_domain.real >= umbrales[0].real) & (real_domain.real >= umbrales[1].real)' #Condicionales PARA LA GRAFICA, no detección
            region2 = '(real_domain.real <= umbrales[0].real) & (real_domain.real <=umbrales[1].real)'
            region3 = '~((region1) & (region2))'
            plt.fill_between(real_domain.real, -20, 20, where = eval(region1), alpha=0.4)
            plt.fill_between(real_domain.real, -20, 20, where = eval(region2), alpha=0.4)
            plt.fill_between(real_domain.real, -20, 20, where = ~(eval(region1)) & ~(eval(region2)), alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2', 'region3'])
    
        elif etiquetas[0]==2 and etiquetas[1]==2: #Dos lineas horizontales
            plt.fill_between(real_domain.real, umbrales[0].imag, umbrales[1].imag, alpha=0.4)
            if umbrales[0][0].imag >= umbrales[1][0].imag:
                plt.fill_between(real_domain.real, umbrales[0].imag, 20, alpha=0.4)
                plt.fill_between(real_domain.real, umbrales[1].imag, -20, alpha=0.4)
            else:
                plt.fill_between(real_domain.real, umbrales[1].imag, 20, alpha=0.4)
                plt.fill_between(real_domain.real, umbrales[0].imag, -20, alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2', 'region3', 'region4'])
        
        elif etiquetas[0]==1 and etiquetas[1]==2 or etiquetas[0]==2 and etiquetas[1]==1: #Linea vertical y linea Horizontal
            point = etiqueta_point
            region1 = '(real_domain.real >= point.real)'
            region2 = '(real_domain.real <= point.real)'
            plt.fill_between(real_domain.real, point.imag, 20, where = eval(region1), alpha=0.4)
            plt.fill_between(real_domain.real, point.imag, -20, where = eval(region1), alpha=0.4)
            plt.fill_between(real_domain.real, point.imag, -20, where = eval(region2), alpha=0.4)
            plt.fill_between(real_domain.real, point.imag, 20, where = eval(region2), alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2', 'region3', 'region4'])
    
        elif etiquetas[0]==1 and etiquetas[1]==3: #Línea vertical junto a una línea inclinada
            point = find_intersection(umbrales[0].real, umbrales[0].imag, umbrales[1].real, umbrales[1].imag)
            region1 = '(real_domain.real >= point.real)'
            region2 = '(real_domain.real <= point.real)'
            plt.fill_between(real_domain.real, umbrales[1].imag, 20, where = eval(region1), alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[1].imag, -20, where = eval(region1), alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[1].imag, -20, where = eval(region2), alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[1].imag, 20, where = eval(region2), alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2', 'region3', 'region4'])
    
        elif etiquetas[0]==3 and etiquetas[1]==1: #Línea inclinada junto a vertical
            point = find_intersection(umbrales[0].real, umbrales[0].imag, umbrales[1].real, umbrales[1].imag)
            region1 = '(real_domain.real >= point.real)'
            region2 = '(real_domain.real <= point.real)'
            plt.fill_between(real_domain.real, umbrales[0].imag, 20, where = eval(region1), alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[0].imag, -20, where = eval(region1), alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[0].imag, -20, where = eval(region2), alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[0].imag, 20, where = eval(region2), alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2', 'region3', 'region4'])
    
        elif etiquetas[0]==3 and etiquetas[1]==3: #Dos lineas inclinadas (Si 90 o 0 grados, puede dar errores, usar lineas verticales u horizontales)
            point = find_intersection(umbrales[0].real, umbrales[0].imag, umbrales[1].real, umbrales[1].imag)
            if point.real != None and point.imag != None: #Se intersectan
                region1 = '(real_domain.real >= point.real)'
                region2 = '(real_domain.real <= point.real)'
                max = np.maximum(umbrales[0].imag,umbrales[1].imag)
                min = np.minimum(umbrales[0].imag,umbrales[1].imag)
                plt.fill_between(real_domain.real, umbrales[0].imag, umbrales[1].imag, where = eval(region1), alpha=0.4)
                plt.fill_between(real_domain.real, umbrales[0].imag, umbrales[1].imag, where = eval(region2), alpha=0.4)
                plt.fill_between(real_domain.real, max, 20, alpha=0.4)
                plt.fill_between(real_domain.real, min, -20, alpha=0.4)
                plt.legend(legend_append + ['region1', 'region2', 'region3', 'region4'])
            else:
                print("Para este caso, solo se permiten rectas que se intersecten")
    else: #Solo se creó 1 umbral
        if etiquetas[0]==1: #Linea vertical
            point = etiqueta_point
            plt.fill_between(real_domain.real, -20, 20, where = real_domain.real >= point.real, alpha=0.4)
            plt.fill_between(real_domain.real, -20, 20, where = real_domain.real <= point.real, alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2'])
    
        elif etiquetas[0]==2: #Linea horizontal
            plt.fill_between(real_domain.real, umbrales[0][0].imag, 20, alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[0][0].imag, -20, alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2'])
    
        elif etiquetas[0]==3: #Linea inclinada
            plt.fill_between(real_domain.real, umbrales[0].imag, 20, alpha=0.4)
            plt.fill_between(real_domain.real, umbrales[0].imag, -20, alpha=0.4)
            plt.legend(legend_append + ['region1', 'region2'])

    
def check_conditions(samples, regiones, bits_save, umbrales, umbrales_i, umbrales_no): #Umbrales de entrada tienen que ser los umbrales interpolados. YA EN PROGRAMA PRINCIPAL
        
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

def check_regions_user(nsimb, samples, etiquetas, umbrales, umbrales_i, umbrales_no): #entran umbrales inter, inter en Y y sin inter
    #Se definen regiones y bits_save para la función ya hecha "check_conditions". PERO me parece que con la funcion "is_inside_sm" formando poligonos con: punto interseccion de los umbrales, punto extremo hacia un lado de un umbral, punto extremo hacia un lado del otro umbral, la función retorna directamente si el punto está dentro de la región formada
    
    #Se trata de dar prioridad al orden 00, 01, 10, 11 empezando por la region izquierda-arriba, luego derecha arriba, luego derecha abajo y asi (priorizando izquierda sobre arriba o abajo parece)
    if nsimb == 2: #2 Regiones formadas por linea vertical u horizontal
        if etiquetas[0] == 1: #Vertical
            regiones = [
                   samples.real < umbrales_no[0][0].real, #0 #Region izquierda es 0
                   samples.real > umbrales_no[0][0].real, #1
                ]
            bits_save = [
                    '0',
                    '1',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
        elif etiquetas[0] == 2: #Horizontal
            regiones = [
                   samples.imag < umbrales_no[0][0].imag, #0 #Region arriba es 0
                   samples.imag > umbrales_no[0][0].imag, #1
                ]
            bits_save = [
                    '0',
                    '1',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
        elif etiquetas[0] == 3: #Inclinada
            regiones = [
                   samples.imag > umbrales[0](samples.real), #0 #Region arriba es 0, dependiendo del angulo de inclinacion, algo subjetivo
                   samples.imag < umbrales[0](samples.real), #1
                ]
            bits_save = [
                    '0',
                    '1',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
    elif nsimb == 4: #2 umbrales
        if etiquetas[0] == 1 and etiquetas[1] == 2: #Linea Vertical con Horizontal
            regiones = [
                   (samples.real < umbrales_no[0][0].real) & (samples.imag > umbrales_no[1][0].imag), #00 Arriba izquierda
                   (samples.real > umbrales_no[0][0].real) & (samples.imag > umbrales_no[1][0].imag), #01 Arriba derecha
                   (samples.real > umbrales_no[0][0].real) & (samples.imag < umbrales_no[1][0].imag), #10 Abajo derecha
                   (samples.real < umbrales_no[0][0].real) & (samples.imag < umbrales_no[1][0].imag), #11 Abajo izquierda
                ]
            bits_save = [
                    '00',
                    '01',
                    '10',
                    '11',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
        elif etiquetas[1] == 1 and etiquetas[0] == 2: #Linea Horizontal con Vertical
            regiones = [
                   (samples.real < umbrales_no[1][0].real) & (samples.imag > umbrales_no[0][0].imag), #00 Arriba izquierda
                   (samples.real > umbrales_no[1][0].real) & (samples.imag > umbrales_no[0][0].imag), #01 Arriba derecha
                   (samples.real > umbrales_no[1][0].real) & (samples.imag < umbrales_no[0][0].imag), #10 Abajo derecha
                   (samples.real < umbrales_no[1][0].real) & (samples.imag < umbrales_no[0][0].imag), #11 Abajo izquierda
                ]
            bits_save = [
                    '00',
                    '01',
                    '10',
                    '11',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
        elif etiquetas[0] == 1 and etiquetas[1] == 3: #Linea Vertical con Inclinada
            regiones = [
                   (samples.real < umbrales_no[0][0].real) & (samples.imag > umbrales[1](samples.real)), #00 Arriba izquierda (subjetivo al angulo)
                   (samples.real > umbrales_no[0][0].real) & (samples.imag > umbrales[1](samples.real)), #01 Arriba derecha
                   (samples.real > umbrales_no[0][0].real) & (samples.imag < umbrales[1](samples.real)), #10 Abajo derecha
                   (samples.real < umbrales_no[0][0].real) & (samples.imag < umbrales[1](samples.real)), #11 Abajo izquierda
                ]
            bits_save = [
                    '00',
                    '01',
                    '10',
                    '11',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
        elif etiquetas[0] == 3 and etiquetas[1] == 1: #Linea Inclinada con Vertical
            regiones = [
                   (samples.real < umbrales_no[1][0].real) & (samples.imag > umbrales[0](samples.real)), #00 Arriba izquierda (subjetivo al angulo)
                   (samples.real > umbrales_no[1][0].real) & (samples.imag > umbrales[0](samples.real)), #01 Arriba derecha
                   (samples.real > umbrales_no[1][0].real) & (samples.imag < umbrales[0](samples.real)), #10 Abajo derecha
                   (samples.real < umbrales_no[1][0].real) & (samples.imag < umbrales[0](samples.real)), #11 Abajo izquierda
                ]
            bits_save = [
                    '00',
                    '01',
                    '10',
                    '11',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
        elif etiquetas[0] == 2 and etiquetas[1] == 3: #Linea Horizontal con Inclinada
            regiones = [
                   (samples.imag > umbrales_no[0][0].imag) & (samples.real < umbrales_i[1](samples.imag)), #00 Arriba izquierda (subjetivo angulo)
                   (samples.imag > umbrales_no[0][0].imag) & (samples.real > umbrales_i[1](samples.imag)), #01 Arriba derecha
                   (samples.imag < umbrales_no[0][0].imag) & (samples.real > umbrales_i[1](samples.imag)), #10 Abajo derecha
                   (samples.imag < umbrales_no[0][0].imag) & (samples.real < umbrales_i[1](samples.imag)), #11 Abajo izquierda
                ]
            bits_save = [
                    '00',
                    '01',
                    '10',
                    '11',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
        elif etiquetas[0] == 3 and etiquetas[1] == 2: #Linea Inclinada con Horizontal
            regiones = [
                   (samples.imag > umbrales_no[1][0].imag) & (samples.real < umbrales_i[0](samples.imag)), #00 Arriba izquierda (subjetivo angulo)
                   (samples.imag > umbrales_no[1][0].imag) & (samples.real > umbrales_i[0](samples.imag)), #01 Arriba derecha
                   (samples.imag < umbrales_no[1][0].imag) & (samples.real > umbrales_i[0](samples.imag)), #10 Abajo derecha
                   (samples.imag < umbrales_no[1][0].imag) & (samples.real < umbrales_i[0](samples.imag)), #11 Abajo izquierda
                ]
            bits_save = [
                    '00',
                    '01',
                    '10',
                    '11',
                ]
            result = np.select(regiones, bits_save, default=random.choice(bits_save))
            
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
                   	(samples.real < point.real) & (samples.imag < umbrales[1](samples.real)) & (samples.imag > umbrales[0](samples.real)), #00 Arriba izquierda (subjetivo angulo)
                    (samples.imag > point.imag) & (samples.real > umbrales_i[1](samples.imag)) & (samples.real < umbrales_i[0](samples.imag)),#01 Arriba derecha
                    (samples.imag < point.imag) & (samples.real < umbrales_i[1](samples.imag)) & (samples.real > umbrales_i[0](samples.imag)) 	#10 Abajo derecha
                    (samples.imag < point.imag) & (samples.real < umbrales[1](samples.imag)) & (samples.real > umbrales[0](samples.imag))	#11 Abajo izquierda
                	]
            	bits_save = [
                    	'00',
                    	'01',
                    	'10',
                    	'11',
                	]
            	result = np.select(regiones, bits_save, default=random.choice(bits_save))                              
        
    return result

umbrales, etiquetas = threshold_user(4, selector1="inclinada", selector2="inclinada", offset_x=3, offset_y=1, angle=33, offset_x2=-1, offset_y2=2, angle2=-43)

umbral1 = umbrales[0][0]
umbral2 = umbrales[1][0]

interpo1 = interpolate.interp1d(umbral1.real,umbral1.imag, fill_value='extrapolate')
interpo2 = interpolate.interp1d(umbral2.real,umbral2.imag, fill_value='extrapolate')

print("Se interceptan en: ", find_intersection(umbral1.real, umbral1.imag, umbral2.real, umbral2.imag))
print("Angulos: \n 1: {} \n 2: {}".format(np.angle(umbral1, deg=True), np.angle(umbral2, deg=True)))
plt.plot(interpo1(umbral1.real), interpo1(umbral1.imag))
plt.plot(interpo2(umbral2.real), interpo2(umbral2.imag))
plt.show()
