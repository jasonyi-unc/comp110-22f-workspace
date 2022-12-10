"""Stair climbing."""

def stairs(start: int, end: int) -> str:
    s: str = str(start) + " "
    if start >= end:
        s += "TURN "
    else:
        s += stairs(start + 1, end)
    s += str(start) + " "
    return s

print(stairs(1,3))