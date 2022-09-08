"""EX02 - One Shot Worldle: Loops!"""

__author__ = "730604615"


secret_word: str = "python"
input_guess: str = input("What is your 6-letter guess? ")
counter: int = 0
box_emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
yellow_guess: bool = False
alt_counter = 0


while len(input_guess) != 6:
    input_guess = input("This was not 6 letters ! Try again: ")


while counter < len(secret_word):
    if input_guess[counter] == secret_word[counter]:
        box_emoji += GREEN_BOX
    else:
        while not yellow_guess and alt_counter < len(secret_word):
            if input_guess[counter] == secret_word[alt_counter]:
                yellow_guess = True
            else:
                alt_counter += 1
        if yellow_guess:
            box_emoji += YELLOW_BOX
        else:
            box_emoji += WHITE_BOX
    counter += 1
    alt_counter = 0
    yellow_guess = False
print(box_emoji)
  
if input_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")