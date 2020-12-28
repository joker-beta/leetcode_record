# -*- coding:utf-8 -*-
""" leetcode-713. 乘积小于K的子数组
[题目]：
        给定一个正整数数组 `nums`。找出该数组内==乘积小于 `k` 的连续的子数组的个数==。

示例 1:
		输入: nums = [10,5,2,6], k = 100
		输出: 8
		解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5],[5,2], [2,6], [5,2,6]。
		需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

说明:
* 0 < nums.length <= 50000
* 0 < nums[i] < 1000
* 0 <= k < 10^6
"""

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        n = len(nums)
        left, right = 0, 0
        pre = 1   # 累乘初始单位
        ans = 0   # 统计个数
        while right < len(nums):
            pre *= nums[right]
            right += 1
            # 当累乘大于target时，开始收缩窗口
            while (left < right) and (pre >= target):
                pre /= nums[left]
                left += 1
            # 由于单个的元素也算作一个集合，所以当前满足条件的窗口中的集合个数为right-left
            ans += right - left
        return ans




if __name__ == '__main__':
    while True:
        try:
            k = int(input().strip())
            nums = list(map(int, input().split()))
            print(Solution().numSubarrayProductLessThanK(nums, k))
        except:
            break