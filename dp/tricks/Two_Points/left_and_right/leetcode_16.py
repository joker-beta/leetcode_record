# -*- coding:utf-8 -*-
""" leetcode-16. 最接近的三数之和
[题目]：
        给定一个包括 `n` 个整数的数组 `nums` 和 一个目标值 `target`。
        找出 `nums` 中的三个整数，使得它们的和与 `target` 最接近。返回这三个数的和。
        假定每组输入只存在唯一答案。
"""

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('INF')
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s >= target:
                    right -= 1
                    if s - target <= abs(ans - target):   # 替换与target更近的三元组
                        ans = s
                else:
                    left += 1
                    if target - s <= abs(ans - target):   # 替换与target更近的三元组
                        ans = s
        return ans