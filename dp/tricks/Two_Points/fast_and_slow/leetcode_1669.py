# -*- coding:utf-8 -*-
""" leetcode-1669. 合并两个链表
[题目]：
        给你两个链表 `list1` 和 `list2` ，它们包含的元素分别为 `n` 个和 `m` 个。
        请你将 `list1` 中第 `a` 个节点到第 `b` 个节点删除，并将`list2` 接在被删除节点的位置。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        slow, fast = list1, list1
        # 快指针先走b-a+1各节点
        tmp = b - a + 2
        while tmp > 0:
            fast = fast.next
            tmp -= 1
        # 然后，快慢指针同时走a-1个节点，那么slow到第a-1节点，fast到b+1节点
        for _ in range(a - 1):
            slow = slow.next
            fast = fast.next
        # 设置一个临时指针遍历到list2尾节点，方便链接fast
        plist2 = list2
        while plist2.next:
            plist2 = plist2.next
        slow.next = list2
        plist2.next = fast

        return list1