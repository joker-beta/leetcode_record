# -*- coding:utf-8 -*-
""" leetcode-438. 找到字符串中所有字母异位词 (中等)
[题目]：
        给定一个字符串 `s` 和一个非空字符串 `p`，找到 `s` 中所有是 `p` 的字母异位词的子串，
        返回这些子串的起始索引。字符串只包含小写英文字母，并且字符串 `s` 和 `p` 的长度都不超过 `20100`。

说明：
* 字母异位词指字母相同，但排列不同的字符串。
* 不考虑答案输出的顺序。

示例 1:
	输入: s: "cbaebabacd" p: "abc"
	输出: [0, 6]
解释:
* 起始索引等于 `0` 的子串是 `"cba"`, 它是 `"abc"` 的字母异位词。
* 起始索引等于 `6` 的子串是 `"bac"`, 它是 `"abc"` 的字母异位词。


示例 2:
	输入: s: "abab" p: "ab"
	输出: [0, 1, 2]
解释:
* 起始索引等于 `0` 的子串是 `"ab"`, 它是 `"ab"` 的字母异位词。
* 起始索引等于 `1` 的子串是 `"ba"`, 它是 `"ab"` 的字母异位词。
* 起始索引等于 `2` 的子串是 `"ab"`, 它是 `"ab"` 的字母异位词。
"""
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not p:
            return []

        need = {}
        window = {}
        ans = []  # 记录各满足条件的子串的起始位置
        for i in p:
            window[i] = 0
            need[i] = p.count(i)

        left, right = 0, 0
        # 记录当前窗口中满足统计个数要求的字符个数
        # 例如，need中c字符个数为nc,若当前窗口中c字符个数达到nc个,那么valid+1
        valid = 0

        # 开始窗口移动
        while right < len(s):
            cin = s[right]
            right += 1

            if cin in need:
                window[cin] += 1
                if window[cin] == need[cin]:
                    valid += 1
            # 若当前窗口长度达到字符p长度
            while right - left == len(p):
                # 并且各字符个数达到要求，则记录字符串起始位置
                if valid == len(need):
                    ans.append(left)

                # 开始收缩窗口
                cout = s[left]
                left += 1
                if cout in need:
                    if window[cout] == need[cout]:
                        valid -= 1
                    window[cout] -= 1
        return ans


if __name__ == '__main__':
    while True:
        try:
            s = input()
            p = input()
            print(Solution().findAnagrams(s, p))
        except:
            break