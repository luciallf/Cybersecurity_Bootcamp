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
    try:
        num = int(sys.argv[1])
        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("Error: Argument is not an integer.")
else:
    print("Error: Provide one integer argument.")
