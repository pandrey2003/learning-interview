# https://leetcode.com/problems/plus-one/


def plus_one(digits: list[int]) -> list[int]:
    num = 0
    for index in range(len(digits)):
        num += digits[index] * 10 ** (len(digits) - index - 1)
    num += 1
    return [int(digit) for digit in str(num)]


def plus_one_better(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits


if __name__ == "__main__":
    print(plus_one_better([1, 2, 4]))
