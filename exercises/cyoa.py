"""EX06 - Choose Your Own Adventure!"""

__author__ = "730604615"

from random import randint

points: int
player: str
GOODBYE_EMOJI: str


def main() -> None:
    """The main function."""
    global points, player, GOODBYE_EMOJI
    points = 0
    player = ""
    GOODBYE_EMOJI = "\U0001F493"
    choice: int = 0

    greet()
    while choice != 1:
        choice = int(input("Where would you like to go next? (1-END, 2-Guess a Number, 3-Flip a coin) "))
        if choice == 1:
            print(f"You have ended the session. Goodbye {GOODBYE_EMOJI}")
            print(f"Here are your total points: {points}")
        if choice == 2:
            num_guess()
        if choice == 3:
            points += coin_toss(points)
        print(f"Your total points: {points}")


def greet() -> None:
    """A procedure that greets the user."""
    global player
    print("Welcome to the Adventure!")
    player = input("What is your name? ")


def num_guess() -> None:
    """A function that asks the user to guess a number from 1-50."""
    global player, points
    guess: int = 0
    count: int = 1
    x: int = randint(1, 50)
    print(f"Hello {player}, I have choosen a number from 1-50. You have 5 tries, and whether the number is above or below will be provided")
    while count <= 5:
        guess = int(input(f"Attempt #{count} "))
        if guess == x:
            print("Correct! You are awarded 10 points!")
            points += 10
            count = 5
        elif guess < x:
            print("Try higher")
        else:
            print("Try lower")
        count += 1


def coin_toss(p: int) -> int:
    """User gets as many points as the streak they are able to get."""
    global player
    ans: int = randint(0, 1)
    guess: int = 0
    guess = int(input(f"I have a coin. {player}, guess if it's heads or tails! (0/1) "))
    while guess == ans:
        print("Correct! You get 1 point.")
        p += 1
        guess = int(input("What is it this time? "))
    print("You have guessed incorrectly. It was a good run though!")
    return p


if __name__ == "__main__":
    main()