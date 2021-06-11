# https://leetcode.com/problems/number-complement/


def find_complement(num: int) -> int:
    result = 0
    power = 1
    while num > 0:
        result += (num % 2 ^ 1) * power
        power <<= 1
        num >>= 1
    return result
