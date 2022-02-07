"""EX03 Structured Wordle."""

__author__ = "730440093"


def contains_char(search_word: str, sing_char: str) -> bool:
    """Return whether character exists within given word."""
    i: int = 0 
    assert len(sing_char) == 1
    while i < len(search_word):
        if sing_char == search_word[i]:      
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Function to classify and assign emoji values."""
    assert len(guess) == len(secret)
    length: int = len(secret)
    i: int = 0
    box_line: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i < length:
        if contains_char(secret, guess[i]) is True and guess[i] == secret[i]:
            box_line += GREEN_BOX
        elif contains_char(secret, guess[i]) is True and guess[i] != secret[i]:
            box_line += YELLOW_BOX
        elif contains_char(secret, guess[i]) is False:
            box_line += WHITE_BOX
        i += 1
    return box_line


def input_guess(expctd_len: int) -> str:
    """Function to ensure that user's input is correct length."""
    input_guess: str = input(f"Enter a {expctd_len} character word: ")
    while len(input_guess) != expctd_len: 
        input_guess = input(f"That wasn't {expctd_len} chars! Try again: ")
    return input_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    answer: str = "codes"
    length: int = len(answer)
    i: int = 0
    turn: int = 1
    playing: bool = True
    while turn <= 6 and playing is True:
        print(f"=== Turn {turn}/6 ===")
        user_guess: str = input_guess(length)
        print(emojified(user_guess, answer))
        if user_guess == answer:
            print(f"You won in {turn}/6 turns!")
            playing = False
        turn += 1
        i += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__": 
    main()