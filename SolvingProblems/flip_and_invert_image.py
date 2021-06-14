# https://leetcode.com/problems/flipping-an-image/


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        # Flipping
        for i in range(len(image)):
            image[i] = image[i][::-1]
        # Inverting
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
