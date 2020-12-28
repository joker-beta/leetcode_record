# -*- coding:utf-8 -*-
""" leetcode-209. 长度最小的子数组
[题目]：
        给定一个含有 `n` 个正整数的数组和一个正整数 `s` ，
        找出该数组中满足其和 `≥ s` 的==长度最小==的 ==连续== 子数组，并返回其长度。
        如果不存在符合条件的子数组，返回 `0`。

[示例]：
	输入：s = 7, nums = [2,3,1,2,4,3]
	输出：2
	解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""

from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if (s == 0) or (nums == []) or (s > sum(nums)):
            return 0
        # 设置窗口左右位置的标记
        left, right = 0, 0
        # 统计连续数组的累加和
        ans = 0
        while right < len(nums):
            # 当前窗口累加的过程
            ans += nums[right]
            right += 1
            # 若当前窗口中的累加和超过s，那么一边将窗口左边界往右移动，一边更新窗口大小
            while (left < right) and (ans > s):
                ans = min(ans, right - left)
                ans -= nums[left]
                left += 1
        return ans


if __name__ == '__main__':
    while True:
        try:
            s = int(input().strip())
            nums = list(map(int, input().split()))
            print(Solution().minSubArrayLen(s, nums))
        except:
            break