# -*- coding:utf-8 -*-
""" leetcode-350. 两个数组的交集 II
[题目]：
        给定两个数组，编写一个函数来计算它们的交集。
"""

from typing import List

class Solution_1:
    """无序数组"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) <= len(nums1):
            nums1, nums2 = nums2, nums1
        ans = {}   # 统计nums1中各元素个数
        for num in nums1:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1
        res = []
        for i in range(len(nums2)):
            if (nums2[i] in nums1) and (ans[nums2[i]] != 0):
                res.append(nums2[i])
                ans[nums2[i]] -= 1    # 若nums2[i]中元素在nums1中也出现，则进行统计，并将ans中对应个数-1
        return res


class Solution_2:
    """若两个数组是排好序的"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        # 设置两个指针从数组的首位开始遍历对比
        left, right = 0, 0
        while (left < len(nums1)) and (right < len(nums2)):
            if nums1[left] == nums2[right]:
                ans.append(nums1[left])
                left += 1
                right += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                left += 1
        return ans