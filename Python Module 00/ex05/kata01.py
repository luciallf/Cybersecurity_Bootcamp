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
        'Python' : 'Guido van Rossum', 
        'Ruby' : 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
if __name__ == "__main__":
    for key in kata:
        print("{} was created by {}".format(key, kata[key]))
        
