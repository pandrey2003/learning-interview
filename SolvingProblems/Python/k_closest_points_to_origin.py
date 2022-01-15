# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 >= other.x ** 2 + other.y ** 2


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    points = [Point(point[0], point[1]) for point in points]
    max_heap = []
    for point in points:
        heapq.heappush(max_heap, point)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    max_heap = [[point.x, point.y] for point in max_heap]
    return max_heap
