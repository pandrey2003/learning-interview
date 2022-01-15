# https://leetcode.com/problems/unique-paths/
class Solution:
    # Recursive solution giving "Time Limit Exceeded"
    def uniquePaths(self, m: int, n: int) -> int:
        return 1 + self.uniquePathsRecursive(m, n, 1, 1)

    def uniquePathsRecursive(self, m: int, n: int, curr_m: int, curr_n: int) -> int:
        if curr_m >= m or curr_n >= n:
            return 0
        return 1 + self.uniquePathsRecursive(m, n, curr_m + 1, curr_n) \
            + self.uniquePathsRecursive(m, n, curr_m, curr_n + 1)


def unique_paths_dp(m: int, n: int) -> int:
    dp = [[0] * m] * n
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(1, len(dp[0])):
        dp[0][i] = 1
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
