"""Examples of importing Python."""

#lessons - package, helpers - module
from lessons import helpers

#Alias a module / imported name as other name
from lessons import helpers as hp

#import names and defined globally in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2,4))
    print(f"The answer: {helpers.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)
#
if __name__ == "__main__":
    main()