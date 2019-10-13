# Find a middle of a linked list
# Input:
# 1, 2, 3, 4, 5, 6, 7
#
# Output:
# 4
#
# Input:
# 1, 2, 3, 4
#
# Output:
# 2
#

from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next_node: Optional['Node'] = None

    def __repr__(self):
        return f'<Node {self.value}>'


class LinkedList:
    def __init__(self):
        self.root: Optional[Node] = None

    @classmethod
    def from_list(cls, l: list) -> 'LinkedList':
        ll = cls()

        if not l:
            return ll

        ll.root = Node(l[0])
        current = ll.root
        for i in range(1, len(l)):
            current.next_node = Node(l[i])
            current = current.next_node

        return ll

    def __repr__(self) -> str:
        l = []
        if not self.root:
            return str(l)

        current = self.root
        while current:
            l.append(current.value)
            current = current.next_node

        return str(l)


def solve(ll: LinkedList) -> Optional[int]:
    if not ll.root:
        return None

    middle = ll.root
    current = ll.root
    length = 0
    mid_index = 0

    while current:
        length += 1
        if length % 2 and (length // 2) > mid_index:
            middle = middle.next_node
            mid_index += 1
        current = current.next_node

    return middle.value


if __name__ == '__main__':
    print(solve(LinkedList.from_list([1])))
    print(solve(LinkedList.from_list([1, 2, 3])))
    print(solve(LinkedList.from_list([1, 2, 3, 4, 5, 6, 7])))
    print(solve(LinkedList.from_list([1, 2, 3, 4, 5, 6, 7, 8])))
    print(solve(LinkedList.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])))
    print(solve(LinkedList.from_list([i for i in range(101)])))
