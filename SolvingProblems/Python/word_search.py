# https://leetcode.com/problems/word-search/
def exist(board: list[list[str]], word: str) -> bool:
    results = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                result = exists_word_recursive(board, i, j, word, 0, set())
                results.add(result)
    return bool(any(results))


def exists_word_recursive(board, i, j, word, index, current):
    if index == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[index] or (i, j) in current:
        return False
    board[i][j] = None
    down = exists_word_recursive(board, i + 1, j, word, index + 1, current.copy())
    up = exists_word_recursive(board, i - 1, j, word, index + 1, current.copy())
    right = exists_word_recursive(board, i, j + 1, word, index + 1, current.copy())
    left = exists_word_recursive(board, i, j - 1, word, index + 1, current.copy())
    return down or up or right or left


if __name__ == "__main__":
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
