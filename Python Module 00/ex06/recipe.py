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

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

# Esta función imprime todos los nombres de las recetas
def recipe_name():
    for name in cookbook:
        print(name)

# Esta función toma el nombre de la receta e imprime sus detalles
def recipe_details(name):
    if name in cookbook:
        print("Recipe for", name, ":")
        print("Ingredients list:", cookbook[name]["ingredients"])
        print("To be eaten for", cookbook[name]["meal"], ".")
        print("Takes", cookbook[name]["prep_time"], "minutes of cooking.")
    else:
        print("The recipe is not in the cookbook")

# Esta función borra el nombre de la receta si está en el diccionario
def clean_name(name):
    if name in cookbook:
        del cookbook[name]
    else:
        print("The recipe does not exist.")

# Esta función te permite crear una nueva receta con los nombres e ingredientes que ingreses en una lista
# y las añade al diccionario "cookbook"
def add_recipe():
    print("Enter name:")
    name = input()
    if name in cookbook:
        print("The recipe already exists")
        return False
    ingredients = []
    print("Enter ingredients:")
    value = input()
    while value != "":
        ingredients.append(value)
        value = input()
    print("Enter a meal type:")
    meal_type = input()
    print("Enter a preparation time:")
    prep_time = input()
    cookbook.update({name: {"ingredients": ingredients, "meal": meal_type, "prep_time": prep_time}})
    return True

def introduction():
    print("List of available options:")
    print("    1: Add a recipe\n    2: Delete a recipe\n    3: Print a recipe\n    4: Print the cookbook\n    5: Quit")
    while True:
        var = input("Please select an option:")
        if var == "1":
            add_recipe()
        elif var == "2":
            name = input("Which recipe do you want to delete?")
            clean_name(name)
        elif var == "3":
            name = input("Please enter a recipe name to get its details:")
            recipe_details(name)
        elif var == "4":
            recipe_name()
        elif var == "5":
            break
        else:
            print("Sorry, this option does not exist.")

    print("Cookbook closed. Goodbye!\n")

if __name__ == "__main__":
    print("Welcome to the Python Cookbook!")
    introduction()












        

