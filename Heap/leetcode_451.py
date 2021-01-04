# -*- coding:utf-8 -*-
""" leetcode-451. 根据字符出现频率排序
[题目]：
        给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

输入: "tree"
输出: "eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

输入: "cccaaa"
输出: "cccaaa"
解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
"""

import heapq as hq
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        :param s: str
        :return: str
        """
        res = {}
        for i in range(len(s)):
            if s[i] in res:
                res[s[i]] += 1
            else:
                res[s[i]] = 1
        h = []
        for num, freq in res.items():
            hq.heappush(h, (-freq, num))
        ans = ""
        while h:
            tmp = hq.heappop(h)
            for _ in range(-tmp[0]):
                ans += tmp[1]
        return ans


if __name__ == '__main__':
    while True:
        try:
            s = input()
            print(Solution().frequencySort(s))
        except:
            break


