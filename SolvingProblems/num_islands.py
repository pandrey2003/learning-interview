# https://leetcode.com/problems/number-of-islands/


class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_islands += self.dfs(grid, i, j)
        return num_islands

    def dfs(self, grid: list[list[str]], i: int, j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
        grid[i][j] = "0"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        return 1
