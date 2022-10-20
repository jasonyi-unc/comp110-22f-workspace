"""EX07 - Dictionary Functions!"""

__author__ = "730604615"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Given a dict[str, int], return the same dict but the keys and values are switched."""
    y: dict[str, str] = {}
    for key in x:
        y[x[key]] = key
    return y


def favorite_color(x: dict[str, str]) -> str:
    """Given a dict of people's fav colors, return the color with the most frequency."""
    color_count: dict[str, int] = {}
    color: str = ""
    m: int = 0
    for key in x:
        if x[key] in color_count:
            color_count[x[key]] += 1
        else:
            color_count[x[key]] = 1
    for c in color_count:
        if color_count[c] > m:
            m = color_count[c]
            color = c
    return color


def count(x: list[str]) -> dict[str, int]:
    """Given a list of str, return a dict counting the frequency of each str."""
    total: dict[str, int] = {}
    for i in x:
        if i in total:
            total[i] += 1
        else:
            total[i] = 1
    return total
