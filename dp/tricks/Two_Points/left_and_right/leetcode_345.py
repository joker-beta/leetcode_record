# -*- coding:utf-8 -*-
""" leetcode-345. 反转字符串中的元音字母
[题目]：
        编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
"""

from typing import List
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}   # 相比列表，集合查找更快些！！！
        s = list(s)   # 在python中str类型不能直接赋值互换！！
        left, right = 0, len(s)-1
        while left < right:
            if (s[left] in arr) and (s[right] in arr):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in arr:
                left += 1
            elif s[right] not in arr:
                right -= 1
        return ''.join(s)