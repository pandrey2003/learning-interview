# https://leetcode.com/problems/happy-number/
def isHappy(n: int) -> bool:
    seen = set()
    while n != 1:
        current = n
        digit_sum = 0
        while current != 0:
            digit_sum += (current % 10) ** 2
            current //= 10
        if digit_sum in seen:
            return False
        seen.add(digit_sum)
        n = digit_sum
    return True
