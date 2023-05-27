# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 13:53:47 by lucilope          #+#    #+#              #
#    Updated: 2023/04/18 20:03:07 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


kata = (2019, 9, 25, 3, 30)

# Imprime una cadena formateada con los elementos de la tupla kata
# Se utiliza "{:02d}" para imprimir los números con dos dígitos, rellenando con ceros si es necesario
# "{}" se utiliza para imprimir los elementos que no necesitan formato especial

print("{:02d}/{}/{} {:02d}:{}".format(kata[1], kata[2], kata[0], kata[3], kata[4]))
