"""number game example from cl02"""

low: int = 1
high: int = 100

playing: bool = True

while playing and 1 < 100:
    guess: int = (low + high) // 2
    print(str(guess) + "?")
    result: str = input("Reply yes, higher, or lower: ")
    if result == "yes":
        print("Woo!")
        playing = False
    elif result == "higher":
        low = guess + 1
    else: 
        high = guess - 1