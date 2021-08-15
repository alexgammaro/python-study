import itertools

import wordlist

string = input("String a ser permutada: ")

# resultado = itertools.permutations("abcdef", 5)
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print("".join(i))