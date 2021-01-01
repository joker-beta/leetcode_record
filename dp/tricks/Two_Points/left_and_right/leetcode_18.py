# -*- coding:utf-8 -*-
""" leetcode-18. 四数之和
[题目]：
        给定一个包含 `n` 个整数的数组 `nums` 和一个目标值 `target`，
        判断 `nums` 中是否存在四个元素 `a，b，c` 和 `d` ，
        使得 `a + b + c + d` 的值与 `target` 相等？找出所有满足条件且不重复的四元组。"""

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()   # 避免在循环中调用太多的while去重
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left, right = j+1, len(nums)-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1
        return list(ans)