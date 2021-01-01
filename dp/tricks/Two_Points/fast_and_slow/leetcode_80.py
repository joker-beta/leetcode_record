# -*- coding:utf-8 -*-
""" leetcode-80. 删除排序数组中的重复项 II
[题目]：给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现==两==次，
        返回移除后数组的==新长度==。
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, count = 1, 1
        for fast in range(1, len(nums)):
            # 统计重复项
            if nums[fast] == nums[fast-1]:
                count += 1
            else:
                count = 1
            # 对个数大于2的数组元素进行覆盖
            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1
        return slow