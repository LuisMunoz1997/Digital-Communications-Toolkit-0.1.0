from PIL import Image
import numpy as np


def reconstruct_image(header_bytes, pixel_bytes, output_path):
    # Crear una nueva imagen en PIL con base en los bytes de la cabecera
    image = Image.open(io.BytesIO(header_bytes))

    # Convertir los bytes de los datos de los píxeles en un arreglo NumPy
    pixel_data = np.frombuffer(pixel_bytes, dtype=np.uint8)

    # Asignar los valores de los píxeles a la imagen
    image_pixels = np.array(image)
    image_pixels.flat = pixel_data

    # Guardar la imagen reconstruida
    image.save(output_path)


def separate_header_and_pixels(file_path):
    with open(file_path, 'rb') as file:
        byte_data = np.fromfile(file, dtype=np.uint8)

    print(byte_data)
    f = open(file_path, 'rb')
    file = f.read()
    f.close()

    # Buscar el marcador de inicio de cabecera (APP0)
    app0_marker = np.where(file == 0xFFE0)[0]

    # Obtener los bytes de cabecera
    header_bytes = byte_data[:app0_marker[0]]

    # Obtener los bytes de los datos de los píxeles
    pixel_bytes = byte_data[app0_marker[0]:]

    return header_bytes, pixel_bytes



def separate_header_and_pixels2(file_path):
    image = Image.open(file_path)
    bytes_imagen = image.tobytes()
    print(bytes_imagen)
    bytes_cabecera = bytes_imagen[:image._frameoffset]
    pixel_bytes = bytes_imagen[image._frameoffset:]
    return bytes_cabecera, pixel_bytes


#https://www.researchgate.net/figure/Some-Important-Markers-Found-in-JPEG-File-6_tbl1_308023205
#link arriba header formato jpeg
def separate_header_and_pixels3(file_path):
    # Leer los bytes del archivo JPEG
    with open(file_path, "rb") as f:
        bytes_imagen = np.fromfile(f, dtype=np.uint8)
        #bytes_imagen = f.read()
    print(bytes_imagen)
    # Buscar la posición del segmento de inicio de imagen (SOI)
    #soi_index = np.where((bytes_imagen == 255) & (np.roll(bytes_imagen, -1) == 216))[0][0]
    soi_index = np.where(np.logical_and(bytes_imagen[:-1] == 255, bytes_imagen[1:] == 216))[0][0]
    sof_index = np.where(np.logical_and(bytes_imagen[:-1] == 255, bytes_imagen[1:] == 192))[0][0]
    dqt_index = np.where(np.logical_and(bytes_imagen[:-1] == 255, bytes_imagen[1:] == 219))[0][0]
    print("Cantidad bytes:", len(bytes_imagen))
    print("soi index:", soi_index)
    print("sof index:", sof_index)
    print("dqt index:", dqt_index)

    # Obtener los bytes de la cabecera y pixeles
    bytes_imagen_inicio = bytes_imagen[sof_index:]
    altura = (bytes_imagen_inicio[5] << 8) + bytes_imagen_inicio[6]
    ancho = (bytes_imagen_inicio[7] << 8) + bytes_imagen_inicio[8]


    bytes_valores_pixeles = bytes_imagen_inicio[9:]
    #valores_pixeles = np.frombuffer(bytes_valores_pixeles, dtype=np.uint8)

    # Imprimir los bytes de la cabecera y pixeles
    #print(bytes_cabecera)
    #print()
    #print(bytes_pixeles)
    return altura, ancho, bytes_valores_pixeles

# Ejemplo de uso
file_path = "ave_chiquita2.jpg"
altura, ancho, bytes_valores_pixeles = separate_header_and_pixels3(file_path)
print("Altura:", altura)
print("Ancho:", ancho)
print('Valores pixeles plano:', bytes_valores_pixeles)



#reconstruct_image(header_bytes, pixel_bytes, 'prueba_imagen.jpg')







"""
# Ejemplo de uso
header_bytes = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $'
pixel_bytes = b'\xff\xc0\x00\x11\x08\x01\x0a\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\x0a\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\x0a\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\x15br\xd1\xf0$4\xe1%&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8'


En el ejemplo anterior, se utiliza el método `Image.open()` de PIL para crear una nueva imagen basada en los bytes de la cabecera. Luego, se convierten los bytes de los datos de los píxeles en un arreglo NumPy y se asignan los valores de los píxeles a la imagen utilizando `image_pixels.flat = pixel_data`. Finalmente, la imagen reconstruida se guarda en el archivo especificado por `output_path` utilizando el método `image.save()`.

Recuerda importar los módulos necesarios, como `Image` de PIL y `numpy`. Además, asegúrate de tener instalada la biblioteca PIL (por ejemplo, puedes instalarla utilizando `pip install Pillow`).

Ten en cuenta que este ejemplo asume que los datos de los píxeles están en un formato compatible con la imagen JPEG y que la cabecera contiene la información necesaria para interpretar los datos de los píxeles correctamente. Si los datos de los píxeles no están en un formato adecuado o la cabecera no es válida, es posible que la reconstrucción de la imagen no sea exitosa.

Espero que esto te sea útil. Si tienes más preguntas, no dudes en hacerlas.
"""
