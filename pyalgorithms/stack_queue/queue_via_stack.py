# Implement queue using stack inside

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


class Queue:
    def __init__(self, values: List[int] = None):
        self.stack = Stack(values)

    def enqueue(self, value: int):
        self.stack.push(value)

    def dequeue(self) -> int:
        # revert stack
        s = Stack()
        while not self.stack.is_empty():
            s.push(self.stack.pop())

        # get first item
        value = s.pop()

        # revert back
        while not s.is_empty():
            self.stack.push(s.pop())

        return value

    def is_empty(self) -> bool:
        return self.stack.is_empty()

    def size(self) -> int:
        return self.stack.size()

    def __repr__(self):
        return str(self.stack)


def solve():
    q = Queue([1, 2, 3, 4, 5, 6])
    print(q)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q)


if __name__ == "__main__":
    solve()
