# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 13:53:49 by lucilope          #+#    #+#              #
#    Updated: 2023/04/18 20:02:51 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = "The right format"

# Imprime una cadena formateada con el contenido de la variable kata
# Utiliza "{:->42}" para justificar el texto a la derecha y rellenar con guiones (-) hasta alcanzar una longitud de 42 caracteres
# El parámetro end="" se utiliza para evitar el salto de línea al final de la impresión

print("{:->42}".format(kata), end="")
