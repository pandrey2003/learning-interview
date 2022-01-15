# https://leetcode.com/problems/boats-to-save-people/
def num_rescue_boats(people: list[int], limit: int) -> int:
    people.sort()  # This gives O(n * log n) for time complexity (timsort)
    num_boats = 0
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        num_boats += 1
    return num_boats
