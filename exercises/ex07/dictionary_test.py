"""EX07 - Dictionary Tests."""

__author__ = "730604615"

from dictionary import invert, favorite_color, count
from pytest import raises


def test_invert_empty_dict() -> None:
    """Test to see if dictionary is empty."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_same_keys() -> None:
    """Test to raise error if identical keys."""
    with raises(KeyError):
        xs: dict[str, str] = {"Kris": "Jordan", "Michael": "Jordan"}
        invert(xs)


def test_invert() -> None:
    """Test functionality of invert."""
    cs_rankings: dict[str, str] = {"UNC": "28", "Duke": "23", "MIT": "1"}
    assert invert(cs_rankings) == {"28": "UNC", "23": "Duke", "1": "MIT"}


def test_color_empty_dict() -> None:
    """Test to see if dictionary is empty."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_color_tie() -> None:
    """Test if 2 colors with same vote, the first one that appears is chosen."""
    xs: dict[str, str] = {"Kris": "Blue", "Bob": "Blue", "Hyon": "Black", "Marc": "Black"}
    assert favorite_color(xs) == "Blue"


def test_color() -> None:
    """Test functionality of favorite_color."""
    xs: dict[str, str] = {"Kris": "Blue", "Hyon": "Black", "Ryan": "Blue"}
    assert favorite_color(xs) == "Blue"


def test_count_empty_list() -> None:
    """Test if empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_same_freq() -> None:
    """Test if there are occurrances of the same amount."""
    xs: list[str] = ["One", "One", "Two", "Two"]
    assert count(xs) == {"One": 2, "Two": 2}


def test_count_diff_freq() -> None:
    """Test if there are occurrances of different amounts."""
    xs: list[str] = ["One", "One", "Two", "Three"]
    assert count(xs) == {"One": 2, "Two": 2, "Three": 3}