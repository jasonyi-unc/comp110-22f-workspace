"""EX03 - Structured Wordle!"""

__author__ = "730604615"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> bool:
    """Given a word and a single character, return True if character is found in word."""
    assert len(letter) == 1
    flag: bool = False
    i = 0
    while not flag and i < len(word):
        if letter == word[i]:
            flag = True
            return flag
        i += 1
    return flag


def emojified(input_guess: str, secret_word: str) -> str:
    """Given the user's guess and the secret word, return a str of emoji boxes reflecting its match."""
    assert len(input_guess) == len(secret_word)
    counter: int = 0
    box_emoji: str = ""

    while counter < len(secret_word):
        if input_guess[counter] == secret_word[counter]:
            box_emoji += GREEN_BOX
        elif contains_char(secret_word, input_guess[counter]):
            box_emoji += YELLOW_BOX
        else:
            box_emoji += WHITE_BOX
        counter += 1
    return box_emoji


def input_guess(length: int) -> str:
    """Returns the user input based on the desired length."""
    user_input: str = input(f"Enter a {length} character word: ")
    while len(user_input) != length:
        user_input = input(f"That wasn't {length} chars! Try again: ")
    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    codes: str = "codes"
    n: int = 1
    while n <= 6:
        print(f"=== Turn {n}/6 ===")
        guess = input_guess(len(codes))
        print(emojified(guess, codes))
        if guess == codes: 
            print(f"You won in {n}/6 turns!")
            return
        else:
            n += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()