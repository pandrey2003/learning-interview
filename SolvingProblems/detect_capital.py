# https://leetcode.com/problems/detect-capital/
def detect_capital_use(word: str) -> bool:
    return word == word.capitalize() or word == word.upper() or word == word.lower()
