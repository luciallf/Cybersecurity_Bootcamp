# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 13:53:51 by lucilope          #+#    #+#              #
#    Updated: 2023/04/14 15:51:46 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



kata = (0, 4, 123.42222, 10000, 1235.67)

# Imprime una cadena formateada con los elementos de la tupla kata
# Utiliza "{:02d}" para imprimir los números enteros con dos dígitos, rellenando con ceros si es necesario
# Utiliza "{:.02f}" para imprimir el número de punto flotante con dos decimales
# Utiliza "{:.02e}" para imprimir el número en notación científica con dos decimales

print("module_{:02d}, ex_{:02d} : {:.02f}, {:.02e}, {:.02e}".format(kata[0], kata[1], kata[2], kata[3], kata[4]))


