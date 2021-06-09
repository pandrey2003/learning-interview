# https://leetcode.com/problems/fizz-buzz/


def fizz_buzz(n: int) -> list[str]:
    end_list = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            end_list.append("FizzBuzz")
        elif i % 3 == 0:
            end_list.append("Fizz")
        elif i % 5 == 0:
            end_list.append("Buzz")
        else:
            end_list.append(str(i))
    return end_list
