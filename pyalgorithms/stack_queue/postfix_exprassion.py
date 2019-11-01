# Implement postfix expression
# Input:
# 921*-8-4+
#
# 4 = a
# -8 + a = b
# -2 + b = c
# 9 + c = 3
#
# Output:
# 3

import operator

from typing import List


class Stack:
    def __init__(self, values: List[str] = None):
        self.values = values or []

    def push(self, value: str):
        self.values.append(value)

    def pop(self) -> str:
        return self.values.pop(self.size() - 1)

    def is_empty(self) -> bool:
        return self.size() <= 0

    def size(self) -> int:
        return len(self.values)

    def __repr__(self):
        return str(self.values)


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul
}


def solve(expression: str) -> int:
    exp = Stack([e for e in expression])
    operators = Stack()

    left_operand = None
    while not exp.is_empty():
        operand = exp.pop()
        if operand in OPERATORS:
            operators.push(operand)
            continue

        int_operand = int(operand)
        if left_operand is None:
            left_operand = int_operand
            continue

        right_operand = int_operand
        left_operand = OPERATORS[operators.pop()](left_operand, right_operand)

    return left_operand


if __name__ == "__main__":
    result = solve("921*-8-4+")
    print(result)
