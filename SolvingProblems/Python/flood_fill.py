# https://leetcode.com/problems/flood-fill/


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        if image[sr][sc] == newColor:
            return image
        defaultColor = image[sr][sc]
        self.floodFillRecursive(image, sr, sc, newColor, defaultColor)
        return image

    def floodFillRecursive(self, image, sr, sc, newColor, defaultColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]) or image[sr][sc] != defaultColor:
            return
        image[sr][sc] = newColor
        self.floodFillRecursive(image, sr + 1, sc, newColor, defaultColor)
        self.floodFillRecursive(image, sr - 1, sc, newColor, defaultColor)
        self.floodFillRecursive(image, sr, sc + 1, newColor, defaultColor)
        self.floodFillRecursive(image, sr, sc - 1, newColor, defaultColor)
