def max_subarray_sum(lst: list):
    if not (isinstance(lst, list) and len(lst) >= 1):
        raise TypeError
    max_sum = lst[0]
    current_sum = max_sum
    for number in lst[1:]:
        current_sum = max(number + current_sum, number)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    print(
        f"Max subarray sum for [-2,2,5,-11,6] is "
        f"{max_subarray_sum([-2,2,5,-11,6])}"
    )
