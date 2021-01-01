# -*- coding:utf-8 -*-
""" leetcode-704. 二分查找
[题目]：
        给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target`  ，
        写一个函数搜索 `nums` 中的 `target`，如果目标值存在返回下标，否则返回 `-1`。
"""

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 若目标数不在数组范围内，直接返回-1
        if (target < nums[0]) or (target > nums[-1]):
            return -1
        # 设置双指针，用于划分数组
        left, right = 0, len(nums) - 1

        while left < right:
            # 避免溢出
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 由于上面的while循环是<号
        # 所以在结束循环后还有再判断一次当前位置数，是否为目标值！！！
        if nums[left] == target:
            return left
        else:
            return -1


