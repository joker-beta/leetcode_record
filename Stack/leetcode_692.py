# -*- coding:utf-8 -*-
""" leetcode-692. 前K个高频单词
[题目]：
        给一非空的单词列表，返回前 `k` 个出现次数最多的单词。
        返回的答案应该按单词出现频率由高到低排序。
        如果不同的单词有相同出现频率，按字母顺序排序。
"""
import heapq as hq
class Solution:
    def topkFrequent(self, words, k):
        stack = []
        for num in words:
            freq = words.count(num)
            if len(stack) < k:
                hq.heappush(stack, (freq, num))
            else:                       # 当前遍历元素有可能于之前元素重复
                if (stack[0][0] < freq) and ((freq, num) not in stack):
                    hq.heapreplace(stack, (freq, num))
        ans = []
        while stack:
            ans.append(hq.heappop(stack)[1])
        return ans


arr = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(Solution().topkFrequent(arr, k))
