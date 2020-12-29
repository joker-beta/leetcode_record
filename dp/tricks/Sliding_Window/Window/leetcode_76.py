# -*- coding:utf-8 -*-
""" leetcode-76. 最小覆盖子串 (困难)
[题目]：
        给你一个字符串 S、一个字符串 T`。
        请你设计一种算法，可以在 O(n)的时间复杂度内，从字符串 S 里面找出：
        包含 T 所有字符的最小子串。

示例：
	输入：S = "ADOBECODEBANC", T = "ABC"
	输出："BANC"

提示：
* 如果 S 中不存这样的子串，则返回空字符串 ""。
* 如果 S 中存在这样的子串，我们保证它是唯一的答案。
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
            need[i] = t.count(i)

        # 设置窗口左右边界
        left, right = 0, 0
        start = 0   # start 记录最小子串的起始位置
        # 记录当前窗口中满足统计个数要求的字符个数
        # 例如，need中c字符个数为nc,若当前窗口中c字符个数达到nc个,那么valid+1
        valid = 0
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

if __name__ == '__main__':
    while True:
        try:
            s = input()
            t = input()
            print(Solution().minWindow(s, t))
        except:
            break