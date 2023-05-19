# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/01 16:09:28 by lucilope          #+#    #+#              #
#    Updated: 2023/05/01 16:09:28 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
El segundo programa scorpion recibirá archivos de imagen como parámetros y será
capaz de analizarlos en busca datos EXIF y otros metadatos, mostrándolos en pantalla.
El programa será compatible, al menos, con las mismas extensiones que gestiona spider.
Deberá mostrar atributos básicos como la fecha de creación, así como otros datos EXIF.
El formato en el que se muestren los metadatos queda a tu elección.
"""


"""
PIL (Python Imaging Library) es una biblioteca de procesamiento de imágenes de Python que se utiliza para abrir,
 manipular y guardar imágenes en diferentes formatos. PIL.ExifTags es un módulo en la biblioteca PIL que se 
 utiliza específicamente para leer y procesar metadatos Exif de imágenes.
"""
import sys
import argparse
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS


def arguments():

    analizador = argparse.ArgumentParser(
    description = "Herramienta de scraping de imagenes en un sitio web"
    )    
    
    analizador.add_argument("IMAGEN", help="Imagen a analizar", type = str) 
    analizador.add_argument("IMAGENES", help= "Imágenes a anlizar ", nargs = "*") 
    return analizador.parse_args()


def meta_data(imagen):
    print("Nombre".ljust(29), ":", imagen.filename.split('/'))
    print("Dimesiones".ljust(29), ":", imagen.size[0], imagen.size[1])
    print("Formato".ljust(29), ":" , imagen.format )
    print("Modo".ljust(29), ":", imagen.mode)
    print("Paleta".ljust(29), ":", imagen.palette)


def scorpion(rutas):
    for ruta in rutas:
        try:
            imagen = Image.open(ruta)
        except:
            print("no se ha podido abrir", ruta)
        else: 
            datos = imagen.getexif()
            print(ruta.split('/')[-1])
            meta_data(imagen)
            if not datos:
                print("Exif:", datos)
            for key, val in datos.items():
                if key in ExifTags.TAGS:
                    print(f'{ExifTags.TAGS[key]:30}: {val}')
       
            


if __name__ == "__main__": 
   
    args = arguments()

    comandos = list()
    comandos.append(args.IMAGEN)
    comandos += args.IMAGENES

    scorpion(comandos)



