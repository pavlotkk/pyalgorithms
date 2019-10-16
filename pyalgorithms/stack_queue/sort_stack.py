# Sort stack using only public methods push/pop
# P.S. Sorting array is not fun ;)
# Input:
# [19, 20, 1, 4, 12, 5]
#
# Output:
# [1, 2, 4, 12, 19, 20]

from typing import List


class Stack:
    def __init__(self, values: List[int] = None):
        self.values = values or []

    def push(self, value: int):
        self.values.append(value)

    def pop(self) -> int:
        return self.values.pop(self.size() - 1)

    def is_empty(self) -> bool:
        return self.size() <= 0

    def size(self) -> int:
        return len(self.values)

    def __repr__(self):
        return str(self.values)


def sort_stack(s: Stack) -> Stack:
    ordered_stack = Stack()
    while not s.is_empty():
        value = s.pop()

        if ordered_stack.is_empty():
            ordered_stack.push(value)
            continue

        last_ordered_value = ordered_stack.pop()
        if value >= last_ordered_value:
            ordered_stack.push(last_ordered_value)
            ordered_stack.push(value)
        else:
            s.push(last_ordered_value)
            s.push(value)

    return ordered_stack


def solve():
    s = Stack([19, 20, 1, 4, 12, 5])
    s = sort_stack(s)
    print(s)

    s = Stack([1, 2, 3, 4, 5])
    s = sort_stack(s)
    print(s)

    s = Stack([5, 4, 3, 2, 1])
    s = sort_stack(s)
    print(s)


if __name__ == "__main__":
    solve()
