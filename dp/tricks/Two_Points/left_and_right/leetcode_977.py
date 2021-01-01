# -*- coding:utf-8 -*-
""" leetcode-977. 有序数组的平方
[题目]：
        给定一个按非递减顺序排序的整数数组 `A`，
        返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
"""

from typing import List

# [思路]：我们可以使用两个指针分别指向位置 0 和 n-1，每次比较两个指针对应的数，
# 选择较大的那个逆序放入答案并移动指针。这种方法无需处理某一指针移动至边界的情况。
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(n)]
        left, right = 0, n-1
        tmp = n-1
        while left <= right:
            if -nums[left] > nums[right]:
                ans[tmp] = nums[left]**2
                left += 1
            else:
                ans[tmp] = nums[right]**2
                right -= 1
            tmp -= 1
        return ans