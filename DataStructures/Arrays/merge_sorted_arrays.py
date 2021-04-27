def merge_sorted_lists(f_list: list, s_list: list):
    # Time complexity: O(n)
    # Space complexity: O(1)
    merged_list = []
    while f_list or s_list:
        if not f_list:
            merged_list.extend(s_list)
            break
        if not s_list:
            merged_list.extend(f_list)
            break
        if f_list[0] <= s_list[0]:
            merged_list.append(f_list[0])
            f_list.pop(0)
            continue
        merged_list.append(s_list[0])
        s_list.pop(0)
    return merged_list


if __name__ == "__main__":
    # Casual cases
    print(merge_sorted_lists([0,3,4,31], [4, 6, 30]))
    print(merge_sorted_lists([1, 2, 3, 4, 5], [2, 9, 11, 90]))
    # Extreme cases
    print(merge_sorted_lists([0, 1], []))
    print(merge_sorted_lists([], []))
