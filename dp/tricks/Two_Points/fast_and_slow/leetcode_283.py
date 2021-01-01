
# -*- coding:utf-8 -*-
""" leetcode-283. 移动零
[题目]：
        给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，
        同时保持非零元素的相对顺序。
"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 利用快慢指针将数组中的0全部删除
        # 也就是把非0元素全部移动到数组前面
        fast = slow = 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # 数组中0的个数
        n = len(nums[slow:])
        # 将数组后n个数全部赋值为0
        for i in range(n):
            nums[slow + i] = 0