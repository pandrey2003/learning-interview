# https://leetcode.com/problems/valid-parentheses


def valid_parenthesis_andrew(s: str) -> bool:
    match = {"(": ")", "[": "]", "{": "}"}
    order = []  # The stack logic
    for char in s:
        if char in {"(", "[", "{"}:
            order.append(char)
            continue
        if not order:
            return False
        last_opened_parenthesis = order.pop()
        if char != match[last_opened_parenthesis]:
            return False
    return True if not order else False
