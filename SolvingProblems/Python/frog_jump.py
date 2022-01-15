# https://leetcode.com/problems/frog-jump/
def can_cross(self, stones: list[int]) -> bool:
    for i in range(3, len(stones)):
        if stones[i] > stones[i - 1] * 2:
            return False
    last_stone = stones[-1]
    positions, jumps = [], []
    hash_set_stones = set(stones)
    positions.append(0)
    jumps.append(0)
    while positions:
        position = positions.pop()
        jump = jumps.pop()
        for i in range(jump - 1, jump + 2):
            if i <= 0:
                continue
            next_position = position + i
            if next_position == last_stone:
                return True
            if next_position in hash_set_stones:
                positions.append(next_position)
                jumps.append(i)
    return False
