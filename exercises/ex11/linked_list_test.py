"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730604615"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3

    
def test_value_at_out_of_bounds() -> None:
    """An invalid index value should raise an IndexError."""
    linked_list = Node(10, Node(20, Node(30, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 3)


def test_value_at_index() -> None:
    """The index value should return the position of the corresponding linked list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def test_max() -> None:
    """The function should return the data with the highest value."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30


def test_max_empty() -> None:
    """An empty linked list should return a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify() -> None:
    """Should return a Linked List of Nodes with the same values, in the same order, as the input list."""
    l: list[int] = [1, 2, 3]
    assert print(linkify(l)) == print(Node(1, Node(2, Node(3, None))))


def test_linkify_empty() -> None:
    """Should return None if given an empty list."""
    assert linkify([]) is None

    
def test_scale() -> None:
    """Should return a Node with the factor applied."""
    list1 = scale(linkify([1, 2, 3]), 2)
    assert print(list1) == print(Node(2, Node(4, Node(6, None))))


def test_scale_empty() -> None:
    """Should return None on empty Node."""
    assert scale(None, 3) is None