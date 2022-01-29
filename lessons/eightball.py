"""A magic eightball oracle of truth ab the future."""

from random import randint

input("Ask a yes or no wquestion: ")

response: int = randint(0, 3)

if response == 0:
    print("Yes, definitely!")
else:
    if response == 1:
        print("Looking hopeful.")
    else:
        if response == 2:
            print("Ask again later.")
        else: 
            print("No way. Not a chance.")