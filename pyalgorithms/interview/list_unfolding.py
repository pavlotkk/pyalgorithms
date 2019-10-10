# Convert list with sublists into one-dimensioned list with saving order
# Input:
# [1, 2, [3, 4, [[5, 6], [7, 8, 9], 10]], 11, 12]
#
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12]

input_data = [1, 2, [3, 4, [[5, 6], [7, 8, 9], 10]], 11, 12]


def solve_recursion(lst: list):
    result = []

    for item in lst:
        if type(item) is list:
            result += solve_recursion(item)
            continue
        result.append(item)

    return result


def solve_linear(lst: list):

    result = None
    is_valid_array = False

    while not is_valid_array:
        result = []
        for item in lst:
            if type(item) is not list:
                result.append(item)
            else:
                for i in item:
                    result.append(i)
                lst = result

        is_valid_array = True
        for item in result:
            if type(item) is list:
                is_valid_array = False
                break

    return result


if __name__ == "__main__":
    input_data = [1, 2, [3, 4, [[5, 6], [7, 8, 9], 10]], 11, 12]

    print(f"Linear solve:\n"
          f"Input:\n{input_data}\n"
          f"Output:\n{solve_recursion(input_data)}"
    )

    print("\n\n")
    print(f"Recursive solve:\n"
          f"Input:\n{input_data}\n\n"
          f"Output:\n{solve_linear(input_data)}"
    )
