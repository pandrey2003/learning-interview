class Solution:
    # Recursive solution giving "Time Limit Exceeded"
    def uniquePaths(self, m: int, n: int) -> int:
        return 1 + self.uniquePathsRecursive(m, n, 1, 1)

    def uniquePathsRecursive(self, m: int, n: int, curr_m: int, curr_n: int) -> int:
        if curr_m >= m or curr_n >= n:
            return 0
        return 1 + self.uniquePathsRecursive(m, n, curr_m + 1, curr_n) \
            + self.uniquePathsRecursive(m, n, curr_m, curr_n + 1)
