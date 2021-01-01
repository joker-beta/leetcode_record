# -*- coding:utf-8 -*-
""" leetcode-27. 移除元素
[题目]：给你一个数组 `nums` 和一个值 `val`，你需要 原地 移除所有数值等于 `val` 的元素，
        并返回移除后数组的新长度。
"""

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        # 设置快慢指针，从数组头开始
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return len(nums[:slow])