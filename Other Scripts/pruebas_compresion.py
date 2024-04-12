import numpy as np
import zipfile
from PIL import Image
import io

#Conclusiones:
#Opciones: 
#Bajar calidad a imagen y enviar completa, o comprimirla antes y enviar archivo zip
#Guardar pixeles imagen en archivo .bin (insertando valores ancho y alto primeros dos indices), comprimir archivo y enviarlo
#Buscar algun algoritmo de compresión y descompresión a nivel de bits (bits redundantes por ejemplo)

#Bajar calidad a imagen y obtener arreglo pixeles
image = Image.open("pajarito.jpg")
ancho, altura = image.size[0], image.size[1]
image.save("pajarito_low.jpg",quality=15,optimize=False,progressive=True)
pixels = np.array(image)
image.close()
print("dimensiones pixeles:", pixels.shape)
pixels = pixels.flatten()
print("pixels flatten:",len(pixels))
print(pixels[0:20])

#Pasas pixeles de 8 a 64 bits
#pixels_64 = pixels.reshape((-1, 64)).astype(np.uint8) #Si estan en bits y no uint8
#pixels_64 = np.packbits(pixels_64, bitorder='little').view(np.uint64)
#pixels_64 = pixels.view(np.uint64)
#print("pixels_64:", pixels_64[0:30])
#print("longitud pixels 64:", len(pixels_64))
#print("longitud de vuelta a 8 bits:",len(pixels_64.view(np.uint8)))

#Comprimir archivo imagen normal
zout = zipfile.ZipFile("foto_comprimida.zip", "w", zipfile.ZIP_LZMA)
zout.write("pajarito_low.jpg")
zout.close()

#comprimir pixeles? Parece que da igual pasarlos a 64 bits si luego al guardar en archivo para comprimirlo pesa lo mismo (antes de comprimir)
pixels.tofile("pixels.bin")

pixels_bytes = np.fromfile("pixels.bin")

print('pixels del bin:', len(pixels_bytes))
print(pixels_bytes[0:5])
zout2 = zipfile.ZipFile("pixels_comprimida.zip", "w", zipfile.ZIP_LZMA)
zout2.write('pixels.bin')
zout2.close()
pixeles_compress = np.fromfile("pixels_comprimida.zip")
print("pixels comprimido:", len(pixeles_compress))
print("pixeles comprimido type sin cambiar:")
print(pixeles_compress[0:10])
print("pixels comprimido type uint8:")
print(pixeles_compress.view(np.uint8)[0:10])
print("pixels compreso:",len(pixeles_compress.view(np.uint8)))
print("Entonces, comprimiendo pixeles a enviar se comprimen:", len(pixels) - len(pixeles_compress.view(np.uint8)))
print("")
print("Sin comprimir pixels sino imagen bajada de calidad")

#Pasar a arreglo numpy archivo sin comprimir y archivo comprimido
archivo = np.fromfile("pajarito.jpg", dtype=np.uint8)
compress = np.fromfile("foto_comprimida.zip", dtype=np.uint8)

try:
    with zipfile.ZipFile('foto_comprimida.zip', 'r') as zip_ref:
        zip_ref.extractall()
except Exception as e:
    print(e)
    
#Antes de descomprimir, forzar en recepción bytes de inicio y final de archivo zip? Luego al descomprimir forzar bytes inicio y final archivo jpg?



print("original:",archivo[0:25])
#print(np.where(archivo==255)[0])
#print(len(np.where(archivo==255)[0]))
print("Sin comprimir:",len(archivo))
print("comprimido:",compress[0:20])
print("Compress: ",len(compress))
print("")
print("Descomprimiendo pixels compreso")

try:
    with zipfile.ZipFile('pixels_comprimida.zip', 'r') as zip_ref:
        zip_ref.extractall(path='pixeles_descomprimida')
except Exception as e:
    print(e)

pixels_recuperado = np.fromfile("/home/lubuntu/Desktop/pruebas_compresion/pixeles_descomprimida/pixels.bin", dtype=np.uint8)
print("cantidad recuperada:", len(pixels_recuperado))
pixels_recuperado = pixels_recuperado.reshape(altura,ancho,3)

image = Image.fromarray(pixels_recuperado, mode="RGB")
image.show()
image.close()

