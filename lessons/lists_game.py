"""examples of using lists in a simple 'game'."""


from random import randint


rolls: list[int] = list()  # constructor call: creates empty list in memory (( list() ))

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))
print(rolls)

#  remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)  # no index = pops last item in list 
print(rolls)

#  sum value of rolls!
i: int = 0 
sum: int = 0 
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total score: {sum}")

#  different meanings of square bracket:
# 1.  data type - list[Type] (ex. list[str[])
# 2.  subscription operator - rolls[0] (or any int expression) *accesses items of a list
# 3.  list literal - [2, 4, 6] *itializes list 


# rolls.append(randint(1, 6))  #method call: adds an item to the end of a list
# rolls.append(randint(1, 6))
# print(rolls)

# #  access an individual item 
# print(rolls[0])
# print(rolls[1])  # using subscription notation to access items by 0-based indices

# #  access the length of a list (# of items)
# print(len(rolls))

# #  access the last item of a list 
# print(rolls[len(rolls) - 1])
# #  OR
# last_index: int = len(rolls) - 1
# print(rolls[last_index])