# -*- coding:utf-8 -*-
""" leetcode-844. 比较含退格的字符串
[题目]：
        给定 `S` 和 `T` 两个字符串，当它们分别被输入到空白的文本编辑器后，
        判断二者是否相等，并返回结果。 `#` 代表退格字符。
"""

from typing import List

# [思路]：对含有退格键的字符串逆序遍历
# 1，用变量count记录遍历过程中'#'的个数，
# 2, 2.1若当前遍历位置不是'#'并且count=0，则将当前字符添加到ans中保留
#    2.2若当前遍历位置不是'#'，但是cout!=0，说明当前位置需要删除，则不保留，直接跳过
# 3, 若当前遍历位置是'#'，记录count+1，然后往下移动
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def fun(s):
            """返回经过退格键处理后的字符串(逆序)"""
            count = 0
            ans = ""
            right = len(s)-1
            while right >= 0:
                if s[right] != '#':
                    if count == 0:
                        ans += s[right]
                    else:
                        count -= 1
                else:
                    count += 1
                right -= 1
            return ans
        return fun(S) == fun(T)