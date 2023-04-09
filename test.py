import matplotlib.pyplot as plt
import numpy as np
import time
import math

now = time.time()

f = open('ave.jpg','rb')
original = f.read()
f.close()

after = time.time()

print('\nTiempo f.read(): ',after-now)


now = time.time()

img_np = np.fromfile('ave.jpg', dtype=np.uint8)

after = time.time()

print('Tiempo fromfile numpy:', after-now)

print('')
print(img_np[:10])
print(original[:10])

#if img_np == original:
#	print('Son iguales <3')

print('')
print('Ahora viene conversión a bits de la imagen')

bits_arreglo = ''

#bits_arreglo2 = np.empty((118848),dtype=str)
#print(bits_arreglo2.shape)
bits_arreglo2= []

now = time.time()

#Colocando los bits como un string largo, con bin
for byte in np.nditer(img_np):
	bits_arreglo =bits_arreglo + (bin(byte)[2:].zfill(8))
	#int(bin(byte),2)

after = time.time()

print('Tiempo conversión con bin y string: ',after-now)
print('Cantidad de bits: ',len(bits_arreglo))

now = time.time()

"""
#Colocando los bits como un arreglo de columnas bool, con bin

for byte in np.nditer(img_np.T):
	bits_arreglo2.append((bin(byte)[2:].zfill(8)))
	#int(bin(byte),2)

#res = ''.join(bits_arreglo2)
after = time.time()

print('Tiempo conversión con bin y arreglo: ',after-now)
"""

print('Primeros 10 bits: ',bits_arreglo[:10])
print('Ultimos 10 bits: ',bits_arreglo[-10:])
#print(bits_arreglo)



print('\nBITS EN TIEMPO\n')
#=================================================
#Conversión a símbolos en tiempo
now = time.time()

fsample=100
tbit=1 #segundos
dt = 1/fsample
nbits = len(bits_arreglo)

t = np.arange(0,np.multiply(tbit,nbits),dt)
print('Time domain shape: ',t.shape)

N = t.size
print('Cantidad de bits en bits_arreglo: ',len(bits_arreglo))
print('tbit*nbits/dt, cantidad de muestras time domain: ',tbit*nbits/dt)
print('tbit*bits: ',tbit*nbits)
print('Cantidad muestras time domain: ',N)
print('Cantidad muestras que ocupa un bit para ocupar tbit: ',math.ceil(tbit/dt))

bit1 = np.ones(math.ceil(tbit/dt), dtype=int)
bit0 = np.zeros(math.ceil(tbit/dt), dtype=int)

print('Shape bit0: ',bit0.shape)

bits_signal = np.empty((nbits,math.ceil(tbit/dt)), dtype=int)

print('Shape bits_signal: ',bits_signal.shape)

#Convierto el string a un arreglo numpy, verificar si esto toma más tiempo o no
#bits_arreglo = np.fromiter(bits_arreglo, dtype=int)
#print('Lista numpy:',bits_arreglo)
#Revisé y no parece ser más rápido, más bien un poco más lento

cont = 0
for bit in bits_arreglo:
    if bit == '1':
        bits_signal[cont] = bit1
    else:
        bits_signal[cont] = bit0
    cont += 1

bits_signal=bits_signal.reshape(N)
print('bits_signal shape reshaped',bits_signal.shape)
plt.plot(t,bits_signal)
after = time.time()
print('Tiempo total graficación:',after-now)
print('Será más rápido si no se imprimen tantas cosas, obviamente')
plt.show()
