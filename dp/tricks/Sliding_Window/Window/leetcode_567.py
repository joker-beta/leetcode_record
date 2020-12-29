# -*- coding:utf-8 -*-
""" leetcode-567. 字符串的排列 (困难)
[题目]：
        给定两个字符串 `s1` 和 `s2`，写一个函数来判断 `s2` 是否包含 `s1` 的排列。
        换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
	输入: s1 = "ab" s2 = "eidbaooo"
	输出: True
	解释: s2 包含 s1 的排列之一 ("ba"). 

示例2:
	输入: s1= "ab" s2 = "eidboaoo"
	输出: False

注意：
* 输入的字符串只包含小写字母
* 两个字符串的长度都在 `[1, 10,000]` 之间
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return None
        need = {}    # 需要的字符个数
        window = {}  # 窗口包含的字符个数
        # 初始化各字符出现的个数
        for i in t:
            window[i] = 0
            need[i] += 1

        # 设置窗口左右边界
        left, right = 0, 0
        start = 0   # start 记录最小子串的起始位置
        valid = 0  # 记录要达到要求的各字符个数
        Len = len(s) + len(t)  # 记录最小窗口长度，用于更新

        # 开始滑动窗口
        while right < len(s):
            cin = s[right]
            right += 1

            # 若当前遍历字符是需要匹配的字符，则window中对应位置数+1
            if cin in need:
                window[cin] += 1
                # 若当前遍历字符cin，达到需要的数量，则valid+1
                if need[cin] == window[cin]:
                    valid += 1

            # 若当前所有子串的字符都被包含，那么此时窗口开始收缩
            while valid == len(need):
                # 更新窗口大小
                if right - left <= Len:
                    Len = right - left
                    start = left    # 并更新最小子串的起始位置
                # 窗口左边界收缩
                cout = s[left]
                left += 1

                # 判断当前左边移除的字符是否是需要的字符
                # 若是，则将window和need中对应位置统计个数更新
                if cout in need:
                    if window[cout] == need[cout]:
                        valid -= 1
                    window[cout] -= 1

        return '' if Len >= len(s) else s[start: start + Len]