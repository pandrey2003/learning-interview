# https://leetcode.com/problems/merge-k-sorted-lists/
from queue import PriorityQueue


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists:
        return lists
    head = point = ListNode(0)
    q = PriorityQueue()
    setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
    for linked_list in lists:
        if linked_list:
            q.put((linked_list.val, linked_list))
    while not q.empty():
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, node))
    return head.next
