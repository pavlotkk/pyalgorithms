# You have a string template, e.g. "a?b??c?d".
# Need to replace all "?" with "1" or "0" with any possible combinations.
# Solution can't use itertools and other libs.
#
# Input:
# a?b??c?d
#
# Output:
# a0b00c0d
# a0b00c1d
# a0b01c0d
# a0b01c1d
# a0b10c0d
# ...
# a1b11c1d
from typing import Generator


def solve(template: str) -> Generator:
    count = 0
    for x in template:
        if x == "?":
            count += 1

    for i in range(count ** 2):
        ss = template
        bin_format = "{:0>" + str(count) + "b}"
        for x in bin_format.format(i):
            ss = ss.replace("?", x, 1)
        yield ss


if __name__ == "__main__":
    template = "a?b??c?d"
    print(f"Input:\n{template}\n")
    print("Output")

    for t in solve(template):
        print(t)
