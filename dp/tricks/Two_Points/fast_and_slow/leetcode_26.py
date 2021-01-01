# -*- coding:utf-8 -*-
""" leetcode-26. 删除排序==数组==中的重复项
[题目]：
        给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，
        返回移除后数组的==新长度==。
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        # 设置快慢指针，从数组头开始遍历
        fast = slow = 0
        while fast < len(nums):
            # 若当前快指针遍历的数在前面没有出现过，让慢指针往右移动一步
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            # 否则，接着让快指针往右移动，遍历下一个判断
            fast += 1
        # 由于快慢指针初始化设置的是数组下标，而下标从0开始
        # 因此最后输出的时候+1
        return slow + 1