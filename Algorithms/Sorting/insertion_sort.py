def insertion_sort(input_lst: list):
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    if not isinstance(input_lst, list):
        raise TypeError("Check your input")
    for i in range(len(input_lst)):
        if input_lst[i] <= input_lst[0]:
            input_lst.insert(0, input_lst.pop(i))
            continue
        for trav_index in range(i):
            if input_lst[trav_index] <= input_lst[i] \
                <= input_lst[trav_index+1]:
                input_lst.insert(trav_index+1, input_lst.pop(i))
    return input_lst


if __name__ == "__main__":
    print("Sorting [1, 5, 3, 2, 9, 8, 6]:",
    insertion_sort([1, 5, 3, 2, 9, 8, 6]))
    print("Sorting [7, 2, 1, 9, 3, 2]:",
    insertion_sort([7, 2, 1, 9, 3, 2]))
    print("Sorting [9, 0, 2, 6, 1, 18, 13]",
    insertion_sort([9, 0, 2, 6, 1, 18, 13]))
