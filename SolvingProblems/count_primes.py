# https://leetcode.com/problems/count-primes/
def count_primes(n: int) -> int:
    # Created after reading about sieve of eratosthenes
    booleans = [True] * n
    i = 2
    while i ** 2 < n:
        if booleans[i]:
            for j in range(i ** 2, n, i):
                booleans[j] = False
        i += 1
    count_booleans = 0
    for i in range(2, len(booleans)):
        if booleans[i]:
            count_booleans += 1
    return count_booleans
