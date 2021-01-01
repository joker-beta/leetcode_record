# -*- coding:utf-8 -*-
""" leetcode-142. 环形链表 II
[题目]：给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 `null`。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 设置快慢指针
        fast, slow = head, head
        # 找出快慢指针的相遇点
        while True:
            if not(fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                break
        # 这是快慢指针位于相遇点
        # 重新设置一个节点指针res，让其和slow同时遍历，
        # 那么第一次相遇的节点即为所求。
        res = head
        while (res != slow):
            res = res.next
            slow = slow.next
        return slow