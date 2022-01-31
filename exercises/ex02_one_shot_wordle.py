"""One Shot Worlde COMP110 Assignment."""

__author__ = "730440093"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

answer: str = "python"
# defining answer

length: int = len(answer) 
# defining length variable in order to later determine if guess was acceptable length and in order to establish maximum for while loop

guess: str = input(f"What is your {str(length)}-letter guess? ")
# defining guess + use of f-string

i: int = 0

box_line: str = ""

while len(guess) != length:  # while loop that ends as soon as len(guess) == length since this is the only criteria needed to begin the "game" itself; movement towards closing loop is the new guess
    guess = input(f"That was not {str(length)} letters! Try again: ")
    # redefinition of guess so as to not require a new variable for any guesses following the initial input + use of f-string
if guess == answer:
    while i < length:
        box_line += GREEN_BOX
        i += 1  # changing index variable necessary to close while loop
    # as long as the guess == answer, there was no need to code anything other than a box_line of green boxes
    print(box_line)
    print("Woo! You got it!")
else:
    while i < length:  # while loop used in order to evaluate each individual character in answer string
        if answer[i] == guess[i]:
            box_line += GREEN_BOX
            # as long as the same character exists in the same index as the answer and the guess, only a green box is necessary
        elif answer[i] != guess[i] and guess[i] in answer:
            box_line += YELLOW_BOX
            # when the indices do not match however, it is important to specify that a yellow box should only be denoted iff the character at a given index of the guess string exists within the answer string elsewhere
        elif answer[i] != guess[i]:
            box_line += WHITE_BOX
            # if the character evaulated at a certain index does not exist within the answer then only a white box is necessary to denote this
        i += 1  # changing index variable necessary to close while loop
    print(box_line)
    print("Not quite. Play again soon!")
