"""Example implementing a list utility function."""

#Function name: contains
#We will have 2 parameters: needle (str), haystac
#Gameplan:
#1. Start with the first index
#2. Loop through every index
#   2.A Test if item at index equal to needle
#       2.A Return True! We found it!
#3. Return False

def contains(needle: str, haystack: list[str]) -> bool:
    """Returns True if needle is found in the haystack at least once, False otherwise"""
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i += 1
    return False

print(contains("poop", ["poop", "piss", "shit"]))