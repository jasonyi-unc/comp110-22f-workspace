from __future__ import annotations
from typing import Optional

class Node:
    data: int = -1
    next: Optional[Node] = None

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next

    
def find(head: Optional[Node], needle: int) -> bool:
    if head is None:
        raise ValueError("Cannot call find on an empty linked list")
    else:
        if head.data == needle:
            return True
        else:
            if head.next is None:
                return False
            else:
                return find(head.next, needle)


l: Node = Node(1, Node(2, Node(3, None)))
print(find(l, 4))