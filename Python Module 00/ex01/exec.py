#!/usr/bin/env python

import sys 

def reverse_words(string):
    reversed_string = string[::-1]
    swapped_case_string = reversed_string.swapcase()
    return swapped_case_string

if len(sys.argv) > 1:
    string = ' '.join(sys.argv[1:])
    result = reverse_words(string)
    print(result)
else:
    print("usage: ./exec.py num num")
