"""An example of conditional 'if/else' statements"""


SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess != SECRET: 
    print("You guessed incorrectly")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")
else:
    print("You guessed correctly :))") 
    
    
print("Game Over.")