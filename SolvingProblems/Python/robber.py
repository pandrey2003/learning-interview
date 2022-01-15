def rob(lst_of_int: list[int]):
    l_length = len(lst_of_int)
    if l_length == 0:
        return 0
    if l_length == 1:
        return lst_of_int[0]
    if l_length == 2:
        return max(lst_of_int[0], lst_of_int[1])
    dp = [lst_of_int[0], max(lst_of_int[0], lst_of_int[1])]
    for i in range(2, l_length):
        dp.append(max(lst_of_int[i] + dp[i-2], dp[i-1]))
    return dp[l_length-1]


if __name__ == "__main__":
    print(rob([1,7,3,6,8,10,17]))
