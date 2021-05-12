def merge_sorted_lists(f_list: list, s_list: list):
    # Time complexity: O(n)
    # Space complexity: O(1)
    merged_list = []
    f_list_index = 0
    s_list_index = 0
    while f_list_index < len(f_list) or s_list_index < len(s_list):
        if f_list_index == len(f_list):
            merged_list.extend(s_list[s_list_index:])
            break
        if s_list_index == len(s_list):
            merged_list.extend(f_list[f_list_index:])
            break
        if f_list[f_list_index] <= s_list[s_list_index]:
            merged_list.append(f_list[f_list_index])
            f_list_index += 1
            continue
        merged_list.append(s_list[s_list_index])
        s_list_index += 1
    return merged_list


if __name__ == "__main__":
    # Casual cases
    print(merge_sorted_lists([0,3,4,31], [4, 6, 30]))
    print(merge_sorted_lists([1, 2, 3, 4, 5], [2, 9, 11, 90]))
    # Extreme cases
    print(merge_sorted_lists([0, 1], []))
    print(merge_sorted_lists([], []))
