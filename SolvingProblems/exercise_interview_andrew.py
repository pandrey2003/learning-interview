# Given two lists, create a function
# which lets a user know (True/False) if these two lists
# contain any common items
# For example:
# l1 = ['a', 'b', 'c', 'd']
# l2 = ['e', 'f', 'g']
# should return False
# ------
# l1 = ['a', 'b', 'c', 'd']
# l2 = ['d', 'e', 'f', 'g']
# should return True

# 2 parameters - lists - no size limit
# return True or False

# Solution #1
# Brute force/naive: nested loops, comparing each item in one list
# to each item in another loop
# O(n^2) time complexity - discouraged.

# Solution #2 (mine personally)
# Converting to sets and then finding intersection
def find_if_contains_common_items(f_list: list, s_list: list):
    f_set = set(f_list)  # time: O(n), space: O(n)
    s_set = set(s_list)  # time: O(n), space: O(n)
    set_intersection = f_set.intersection(s_set)
    # time: O of min len of sets, O(n);
    # space: O(n) - the same logic as single intersection
    return bool(set_intersection)


# The solution above has O(n) time and O(n) space complexity.
# Tests for solution #2:
import unittest
class TestSolutionTwo(unittest.TestCase):
    def test_no_intersections(self):
        self.assertEqual(
            find_if_contains_common_items(["a", "b", "c"], ["d", "e"]),
            False
        )
    
    def test_found_intersection(self):
        self.assertEqual(
            find_if_contains_common_items([1, "d", "9"], ["d", "1", 9]),
            True
        )


unittest.main()