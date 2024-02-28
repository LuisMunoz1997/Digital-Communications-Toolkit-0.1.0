#Graph constellation and thresholds

import numpy as np
import random
from random import randint
from matplotlib import pyplot as plt
import math
from scipy import interpolate
from scipy import signal

def slope(a):
    radians = a*np.pi/180
    return np.tan(radians)

def threshold_defined(nsimb, esquema): #Amplificador en algunos casos suma y en otros multiplica
    real_domain = np.linspace(-20,20,num=2, dtype=complex) #Dominios real e imag
    imag_domain = np.linspace(-20j,20j,num=2, dtype=complex) #Para simular la formula y = mx + c de cierta forma
    real_circle = np.linspace(0,1, num=16, dtype=complex)

    if nsimb == 2: # 1 Pendiente, 2 X y 3 Y
        if esquema == 4: #Inclinada 
            umbral1 = imag_domain * slope(45) + real_domain
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
            umbral1 = imag_domain * slope(45) + real_domain
            umbral2 = imag_domain * -slope(45) + real_domain
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
            umbral3 = imag_domain + real_domain * 0 + 3.5
            umbrales = np.array([umbral1, umbral2, umbral3])
        else:
            print("ERROR SELECCIÓN")
        
    elif nsimb == 8:
        if esquema == 1: #2 Rectas Ejes y 1 Circulo
            umbral1 = imag_domain * 0 + real_domain
            umbral2 = imag_domain + real_domain * 0
            umbral3 = 2.5 * np.exp(2j*np.pi*real_circle) #Pendiente con los circulos y la detección
            umbrales = np.array([umbral1, umbral2, umbral3], dtype = object)
        elif esquema == 2: #4 Diagonales. Sirve para 8psk y un 8qam
            umbral1 = imag_domain * slope(45+22.5) + real_domain
            umbral2 = imag_domain * slope(45-22.5) + real_domain
            umbral3 = imag_domain * slope(-45-22.5) + real_domain
            umbral4 = imag_domain * slope(-45+22.5) + real_domain
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
            umbral1 = imag_domain * slope(angles_reference_16[1]+11.25) + real_domain #+11.25 de umbral para cada dirección, por simbolo
            umbral2 = imag_domain * slope(angles_reference_16[1]-11.25) + real_domain
            umbral3 = imag_domain * slope(angles_reference_16[3]+11.25) + real_domain
            umbral4 = imag_domain * slope(angles_reference_16[3]-11.25) + real_domain
            umbral5 = imag_domain * slope(angles_reference_16[5]+11.25) + real_domain
            umbral6 = imag_domain * slope(angles_reference_16[5]-11.25) + real_domain
            umbral7 = imag_domain * slope(angles_reference_16[7]+11.25) + real_domain
            umbral8 = imag_domain * slope(angles_reference_16[7]-11.25) + real_domain            
            umbrales = np.array([umbral1, umbral2, umbral3, umbral4, umbral5, umbral6, umbral7, umbral8])
        elif esquema == 2: #4 Diagonales 1 Circulo R=2.5
            reference_domain_16 = np.arange(0,8)
            reference_16 = np.exp(2j*np.pi*reference_domain_16/8)
            angles_reference_16 = np.angle(reference_16, deg=True)
            umbral1 = imag_domain * slope(angles_reference_16[1]+22.5) + real_domain #+-22.5° de umbral
            umbral2 = imag_domain * slope(angles_reference_16[1]-22.5) + real_domain
            umbral3 = imag_domain * slope(angles_reference_16[3]+22.5) + real_domain
            umbral4 = imag_domain * slope(angles_reference_16[3]-22.5) + real_domain
            umbral5 = 2.5 * np.exp(2j*np.pi*real_circle)
            umbrales = np.array([umbral1, umbral2, umbral3, umbral4, umbral5], dtype=object)
        elif esquema == 3:
            reference_domain_16 = np.arange(0,8)
            reference_16 = np.exp(2j*np.pi*reference_domain_16/8)
            angles_reference_16 = np.angle(reference_16, deg=True)
            umbral1 = imag_domain * slope(angles_reference_16[1]+22.5) + real_domain #+-22.5° de umbral
            umbral2 = imag_domain * slope(angles_reference_16[1]-22.5) + real_domain
            umbral3 = imag_domain * slope(angles_reference_16[3]+22.5) + real_domain
            umbral4 = imag_domain * slope(angles_reference_16[3]-22.5) + real_domain
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






def create_constellation_tx(nsimb,esquema, qam8_selector = 1, qam16_selector = 1): 
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



print("GRAFICAR UMBRALES Y CONSTELACIÓN")
print("======================================")

print("Selección de parámetros:")
print("")
print("Nsimb = 2 - Esquema = 3 - Umbral Vertical X=0 - BPSK")
print("Nsimb = 2 - Esquema = 2 - Umbral Vertical X=0.5 - OOK")
print("Nsimb = 2 - Esquema = 1 - Umbral Vertical X=1.5 - 2ASK")
print("Nsimb = 2 - Esquema = 4 - Umbral Inclinad0 - FSK - NO SE SI GRAFICAR ESTA")
print("")
print("Nsimb = 4 - Esquema = 1 - 2 Diagonales - QPSK EJES")
print("Nsimb = 4 - Esquema = 2 - 2 Rectas Ejes - QPSK NORMAL")
print("Nsimb = 4 - Esquema = 3 - 2 Rectas Ejes -  4ASK")
print("(Esquema 3 y 4 son el mismo umbral, se puede usar uno para implementar 4ASK Bipolar si queremos)")
print("")
print("Nsimb = 8 - Esquema = 1 - 2 Ejes y 1 Circulo - 8QAM Diagonal")
print("Nsimb = 8 - Esquema = 2 - 4 Diagonales - 8PSK")
print("Nsimb = 8 - Esquema = 3 - 2 Ejes y 1 Circulo - 8QAM Circular")
print("Nsimb = 8 - Esquema = 4 - 3 Verticales 1 Horizontal - 8QAM rectangular")
print("Nsimb = 8 - Esquema = 5 - 7 Rectas Verticales - 8ASK Bipolar")
print("")
print("Nsimb = 16 - Esquema = 1 - 8 Diagonales - 16PSK")
print("Nsimb = 16 - Esquema = 2 - 4 Diagonales y 1 Circulo R=2.5 - 16QAM Circular")
print("Nsimb = 16 - Esquema = 3 - 4 Diagonales y 1 Circulo R=1.5 - 16QAM Diagonal")
print("Nsimb = 16 - Esquema = 4 - 3 Horizontales 4 Verticales - 16QAM Rectangular")
print("")
print("====================================")

print("Ingrese Nsimb: ")
nsimb = int(input())
print("Ingrese Esquema: ")
esquema = int(input())

if nsimb == 2:
    bits = ['0', '1']
    
    umbrales = threshold_defined(nsimb, esquema)
    constellation = create_constellation_tx(nsimb,esquema)
    
    for symbol in constellation:
        plt.plot(np.real(symbol), np.imag(symbol), '.', color='blue', markersize=20) #Markersize define el tamaño del punto
        
    bits_index = 0
    for symbol in constellation:
        plt.text(symbol.real, symbol.imag+0.2, '{}'.format(bits[bits_index]), horizontalalignment='center', fontsize='large', bbox = dict(facecolor = 'white'))
        bits_index += 1
        
    for umbral in umbrales:
	    plt.plot(np.real(umbral), np.imag(umbral),'-', color='green')
	    
	    
	        
elif nsimb == 4:
    bits = ['00', '01', '10', '11']
    
    umbrales = threshold_defined(nsimb, esquema)
    constellation = create_constellation_tx(nsimb,esquema)

    for symbol in constellation:
        plt.plot(np.real(symbol), np.imag(symbol), '.', color='blue', markersize=20) #Markersize define el tamaño del punto
        
    bits_index = 0
    for symbol in constellation:
        plt.text(symbol.real, symbol.imag+0.2, '{}'.format(bits[bits_index]), horizontalalignment='center', fontsize='large', bbox = dict(facecolor = 'white'))
        bits_index += 1
        
    for umbral in umbrales:
	    plt.plot(np.real(umbral), np.imag(umbral),'-', color='green')	     



elif nsimb == 8:
    bits = ['111', '110', '010', '011', '001', '000', '100', '101']
    
    umbrales = threshold_defined(nsimb, esquema)
    
    if esquema == 1:
        constellation = create_constellation_tx(nsimb,3,qam8_selector = 3,qam16_selector = 1)
    elif esquema == 2:
        constellation = create_constellation_tx(nsimb,2)
    elif esquema ==3:
        constellation = create_constellation_tx(nsimb,3,qam8_selector = 2,qam16_selector = 1)
        umbrales = threshold_defined(nsimb, 2)
    elif esquema == 4:
        constellation = create_constellation_tx(nsimb,3,qam8_selector = 1,qam16_selector = 1)
    elif esquema == 5:
        constellation = create_constellation_tx(nsimb,1)
        
    legend = []
    for index,umbral in enumerate(umbrales):
	    plt.plot(np.real(umbral), np.imag(umbral),'-', color='green')
	    legend.append("umbral {}".format(index))
        
    for symbol in constellation:
        plt.plot(np.real(symbol), np.imag(symbol), '.', color='blue', markersize=20) #Markersize define el tamaño del punto
        
    bits_index = 0
    for symbol in constellation:
        plt.text(symbol.real, symbol.imag+0.2, '{}'.format(bits[bits_index]), horizontalalignment='center', fontsize='large', bbox = dict(facecolor = 'white'))
        bits_index += 1
        	



elif nsimb == 16:
    bits = ['0000', '1000', '1001', '1011', '1010', '1110', '1111', '1101', '1100', '0100', '0101', '0111', '0110', '0010', '0011', '0001']

    umbrales = threshold_defined(nsimb, esquema)

    if esquema == 1:
        constellation = create_constellation_tx(nsimb,1)
    elif esquema == 2:
        constellation = create_constellation_tx(nsimb,2,qam8_selector = 1,qam16_selector = 2)
    elif esquema == 3:
        constellation = create_constellation_tx(nsimb,2,qam8_selector = 1,qam16_selector = 3)
    elif esquema == 4:
        constellation = create_constellation_tx(nsimb,2,qam8_selector = 1,qam16_selector = 1)
        
    legend = []
    for index,umbral in enumerate(umbrales):
	    plt.plot(np.real(umbral), np.imag(umbral),'-')
	    legend.append("umbral {}".format(index))

    for symbol in constellation:
        plt.plot(np.real(symbol), np.imag(symbol), '.', color='blue', markersize=20) #Markersize define el tamaño del punto
        
    bits_index = 0
    for symbol in constellation:
        plt.text(symbol.real, symbol.imag+0.2, '{}'.format(bits[bits_index]), horizontalalignment='center', fontsize='large', bbox = dict(facecolor = 'white'))
        bits_index += 1
        

#plt.legend(legend)

if np.max(constellation.real) >= np.max(constellation.imag):
    max_limit = abs(np.max(constellation.real)) + 1
else:
    max_limit = abs(np.max(constellation.imag)) + 1
    
plt.ylim(-max_limit,max_limit)
plt.xlim(-max_limit,max_limit)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.grid(linestyle = '--')

plt.show()
