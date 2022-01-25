"""EX01 - Chardle - A cute step toward Worlde."""

__author__ = "730440093"

five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")

if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + five_character_word)

if single_character in five_character_word:
    if single_character == str(five_character_word)[0]:
        print(str(five_character_word)[0] + " found at index 0 ")
    if single_character == str(five_character_word)[1]:
        print(str(five_character_word)[1] + " found at index 1")
    if single_character == str(five_character_word)[2]:
        print(str(five_character_word)[2] + " found at index 2")
    if single_character == str(five_character_word)[3]:
        print(str(five_character_word)[3] + " found at index 3")
    if single_character == str(five_character_word)[4]:
        print(str(five_character_word)[4] + " found at index 4")

list1: str = (five_character_word)

character_instance: int = list1.count(single_character) 

if character_instance == 1:
    print((str(character_instance) + " instance of " + single_character + " found in " + five_character_word))
if character_instance >= 2:
    print((str(character_instance) + " instances of " + single_character + " found in " + five_character_word))
if character_instance == 0: 
    print("No instances of " + single_character + " found in " + five_character_word)
