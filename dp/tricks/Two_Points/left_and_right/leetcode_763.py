# -*- coding:utf-8 -*-
""" leetcode-763. 划分字母区间
[题目]：
        字符串 `S` 由小写字母组成。
        我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
        返回一个表示每个字符串片段的长度的列表。
"""

from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 第一次遍历，统计各字符最后出现的下标位置
        last_idex = [0 for i in range(26)]
        for i, s in enumerate(S):
            last_idex[ord(s) - ord('a')] = i      # ord() 返回字符的ASCII码
        ans = []
        # 第二次遍历，找出各子串结束位置，用于划分子串
        left, right = 0, 0
        for i, s in enumerate(S):
            right = max(right, last_idex[ord(s) - ord('a')])
            if right == i:
                ans.append(right - left + 1)
                left = right + 1
        return ans