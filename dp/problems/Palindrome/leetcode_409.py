# -*- coding:utf-8 -*-
""" leetcode-409 最长回文串

[题目]：
        给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
        在构造过程中，请注意区分大小写。比如 `"Aa"` 不能当做一个回文字符串。
        注意： 假设字符串的长度不会超过 `1010`。

示例 1:
	输入: "abccccdd"		输出: 7
	解释:  我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 统计回文字符长度
        count = 0
        total = {}
        for num in s:
            if num in total:
                total[num] += 1
            else:
                total[num] = 1
        for i in total.values():
            # 若当前遍历字符str_i出现的次数i大于1。
            # 那么可以将i平分，分别将对应的字符放在构造的回文串两侧
            count += (i//2) * 2
            # 同时，若此时的字符str_i出现的是奇数次，那么进一步可以选取一个作为构造的回文串的中心
            if (count%2 == 0) and (i%2 == 1):
                count += 1
        return count


if __name__ == '__main__':
    s = "abccccdd"
    print(Solution().longestPalindrome(s))



"""
[注]：另外，这里我们还可以调用内置函数 Counter 来完成统计字符个数相同的操作

total = {}
for num in s:
    if num in total:
        total[num] += 1
    else:
        total[num] = 1
        
即，先导入内置模块 collections，以及函数 Counter，
其中 Counter() 用于统计字符串中各字符出现的次数，返回字典
from collections import Counter
total = Counter(s)
"""
