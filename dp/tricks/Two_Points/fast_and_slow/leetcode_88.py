
# -*- coding:utf-8 -*-
""" leetcode-88. 合并两个有序数组
[题目]：
        给你两个有序整数数组 `nums1` 和 `nums2`，请你将 `nums2` 合并到 `nums1` 中，
        使 `nums1` 成为一个有序数组。
"""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 先将nums1的前m个待对比元素存起来
        num1_copy = nums1[:m]
        # 将 nums1重置为[]
        nums1[:] = []
        # 设置两个对比指针来遍历nums1和nums2
        p1, p2 = 0, 0
        while (p1 < m) and (p2 < n):
            if num1_copy[p1] < nums2[p2]:
                nums1.append(num1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        # 若num2长度较短，将nums1余下的元素直接加到新nums1后
        if p1 < m:
            nums1[p1+p2:] = num1_copy[p1:]
        # 反之，将nums2余下元素加到新nums1后
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:]
        return nums1