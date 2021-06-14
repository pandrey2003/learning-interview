# https://leetcode.com/problems/battleships-in-a-board/


class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        if board is None or len(board) == 0:
            return 0
        num_battleships = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    num_battleships += self.dfs(board, i, j)
        return num_battleships

    def dfs(self, board: list[list[str]], i: int, j: int):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] == ".":
            return 0
        board[i][j] = "."
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)
        return 1
