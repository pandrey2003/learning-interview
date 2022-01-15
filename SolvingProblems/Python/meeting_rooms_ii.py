import heapq


def min_meeting_rooms(intervals):
    # Time complexity: O(n* log n), space complexity: O(1)
    if intervals is None or len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x.start)  # O(n*log n) is here
    count = 0
    min_heap = []
    for interval in intervals:
        if not min_heap:
            count += 1
            heapq.heappush(min_heap, interval.end)
            continue
        if interval.start >= min_heap[0]:
            heapq.heappop(min_heap)
        else:
            count += 1
        heapq.heappush(min_heap, interval.end)
    return count
