# https://www.lintcode.com/problem/663/
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms):
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    self.dfs(i, j, 0, rooms)

    def dfs(self, i, j, distance, rooms):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[i]) or rooms[i][j] < distance:
            return
        rooms[i][j] = distance
        self.dfs(i + 1, j, distance + 1, rooms)
        self.dfs(i - 1, j, distance + 1, rooms)
        self.dfs(i, j + 1, distance + 1, rooms)
        self.dfs(i, j - 1, distance + 1, rooms)
        return rooms
