from __future__ import annotations
from typing import Optional

class Node:
    data: int = -1
    next: Optional[Node] = None

def build(start: int, end: int) -> Optional[Node]:
    """Build a linked list from start to end -1."""
    if start >= end:
        return None
    else:
        n: Node = Node()
        n.data = start
        n.next = build(start + 1, end)
        return n

head: Optional[Node] = build(0, 2)
print(head)