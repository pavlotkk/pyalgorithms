# Implement two stacks based on one array
from typing import Tuple


class Stack:
    def __init__(self, size: int):
        self.size = size
        self.array = [None] * size
        self.top = (-1, size)  # type: Tuple[int, int]

    def push(self, stack_num: int, value: int):
        top1, top2 = self.top
        if stack_num == 1:
            if (top1 + 1) >= top2:
                raise IndexError("Stack is overflow")
            top1 += 1
            self.array[top1] = value
        elif stack_num == 2:
            if (top2 - 1) <= top1:
                raise IndexError("Stack is overflow")
            top2 -= 1
            self.array[top2] = value

        self.top = (top1, top2)

    def pop(self, stack_num: int) -> int:
        top1, top2 = self.top
        value = None

        if stack_num == 1:
            if top1 <= -1:
                raise IndexError(f"Stack {stack_num} is empty")
            value = self.array[top1]
            self.array[top1] = None
            top1 -= 1
        elif stack_num == 2:
            if top2 >= self.size:
                raise IndexError(f"Stack {stack_num} is empty")
            value = self.array[top2]
            self.array[top2] = None
            top2 += 1

        self.top = (top1, top2)
        return value

    def __repr__(self):
        return str(self.array)


def solve():
    stack = Stack(5)
    print(stack)

    stack.push(1, 1)
    print(stack)

    stack.push(1, 2)
    print(stack)

    stack.push(1, 3)
    print(stack)

    stack.push(2, 5)
    print(stack)

    stack.push(2, 4)
    print(stack)

    try:
        stack.push(2, 3)
    except IndexError:
        pass

    print(stack.pop(1))
    print(stack)

    print(stack.pop(1))
    print(stack)

    print(stack.pop(1))
    print(stack)

    try:
        print(stack.pop(1))
        print(stack)
    except IndexError:
        pass

    print(stack.pop(2))
    print(stack)

    print(stack.pop(2))
    print(stack)


if __name__ == "__main__":
    solve()
