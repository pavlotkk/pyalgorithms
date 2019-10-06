#
#                          abc
#                        /  |  \
#                       /   |   \
#                      /    |    \
#                     /     |     \
#                    /      |      \
#                   /       |       \
#        a -> a    /      a -> b     \    a -> c
#                 /         |         \
#                /          |          \
#               /           |           \
#              /            |            \
#             /             |             \
#            /              |              \
#         [a]bc           [b]ac          [c]ba
#          / \             / \            / \
#         /   \           /   \          /   \
#        /     \         /     \        /     \
#       /       \       /       \      /       \
#     [ab]c   [ac]b   [ba]c   [bc]a   [cb]a   [ca]b

from typing import List


def _simple_recursion_permutation(text: List[str], start: int, end: int):
    if start == end:
        yield "".join(text)
        return

    for i in range(start, end + 1):
        text[start], text[i] = text[i], text[start]
        yield from _simple_recursion_permutation(text, start + 1, end)
        text[start], text[i] = text[i], text[start]


def simple_recursion_permutation(text: str) -> str:
    yield from _simple_recursion_permutation(list(text), 0, len(text) - 1)


if __name__ == "__main__":
    from datetime import datetime
    string = "abcdefghij"

    start = datetime.now()
    for next_value in simple_recursion_permutation(string):
        print(next_value)
    end = datetime.now()

    print((end - start).total_seconds())
