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
    sum, dif, prod=num1+num2, num1-num2, num1*num2 
    print("Sum:", sum)
    print("Difference:", dif)
    print("Product:", prod)
    if num2==0:
        print("Quotient: Error, division by zero")
        print ("Remainder: Error modulo by zero")  
        print("")
    else:
        quotient = num1/num2
        Remainder =num1%num2 
        print("Quotient:", quotient)
        print("Remainder", Remainder)  
        print("")


if __name__ == "__main__":
    if len(sys.argv)<=1:
        print()
    elif len(sys.argv)!=3:
        print("Error: please write 2 numbers arguments \n")
    else:
        try:
            operations(int(sys.argv[1]), int(sys.argv[2]))
        except:
            print("AsertionError: only integers \n")
  