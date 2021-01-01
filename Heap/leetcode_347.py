# -*- coding:utf-8 -*-
""" leetcode-347. 前 K 个高频元素
[题目]：给定一个非空的整数数组，返回其中出现频率前 `k` 高的元素。

示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

示例 2:
    输入: nums = [1], k = 1
    输出: [1]
"""

import heapq as hq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        ans = []
        for num, freq in res.items():    # res.items() 返回res中对应的键值对
            if len(ans) == k:
                if ans[0][0] < freq:
                    hq.heapreplace(ans, (freq, num))
            else:
                hq.heappush(ans, (freq, num))
        answer = []
        while ans:
            answer.append(hq.heappop(ans)[1])
        return answer


if __name__ == '__main__':
    while True:
        try:
            nums = list(map(int, input().split()))
            k = int(input())
            print(Solution().topKFrequent(nums, k))
        except:
            break
