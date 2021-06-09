# https://leetcode.com/problems/power-of-two/


def is_power_of_two(n: int) -> bool:
    for i in range(n):
        check_num = 2 ** i
        if n == check_num:
            return True
        if check_num < n:
            continue
        return False


def is_power_of_two_tutorial(n: int) -> bool:
    num = 1
    while num < n:
        num *= 2
    return num == n
