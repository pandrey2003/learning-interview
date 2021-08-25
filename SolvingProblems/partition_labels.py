# https://leetcode.com/problems/partition-labels/


def partitionLabels(self, s: str) -> list[int]:
        end_indexes = [0] * 26

        for i in range(len(s)):
            end_indexes[ord(s[i]) - ord('a')] = i

        result = []
        start, end = 0, 0

        for i in range(len(s)):
            end = max(end, end_indexes[ord(s[i]) - ord('a')])
            if i == end:
                result.append(i - start + 1)
                start = i + 1

        return result
