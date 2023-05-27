import sys

def reverse_words(string):
    # Invertir la cadena
    reversed_string = string[::-1]
    # Cambiar el caso de las letras en la cadena invertida
    swapped_case_string = reversed_string.swapcase()
    return swapped_case_string

if len(sys.argv) > 1:
    # Obtener la cadena de texto de los argumentos de línea de comandos
    string = ' '.join(sys.argv[1:])
    # Llamar a la función reverse_words() con la cadena de texto
    result = reverse_words(string)
    # Imprimir el resultado
    print(result)
else:
    # Imprimir mensaje de uso en caso de que no se proporcionen argumentos
    print("usage: ./exec.py num num")

