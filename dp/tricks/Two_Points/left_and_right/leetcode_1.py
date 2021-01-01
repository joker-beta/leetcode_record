
# -*- coding:utf-8 -*-
""" leetcode-1. 两数之和
[题目]：
        给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 两个整数，
        并返回他们的数组==下标==。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""

from typing import List

class Solution_1:
    """方法一，双指针"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 记录数组长度
        n = len(nums)
        if n <= 1:
            return []
        # 新建一个数组用于最后返回找出的两数在原数组中的下标
        res = nums.copy()
        nums.sort()  # 排序
        left, right = 0, len(nums) - 1

        while left < right:
            # 若数组中的元素都是非负数，那么先做下面的判断可以提升效率
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
                # 若题目中需要去重复，可以添加下面的代码
                # while (left < right) and (nums[right] == nums[right + 1]):
                #    right -= 1
            elif s < target:
                left += 1
                # 用于去重复
                # while (left < right) and (nums[left] == nums[left - 1]):
                #    left += 1
            else:
                a1 = res.index(nums[left])
                res.pop(a1)
                a2 = res.index(nums[right])
                # 处理原数组nums中存在两个相同的数加和等于target，而对应下标不同的情况
                if a2 >= a1:
                    a2 += 1
                return [a1, a2]
        # 若遍历完整个数组后，仍然没有满足题目的数组，那么输出[]
        return []


class Solution_2:
    """方法二，哈希表法"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 记录数组长度
        n = len(nums)
        if n <= 1:
            return []
        # 创建字典，存放满足条件的数组
        dic = {}
        # 遍历数组，通过字典来判断是否存在满足条件的数
        for i, val in enumerate(nums):
            # 若当前遍历数为val，那么要凑成target，余下的数是res
            res = target - val
            # 若字典中已经存在res，那么直接输出下标
            if res in dic:
                return [dic[res], i]
            # 若余下的数res，字典中没有，那么把当前遍历数val添加到字典中
            else:
                dic[val] = i
        # 若遍历完整个数组nums，仍然没有满足条件的数组，那么输出[]
        return []