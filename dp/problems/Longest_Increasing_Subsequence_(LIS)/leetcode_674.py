# -*- coding:utf-8 -*-
""" leetcode-674
[题目]：
        给定一个**未经排序**的整数数组，找到最长且**连续的的递增序列**，并返回该序列的**长度**。

示例 1:
	输入: [1,3,5,4,7]
	输出: 3
	解释: 最长连续递增序列是 [1,3,5], 长度为3。
	尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
"""

class Solution:
    def findLengthOfLCIS(self, nums):
        if nums == []:
            return 0
        # dp[i] 用来统计以 nums[i] 结尾的最长连续递增子序列长度
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            # 原来数组可能存在重复元素，所以要求严格递增
            if nums[i-1] < nums[i]:
                dp[i] = max(dp[i], dp[i-1] + 1)

        return max(dp)


arr = [1, 3, 5, 4, 7]
print(Solution().findLengthOfLCIS(arr))