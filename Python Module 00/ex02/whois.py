# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:30:53 by lucilope          #+#    #+#              #
#    Updated: 2023/04/12 19:22:23 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



import sys

if len(sys.argv) == 2:
    # Comprueba si se proporcionó exactamente un argumento en línea de comandos
    try:
        # Intenta convertir el argumento a un número entero
        num = int(sys.argv[1])
        if num == 0:
            # Si el número es 0, imprime "I'm Zero."
            print("I'm Zero.")
        elif num % 2 == 0:
            # Si el número es par, imprime "I'm Even."
            print("I'm Even.")
        else:
            # Si el número es impar, imprime "I'm Odd."
            print("I'm Odd.")
    except ValueError:
        # Si el argumento no se puede convertir a entero, imprime un mensaje de error
        print("Error: Argument is not an integer.")
else:
    # Si no se proporciona exactamente un argumento, imprime un mensaje de error
    print("Error: Provide one integer argument.")
