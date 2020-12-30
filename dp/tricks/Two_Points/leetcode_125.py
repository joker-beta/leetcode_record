# -*- coding:utf-8 -*-
""" leetcode-125. 验证回文串 (简单)
[题目]：
        给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

示例1:
    输入: "A man, a plan, a canal: Panama"
    输出: true

示例2:
    输入: "race a car"
    输出: false
"""

class Solution_1:
    """提取字符串判断"""
def isPalindrome(s: str) -> bool:
    # 设置双指针，判断arr是否构成回文
    left, right = 0, len(s) - 1
    while left <= right:
        while not (s[left].isalpha() or s[left].isdigit()):
            left += 1
        while not (s[right].isalpha() or s[right].isdigit()):
            right -= 1
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True



class Solution_2:
    """在原字符串上判断"""
    def isPalindrome(self, s: str) -> bool:
        if (s == "") or (len(s) == 1):
            return True
        # 设置双指针，判断arr是否构成回文
        left, right = 0, len(s)-1
        while left < right:
            while (left < right) and (not s[left].isalnum()):   # .isalnum() 判断当前字符是否是字母或者数字
                left += 1
            while (left < right) and (not s[right].isalnum()):
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True
