# https://www.lintcode.com/problem/645/description
"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        return self.recursive_pairs(n, list(range(n)))

    def recursive_pairs(self, n: int, n_list: list):
        if len(n_list) == 1:
            only_candidate = n_list[0]
            for i in range(n):
                if i == only_candidate:
                    continue
                if Celebrity.knows(only_candidate, i) or not Celebrity.knows(i, only_candidate):
                    return -1
            return only_candidate
        shortened_list = []
        if len(n_list) % 2 != 0:
            shortened_list.append(n_list[-1])
        for i in range(0, len(n_list) - 1, 2):
            if Celebrity.knows(n_list[i], n_list[i + 1]):
                shortened_list.append(n_list[i + 1])
            else:
                shortened_list.append(n_list[i])
        return self.recursive_pairs(n, shortened_list)


def find_celebrity(n):
    candidate = 0
    for i in range(1, n):
        if Celebrity.knows(candidate, i):
            candidate = i
    for i in range(n):
        if i != candidate and Celebrity.knows(candidate, i) or not Celebrity.knows(i, candidate):
            return -1
    return candidate
