#!/usr/bin/env python

import sys, string

def text_analyzer(*args):
    """
    Esta función cuenta el número de caracteres en mayúscula, caracteres en minúscula,
    signos de puntuación y espacios en un texto dado.
    """
    args = list(args)
    palabrita = 0
    if len(args) > 0:
        palabrita = args[0]
    while not palabrita:
        palabrita = input("Por favor, ingresa una cadena de texto: ")
    if type(palabrita) is not str:
        print("Error: la entrada no es una cadena de texto.")
        return

    upper_count = 0  # Contador de caracteres en mayúscula
    lower_count = 0  # Contador de caracteres en minúscula
    punct_count = 0  # Contador de caracteres de puntuación
    space_count = 0  # Contador de espacios
    total_count = 0  # Contador total de caracteres

    for char in palabrita:
        if char.isupper():
            upper_count += 1  # Incrementa el contador de caracteres en mayúscula
        elif char.islower():
            lower_count += 1  # Incrementa el contador de caracteres en minúscula
        elif char.isspace():
            space_count += 1  # Incrementa el contador de espacios
        elif char in string.punctuation:
            punct_count += 1  # Incrementa el contador de caracteres de puntuación
        total_count += 1  # Incrementa el contador total de caracteres

    # Imprimir los resultados
    print("El texto contiene:", total_count, "caracteres")
    print("Número de caracteres en mayúscula:", upper_count)
    print("Número de caracteres en minúscula:", lower_count)
    print("Número de caracteres de puntuación:", punct_count)
    print("Número de espacios:", space_count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Proporciona un argumento")
    else:
        text_analyzer(sys.argv[1])
