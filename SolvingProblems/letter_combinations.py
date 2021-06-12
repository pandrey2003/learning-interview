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


if __name__ == "__main__":
    print(letter_combinations("23"))
