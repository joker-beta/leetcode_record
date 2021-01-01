# -*- coding:utf-8 -*-
""" leetcode-141. 环形链表
[题目]：给定一个链表，判断链表中是否有环。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (not head) or (not head.next):
            return False
        # 设置快慢指针
        slow = head
        fast = head.next     # 设置 fast = head 也可以
        while (fast and fast.next):
        # 若快指针fast在走到链表尾部之前能和慢指针slow遇到，说明链表中有环
            if (fast == slow):
                return True
            # 若还没有遇到，那么两个指针继续往后走
            fast = fast.next.next
            slow = slow.next
        return False