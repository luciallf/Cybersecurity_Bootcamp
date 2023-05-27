# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 13:53:44 by lucilope          #+#    #+#              #
#    Updated: 2023/04/13 16:37:59 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if __name__ == "__main__":
    # Itera sobre las claves del diccionario kata
    for key in kata:
        # Imprime el nombre del lenguaje y su creador
        print("{} fue creado por {}".format(key, kata[key]))

        
