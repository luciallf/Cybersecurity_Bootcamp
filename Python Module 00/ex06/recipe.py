# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucilope <lucilope@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 11:26:02 by lucilope          #+#    #+#              #
#    Updated: 2023/04/19 10:31:14 by lucilope         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook =  {
        "Sandwich":{
        "ingredients":["ham", "bread", "cheese", "tomatoes"], 
        "meal": "lunch",
        "prep_time": 10
        }, 
        "Cake":{
        "ingredients":["flour", "sugar", "eggs"],
        "meal":"dessert",
        "prep_time": 60
        },
        "Salad":{
        "ingredients":["avocado", "arugula", "tomatoes", "spinach"],
        "meal":"lunch",
        "prep_time": 15
        }
        }

#esta funcion imprime todos los nombres de las recetas
def recipe_name():
        for name in cookbook:
                 print(name)  


#este seria la funcion 2: toma el nombre de la receta e imprime sus detalles
def recipe_details(name):
        if name in cookbook:
                print("Recipe for", name, ":")
                print("Ingredients list:", cookbook[name]["ingredients"])
                print("To be eaten for", cookbook[name]["meal"],".")
                print("Takes", cookbook[name]["prep_time"], "minutes of cooking.")
        else:
                print(" The recipe is not in the cookbook")

#funcion que borra el nombre de la receta si está en mi diccionario
def clean_name(name):
        if name in cookbook:
                 del (cookbook[name])
        else:
                print("The recipe does not exits.")
        return


# .update() se utiliza para agregar o actualizar elementos en un diccionario, 
# mientras que la función .append() se utiliza para agregar elementos a una lista.

#funcion que te crea una nueva receta con los nombres e ingredientes que le pongas en una lista y las añade en el diccionario

def add_receta():
        print("Enter name:")
        name = input()
        if name in cookbook:
                print("The recipe already exists")
                return False
        Ingredients = []
        print("Enter ingredients:")
        valor = input()
        while valor != "":
                Ingredients.append(valor)
                valor = input()
        print("Enter a meal type:")
        Meal_type = input()
        print("Enter a preparation time:")
        time = input()
        cookbook.update({name:{"ingredients": Ingredients,"meal":Meal_type, "prep_time": time}})
        return True

def introduction():
        print("List of available option:")
        print("    1: Add a recipe\n    2: Delete a recipe\n    3: Print a recipe\n    4: Print the cookbook \n    5: Quit")
        while 42:
                var = input("Please select an option:")
                if var == "1":
                        add_receta()
                elif var == "2":
                        name = input("What recipe do you want to delete?")
                        clean_name(name)
                elif var == "3":
                        name = (input("Please enter a recipe name to get its details:"))
                        recipe_details(name)
                elif var == "4":
                        recipe_name()
                elif var == "5":
                        break
                else:
                        print("Sorry, this option does not exist.")
                        introduction()
                        exit()
        print("Cookbook closed. Goodbye!\n")
        


if __name__ == "__main__":
        print("Welcome to the python Cookbook !")
        introduction() 
        #aquí, quiero que empiece de nuevo si pone un numero al principio que no






















        

