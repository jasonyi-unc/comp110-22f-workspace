"""EX05 - Utils Test."""

__author__ = "730604615"

from utils import only_evens, sub, concat


def test_evens_empty_list() -> None:
    """Test to see if only_evens() returns empty."""
    xs: list[int] = list()
    assert only_evens(xs) == []


def test_evens_neg_inp() -> None:
    """Test to see how only_evens() handles neg inp."""
    xs: list[int] = [-1, -2, -3, -4, -5, -6]
    assert only_evens(xs) == [-2, -4, -6]


def test_evens_odd_only() -> None:
    """Test to see how only_evens() handles only odd list inp."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_concat_empty_list() -> None:
    """Test to see if concat() returns empty."""
    xs1: list[int] = list()
    xs2: list[int] = list()
    assert concat(xs1, xs2) == []


def test_concat_pos_and_neg() -> None:
    """Test to see how concat() handles pos and neg inp."""
    xs1: list[int] = [1, 2, 3]
    xs2: list[int] = [-4, -5, -6]
    assert concat(xs1, xs2) == [1, 2, 3, -4, -5, -6]


def test_concat_empty_element() -> None:
    """Test to see how concat() handles space element."""
    xs1: list[int] = [1, 2, 3]
    xs2: list[int] = [4, 5, 6, ]
    assert concat(xs1, xs2) == [1, 2, 3, 4, 5, 6, ]


def test_sub_empty_list() -> None:
    """Test to see if sub() returns empty list."""
    xs: list[int] = list()
    assert sub(xs, 1, 10) == []


def test_sub_neg_start() -> None:
    """Test to see how sub() handles negative start inp."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, -1, 5) == [1, 2, 3, 4, 5]


def test_sub_over_end() -> None:
    """Test to see how sub() handles end inp > len(user_list)."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 5, 11) == [6, 7, 8, 9, 10]