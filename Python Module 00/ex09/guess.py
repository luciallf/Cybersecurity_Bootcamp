# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 10:54:19 by lucilope          #+#    #+#              #
#    Updated: 2023/04/19 15:21:58 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Tienes que hacer un programa que sea un juego de adivinanzas interactivo. Pedirá
al usuario que adivine un número entre 1 y 99. El programa indicará al usuario si su
entrada es demasiado alta o demasiado baja. El juego termina cuando el usuario averigua
el número secreto o teclea exit. Importarás el módulo random con la función randint
para obtener un número aleatorio. Tienes que contar el número de intentos e imprimir
ese número cuando el usuario gane. """

import random, sys

#Tengo que usar la función randint para obtener un número aleatorio
#Me tiene que contar el número de intentos e imprimir ese nñumero cuando el usuario gane
#Si el usuario descubre el número secreto en el primer intento, decirselo 

#tengo que hacer primero en el main al inciar el programa, que me cree un numero aleatorio y lo guarde en una variable
#con esa variable ya empiezo a usar la función, donde haré un while con unas condiciones si no se acierta con el número
#generar un conrtador que me genere el numero de intentos y cuando gane el usuario imprimir el n de intentos

def game():
    a = None
    i = 0
    while a != x:
        a = input("What's your guess between 1 and 99?")
        if (a == "exit"):
            print("Goodbye!")
            exit()
        elif (not a.isdigit() or int(a) <1 or int(a) > 99):
            print("Not the right usage! Enter a number between 1 and 99")
            i += 1
            continue
        i+= 1
        a = int(a)
        if a < x : 
            print("Too low!")
        elif a > x:
            print("Too high!")
        else:
            if (a == x):
                print("Congratulations, you've got it!")
                print("You won in {i} attempts!".format(i = i))
            if (i == 1):
                print("Congratulations! You achieve it in your first try!")
            elif (a == 42):
                print("The answer to the ultimate question of life, the universe and everything is 42!")
    
           
        
        
        

if __name__ == "__main__":
    x = random.randint(1,99)
    print("This is an interactive guessing game!\n You have to enter a number between 1 and 999 to find out the secret number.\n Type 'exit' to end the game.\n Good luck!")
    game()
    
        
    
    