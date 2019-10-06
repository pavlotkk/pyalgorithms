# https://en.wikipedia.org/wiki/Heap%27s_algorithm

from typing import List


def _heaps_permutation(text: List[str], n: int) -> str:
    if n == 0:
        yield "".join(text)
        return

    for i in range(n - 1):
        yield from _heaps_permutation(text, n - 1)

        if i % 2 == 0:
            text[i], text[n - 1] = text[n - 1], text[i]
        else:
            text[0], text[n - 1] = text[n - 1], text[0]

    yield from _heaps_permutation(text, n - 1)


def heaps_permutation(text: str) -> str:
    yield from _heaps_permutation(list(text), len(text))


if __name__ == "__main__":
    from datetime import datetime
    string = "abcdefghij"
    # string = "abc"

    start = datetime.now()
    for next_value in heaps_permutation(string):
        print(next_value)
    end = datetime.now()

    print((end - start).total_seconds())
