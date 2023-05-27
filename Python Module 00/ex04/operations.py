# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:02:39 by lucilope          #+#    #+#              #
#    Updated: 2023/04/18 19:34:40 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys

def operations(num1, num2):
    """
    Esta función realiza operaciones aritméticas básicas entre dos números.
    """
    sum, dif, prod = num1 + num2, num1 - num2, num1 * num2
    print("Suma:", sum)
    print("Diferencia:", dif)
    print("Producto:", prod)

    if num2 == 0:
        # Comprueba si el segundo número es cero para evitar una división por cero
        print("Cociente: Error, división por cero")
        print("Resto: Error, módulo por cero")
        print("")
    else:
        quotient = num1 / num2
        remainder = num1 % num2
        print("Cociente:", quotient)
        print("Resto:", remainder)
        print("")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print()
    elif len(sys.argv) != 3:
        print("Error: por favor, proporciona 2 argumentos numéricos\n")
    else:
        try:
            operations(int(sys.argv[1]), int(sys.argv[2]))
        except:
            print("Error de Asertión: solo se admiten números enteros\n")
