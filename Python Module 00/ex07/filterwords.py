# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 15:41:25 by lucilope          #+#    #+#              #
#    Updated: 2023/04/17 15:41:25 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


#Haz un programa que tome como argumento un string S y un número entero N e
#imprima la lista de palabras de S que contenga más de N caracteres que no sean de
#puntuación.
#• Las palabras están separadas entre sí por espacios
#• Los signos de puntuación deben eliminarse de la lista impresa: no forman parte de
#una palabra ni son separadores
#• El programa debe contener al menos una expresión de comprensión de lista.
#Si el número de argumentos es distinto de 2, o si el tipo de algún argumento es
#incorrecto, el programa imprime un mensaje de error.


#. sys es un módulo estándar de Python que proporciona acceso a algunas variables y funciones utilizadas o mantenidas por el intérprete de Python.

import sys 
import string

#Primero, verificamos que el número de argumentos sea 2 mediante la función len(). Si no es así, imprimimos un mensaje de error y salimos del programa con sys.exit()

if len(sys.argv) != 3:
    print("Error: el programa requiere dos argumentos")
    sys.exit()

#Luego, intentamos convertir el segundo argumento a un número entero utilizando int(). Si esto falla, imprimimos un mensaje de error y salimos del programa.
#En este caso, la parte try contiene el código que se espera que genere una excepción, y la parte except contiene el código que se ejecuta si se produce una 
# excepción de tipo ExceptionType. En este caso, la parte try contiene el código que se espera que genere una excepción, y la parte except contiene el código que se 
# ejecuta si se produce una excepción de tipo ExceptionType

try:
    num = int(sys.argv[2])
except ValueError:
    print("Error: el segundo argumento debe ser un número entero")
    sys.exit()

#Comprobamos que el número sea mayor o igual a 0 para asegurarnos de que sea un número entero positivo

if num < 0:
    print("Error: el segundo argumento debe ser un número entero positivo")
    sys.exit()



s = sys.argv[1]
s = s.translate(str.maketrans('', '', string.punctuation))
#Usamos una comprensión de lista para crear una lista de palabras sin signos de puntuación. La cadena de texto se divide en palabras utilizando el método split() y 
#luego se aplica el método translate() para eliminar los signos de puntuación. Esto se logra mediante el uso del método str.maketrans() y el módulo string.

words = [x for x in s.split() if len(x) > num]

#Finalmente, usamos otra comprensión de lista para crear una lista de palabras que tienen más de num caracteres y las imprimimos.

# long_words =[words for words in s in len(words) > num]
print(words)