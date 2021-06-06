def classical_fibonacci(n):
    if n < 2:
        return n
    print("classical - long time")
    return classical_fibonacci(n-1)+classical_fibonacci(n-2)


def memoized_fibonacci():
    cache = {0: 0, 1: 1}

    def wrapped_fibonacci(n):
        nonlocal cache
        if cache.get(n) is not None:
            return cache[n]
        print("memoized - long time")
        cache[n] = wrapped_fibonacci(n-1) + wrapped_fibonacci(n-2)
        return cache[n]
    return wrapped_fibonacci


if __name__ == "__main__":
    # The calls below take A LOT of steps
    print(classical_fibonacci(4))
    print(classical_fibonacci(11))
    # The calls below are memoized
    memoized = memoized_fibonacci()
    print(memoized(4))
    print(memoized(11))
