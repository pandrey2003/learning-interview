def next_closest_time(time):
    minutes = int(time[:2]) * 60
    minutes += int(time[3:])

    digits = set()
    for char in time:
        if char == ":":
            continue
        digits.add(int(char))

    while True:
        minutes = (minutes + 1) % (24 * 60)
        next_time = {
            minutes // 60 // 10,
            minutes // 60 % 10,
            minutes % 60 // 10,
            minutes % 60 % 10,
        }
        if next_time - digits == set():
            return "%02d:%02d" % (minutes // 60, minutes % 60)


if __name__ == "__main__":
    print(next_closest_time("19:34"))
