mapping = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}


def letter_combinations(digits: str) -> list[str]:
    if digits == "":
        return []
    answer = []

    def dfs(position: int, string: str):
        if position == len(digits):
            answer.append(string)
        else:
            global mapping
            letters = mapping[digits[position]]
            for letter in letters:
                dfs(position + 1, string + letter)

    dfs(0, "")
    return answer


def letter_combinations_itertools(digits: str) -> list[str]:
    if digits == "":
        return []
    all_iterables = []
    for digit in digits:
        all_iterables.append(mapping[digit])
    from itertools import product
    combinations_as_tuples = list(product(*all_iterables))
    return ["".join(w) for w in combinations_as_tuples]


if __name__ == "__main__":
    print(letter_combinations("23"))
    print(letter_combinations_itertools("23"))
    print(letter_combinations_itertools("469"))
