# -*- coding:utf-8 -*-
""" leetcode-647 回文子串
[题目]：
        给定一个字符串，你的任务是计算这个字符串中**有多少个回文子串**。
        具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
	输入："abc"
	输出：3
	解释：三个回文子串: "a", "b", "c"

示例 2：
	输入："aaa"
	输出：6
	解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


# [思路一]：构造二维dp数组
class Solution_1:
    def countSubstrings(self, s: str) -> int:
        if s == '':
            return 1
        n = len(s)
        # dp[i][j] 表示s[i],s[i+1],...,s[j]范围内是否构成回文
        dp = [[0 for j in range(n)] for i in range(n)]
        # 统计回文个数
        ans = 0

        for i in range(n):
            for j in range(i+1):
                # 若当前遍历的字符s[i]==s[j]，也就是当前字符串首尾相同，那么需要判断内部字符串
                # 1，若i-j<2，即i==j（内部为空字符），或者i=j+1（内部只有一个字符）
                # 2，若dp[i-1][j+1]==1，说明内部构成回文
                if (s[i] == s[j]) and (i-j<2 or dp[i-1][j+1]==1):
                    dp[i][j] = 1
                    ans += 1
        return ans



# [思路二]：中心扩散法
# 1，构造二维数组使得空间复杂度比较大，尝试降低空间复杂度。
# 2，设置左右标记，从字符串中间往两边遍历判断。
class Solution_2:
    def countSubstrings(self, s: str) -> int:
        if s == '':
            return 1
        # 统计回文串的个数
        self.ans = 0
        # 对每个位置依次利用中心扩散法统计回文串的个数
        for i in range(len(s)):
            self.fun(s, i, i)    # 统计长度为奇数的回文串，回文串中心为s[i]
            self.fun(s, i, i+1)  # 统计长度为偶数的回文串，回文串中心为空字符
        return self.ans

    def fun(self, s, left, right):
        """统计字符s[left],...,s[right]内回文串个数"""
        while (left >= 0 and right < len(s)) and (s[left] == s[right]):
            # 中心扩散，left，right往两边走
            left -= 1
            right += 1
            self.ans += 1



if __name__ == '__main__':
    s = 'dafasdsafe'
    print(Solution_1().countSubstrings(s))
    print(Solution_2().countSubstrings(s))