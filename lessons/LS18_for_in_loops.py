"""LS18 - for-in loops"""

from uuid import NAMESPACE_URL


xs: list[str] = ["a", "b", "c"]

#while-loop ex
i: int = 0
while i < len(xs):
    print(xs[i])
    i += 1

#for-loop ex
for item in xs:
    print(item)

names: list[str] = ["Kris", "Kaki", "Ezri", "Marc"]

#Example of iterating through names using a while loop
print("while output")
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

#The following for...in loop is the same as the while loop
print("for...in output:")
for name in names:
    print(name)