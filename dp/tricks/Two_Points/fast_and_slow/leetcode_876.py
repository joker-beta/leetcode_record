# -*- coding:utf-8 -*-
""" leetcode-876. 链表的中间结点
[题目]：
        给定一个带有头结点 `head` 的非空单链表，返回链表的中间结点(==奇数长度==)。
        如果有两个中间结点，则返回第二个中间结点(==偶数长度==)。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
    	# 设置快慢指针
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return head
            if not (fast.next.next):
                return head.next

            fast = fast.next.next
            slow = slow.next
			# 若链表长度为偶数，返回中间两个节点后一个
            if (fast.next != None):
                if fast.next.next == None:
                    return slow.next
            # 若链表长度为奇数，直接返回中间节点
            else:
                return slow