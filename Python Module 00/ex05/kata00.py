# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 17:51:11 by lucilope          #+#    #+#              #
#    Updated: 2023/04/13 14:01:11 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (9, 42, 21)

if __name__ == "__main__":
    # Imprime la cantidad de números en la tupla kata
    print("Los", len(kata), "números son:", ', '.join(str(x) for x in kata))
