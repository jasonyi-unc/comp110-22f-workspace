"""Demonstrate defining a module imported elsewhere."""

THE_ANSWER: int = 42

def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


print("helpers.py was evaluated")


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")



#idiom for making a module able to run as a program
#or have its global definitions imported elsewhere
if __name__ == "__main__":
    main()
else:
    #It is not typical to have an else branch here
    print(f"helpers.py was imported. {__name__}")