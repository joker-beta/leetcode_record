# -*- coding:utf-8 -*-
""" leetcode-83. 删除排序==链表==中的重复元素
[题目]：
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        # 设置快慢指针，从头结点开始
        fast = slow = head
        while fast:
            # 若当前快指针节点值不等于慢指针节点值
            # 说明当前节点值不是重复节点，那么将慢指针的接到快指针节点，同时移动慢指针
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        # 当快指针遍历完整个链表，即找完全部非重复节点后
        # 此时慢指针位于所有非重复节点的最后一个，那么直接将该位置的下一个节点连接空指针，输出！！！
        slow.next = None

        return head