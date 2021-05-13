def selection_sort(input_list: list):
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    if not (isinstance(input_list, list) and input_list):
        return TypeError("Check your input")
    for traverse_index in range(len(input_list), 0, -1):
        for i in range(len(input_list)-traverse_index+1, len(input_list)):
            if input_list[i] < input_list[len(input_list)-traverse_index]:
                input_list[i], input_list[len(input_list)-traverse_index] = \
                    input_list[len(input_list)-traverse_index], input_list[i]
    return input_list


if __name__ == "__main__":
    print("Sorting [1, 5, 3, 2, 9, 8, 6]:",
    selection_sort([1, 5, 3, 2, 9, 8, 6]))
    print("Sorting [7, 2, 1, 9, 3, 2]:",
    selection_sort([7, 2, 1, 9, 3, 2]))
