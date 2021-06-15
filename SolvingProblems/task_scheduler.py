def least_interval(tasks: list[str], n: int) -> int:
    if n == 0:  # not important, just saves a bit of time
        return len(tasks)
    import collections
    frequency = collections.Counter(tasks)
    m = max(frequency.values())  # what is the freq of the most frequent task
    c = collections.Counter(list(frequency.values()))[m]  # how many tasks do we have at that max frequency
    return max(len(tasks), (m - 1) * (n + 1) + c)


if __name__ == "__main__":
    print(least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
