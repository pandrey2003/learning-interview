# https://leetcode.com/problems/max-area-of-island/
from typing import List


def max_area(grid: List[List[int]]) -> int:
    maximum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                area = max_area_recursive(grid, i, j)
                maximum = max(area, maximum)
    return maximum


def max_area_recursive(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    hor_and_vert = max_area_recursive(grid, i - 1, j) + max_area_recursive(grid, i + 1, j) + \
        max_area_recursive(grid, i, j + 1) + max_area_recursive(grid, i, j - 1)
    return hor_and_vert + 1
