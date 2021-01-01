# -*- coding:utf-8 -*-
""" leetcode-633. 平方数之和
[题目]：
        给定一个非负整数 `c` ，你要判断是否存在两个整数 `a` 和 `b`，使得 `a^2 + b^2 = c` 。
"""

from typing import List
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(pow(c, 0.5))
        while left <= right:
            s = left**2 + right**2
            if s == c:
                return True
            elif s > c:
                right -= 1
            else:
                left += 1
        return False