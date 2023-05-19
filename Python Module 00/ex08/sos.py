# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 15:41:18 by lucilope          #+#    #+#              #
#    Updated: 2023/04/17 15:41:18 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Haz un programa que tome un string como argumento y lo codifique en código Morse.
""" 
• El programa admite espacios y caracteres alfanuméricos
• Un carácter alfanumérico se representa mediante puntos . y guiones -:
• Un carácter de espacio se representa mediante una barra /
• Los caracteres morse completos se separan con un solo espacio

Si se proporciona más de un argumento, combínalos en un solo string con cada argu-
mento separado por un carácter de espacio.

Si no se proporciona ningún argumento, el programa no hará nada o imprimirá un
mensaje de utilización del comando.
 """

import string
import sys

morse_dictionary = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}

#esta funcion convierte cada letra del string en una mayuscula y a su equivalente del codigo Morse.
#agrega un espacio entre cada letra 
#si un caracter no est'a en el diccionario, agrega un error en su lugar
#Al final elimina el espacio adicional al final del codigo Morse


def traduction_morse(message):
    cifra = ''
    for letter in message:
        try:
            cifra += morse_dictionary[letter.upper()] + " "
        except: 
            print("ERROR")
            exit()
    return cifra     

#la funcion main, primero le decimos que si no se escribe ningun argumento que de error y se salga del programa
#en else, le decimos que el mensaje va a ser a partir de un argument en adelante y que se vaya uniendo todos los argv que tengamos 
#para meterlos en string_argument,mi caracter que lo busque en los argumentos unidos

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("ERROR! Use: python3 sos.py <arg>")
        exit()
    else:
        mess = ''
        message = sys.argv[1:]
        string_argument = (" ".join(message))
        mess = traduction_morse(string_argument)
        print(mess)