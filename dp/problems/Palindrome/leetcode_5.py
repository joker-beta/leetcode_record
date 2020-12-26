# -*- coding:utf-8 -*-
""" leetcode-5 最长回文子串
[题目]：
        给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度为 1000。

示例 1:
	输入: "babad"
	输出: "bab"
	注意: "aba" 也是一个有效答案。

示例 2:
	输入: "cbbd"
	输出: "bb"
"""


class Solution:
    def logesrPalindrome(self, arr: str) -> str:
        n = len(arr)
        # 若字符串长度小于2，直接输出字符串
        if n < 2:
            return arr
        # 若输入字符串非空，取首字符作为变量res的值，用于接下来的更新
        max_arr = arr[0]
        # 设置最大的回文子串长度
        max_len = 1
        for i in range(n):
            # 1，若当前字符串作为奇数长度时，返回相应的回文串和长度
            arr_odd, len_odd = self.fun(arr, n, i, i)
            # 2，若当前字符串作为偶数长度时，返回相应的回文串和长度
            arr_even, len_even = self.fun(arr, n, i, i+1)

            # 对比返回的奇偶回文串长度更新每一轮的最大回文串 tmp_max_arr
            if len_odd > len_even:
                tmp_max_arr = arr_odd
            else:
                tmp_max_arr = arr_even

            # 根据上面得到的每一轮的最长回文串tmp_max_arr更新要计算的最长回文串max_arr
            if len(tmp_max_arr) > max_len:
                max_arr = len(tmp_max_arr)
                max_arr = tmp_max_arr
        return max_arr

    def fun(self, arr, n, left, right):
        """通过中心扩散，找到当前最长的回文子串以及长度"""
        while (left >= 0) and (right < n) and (arr[left] == arr[right]):
            # 若当前子串arr[left],arr[left+1],...,arr[right]构成回文串
            # 那么继续往两边扩散
            left -= 1
            right += 1
        return arr[left+1:right], right-left+1


if __name__ == '__main__':
    #s = "babad"
    s = 'cbbd'
    print(Solution().logesrPalindrome(s))

