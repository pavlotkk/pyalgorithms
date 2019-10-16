# Revert k items in queue
# Input:
# Queue: [1, 2, 3, 4, 5, 6]
# k = 4
#
# Output:
# [4, 3, 2, 1, 5, 6]
#

from typing import List


class Queue:
    def __init__(self, values: List[int] = None):
        self.values = values or []

    def enqueue(self, value: int):
        self.values.append(value)

    def dequeue(self) -> int:
        return self.values.pop(0)

    def is_empty(self) -> bool:
        return self.size() <= 0

    def size(self) -> int:
        return len(self.values)

    def __repr__(self):
        return str(self.values)


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


def revert(q: Queue, k: int) -> Queue:
    s = Stack()
    for i in range(k):
        if q.is_empty():
            break
        s.push(q.dequeue())

    # add reverted value back to the queue
    while not s.is_empty():
        q.enqueue(s.pop())
    print(q)

    # swap reverted values and remained
    for i in range(q.size() - k):
        q.enqueue(q.dequeue())

    return q


def solve():
    q = Queue([1, 2, 3, 4, 5, 6])
    q = revert(q, 4)
    print(q)


if __name__ == "__main__":
    solve()
