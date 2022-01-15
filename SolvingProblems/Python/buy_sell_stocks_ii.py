# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


def max_profit(prices: list[int]) -> int:
    if prices is None or len(prices) <= 1:
        return 0
    profit = 0
    for i in range(len(prices) - 1):
        diff_next_and_cur = prices[i + 1] - prices[i]
        if diff_next_and_cur > 0:
            profit += diff_next_and_cur
    return profit
