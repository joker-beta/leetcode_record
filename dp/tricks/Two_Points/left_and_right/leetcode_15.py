# -*- coding:utf-8 -*-
""" leetcode-15. 三数之和
[题目]：
        给你一个包含 `n` 个整数的数组 `nums`，判断 `nums` 中是否存在三个元素 `a`，`b`，`c` ，
        使得 `a + b + c = 0` ？请你找出所有满足条件且不重复的三元组。
"""

from typing import List
class Solution_1:
    """方法一，手动去重"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        # 存放满足条件的数组
        ans = []
        # 原数组排序
        nums.sort()
        # 选择最左边的数遍历，所以只能遍历到n-3，右边留两个数用双指针
        for k in range(len(nums) - 2):
            # 由于nums已经排序，所以nums[k] < nums[i] < nums[j]
            # 要是 nums[k]>0，说明三数和不等于0
            if nums[k] > 0:
                break
            # 从k=1开始，若当前遍历数与前面已经遍历过的数重复，直接跳过
            if (k > 0) and (nums[k] == nums[k - 1]):
                continue
            # 接下来从k+1位置开始，使用双指针
            left, right = k + 1, len(nums) - 1
            while left < right:
                # 记录当前遍历的三数和，记为 s
                s = nums[k] + nums[left] + nums[right]
                # 1，若当前累加和大于0，说明right需要左移
                if s > 0:
                    right -= 1
                    # 同时还需要判断移动之后的数是否与之前的数相同，若相同直接跳过，right -= 1
                    while (left < right) and (nums[right] == nums[right + 1]):
                        right -= 1
                # 2，若当前累加和小于0，说明left需要右移
                elif s < 0:
                    left += 1
                    # 同时还需要判断移动之后的数是否与之前的数相同，若相同直接跳过，left += 1
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1
                # 3，若当前累加和等于0，说明找到一组数组，直接添加到ans
                else:
                    ans.append([nums[k], nums[left], nums[right]])
                    # 添加完成后，往中间收缩双指针
                    left += 1
                    right -= 1
                    # 收缩的同时还需要判断元素是否重复，若有重复直接跳过
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right) and (nums[right] == nums[right + 1]):
                        right -=1
        return ans



class Solution_2:
    """方法二，调用set()去重"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        ans = set()  # 避免下面循环过程中多次调用while去重
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return list(ans)