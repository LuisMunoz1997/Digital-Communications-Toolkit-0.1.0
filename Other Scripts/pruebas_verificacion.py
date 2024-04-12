import numpy as np

def string_to_bits(message): #Cambiar esta funcion en programa principal
    message = [ord(c) for c in message]
    message = np.asarray(message, dtype=np.uint8)
    message = np.unpackbits(message)
    return message

def bits_to_string(bits):
    binary_string = ''.join(bits)
    text = ''.join((chr(int(binary_string[i:i+8],2))) for i in range(0,len(binary_string),8))
    return text


string ='G Ó'
bits = string_to_bits(string)

#Aca se pueden añadir errores intencionales a los bits "recibidos"
prueba = np.array(['0', '1', '0', '0', '0', '1', '1', '1','0','0','1','0','0','0','0','0','1','1','0','1','0','0','1','1'])

string_prueba = bits_to_string(prueba)

print('String: ', string)
print('En Bits: ', bits)
print('Bits diseñados prueba: ',prueba)
print('String resultado:', string_prueba)

r_prueba = [ord(c) for c in string_prueba]
print('Ascii del resultado: ',r_prueba)

#Segun estas pruebas, parece que puedo comprobar errores comparando la cantidad de strings con la cantidad de valores ascii en el arreglo cuando se devuelve el cambio con ord(char). Si estos valores no son iguales, hubo algun error. Pero, hay otros errores a tomar en cuenta. Seguir pruebas.

#Parece que tambien se puede comprobar que el valor, por algun motivo, no salga de 0 o 255, pero esto no deberia suceder porque el ord o chr darian error. Ver mejor que pasa con ejemplos de recepciones reales.

