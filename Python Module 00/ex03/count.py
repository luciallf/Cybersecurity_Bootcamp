#!/usr/bin/env python

import sys, string

def text_analyzer(*args):
    """
   This function counts the number of upper characters, lower characters,\n   punctuation and spaces in a given text. 
    """
    args = list(args)
    palabrita = 0
    if len(args) > 0:
       palabrita= args [0]
    while not (palabrita):
        palabrita= input("Please enter a string: ")
    if type(palabrita) is not str:
        print("Error: the input is not a string.")
        return

    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    total_count = 0
    for char in palabrita:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char in string.punctuation:
            punct_count += 1
        total_count += 1

    print("The text contains:", total_count)
    print("Number of uppercase characters:", upper_count)
    print("Number of lowercase characters:", lower_count)
    print("Number of punctuation characters:", punct_count)
    print("Number of spaces:", space_count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error")
    else:
        text_analyzer(sys.argv[1])
