# -*- coding:utf-8 -*-
""" leetcode-373. 查找和最小的K对数字
[题目]：
        给定两个以升序排列的整形数组 `nums1` 和 `nums2`, 以及一个整数 `k`。
        定义一对值 `(u,v)`，其中第一个元素来自 `nums1`，第二个元素来自 `nums2`。
        找到和最小的 `k` 对数字 `(u1,v1), (u2,v2) ... (uk,vk)`。

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""

import heapq as hq
from typing import List
class Solution_1:
    """时间复杂度为O(n*m)"""
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        if (n == 0) or (m == 0):
            return []
        res = []
        for i in range(n):
            for j in range(m):
                hq.heappush(res, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
        ans = []
        tmp = min(k, n*m)
        for _ in range(tmp):
            ans.append(hq.heappop(res)[1])
        return ans


class Solution_2:
    """时间复杂度为O(min(n, m))"""
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        queue = []
        def push(i, j):
            if (i < n) and (j < m):
                hq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        ans = []
        while queue and len(ans) < k:
            _, i, j = hq.heappop(queue)
            ans.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return ans




if __name__ == '__main__':
    while True:
        try:
            nums1 = list(map(int, input()))
            nums2 = list(map(int, input()))
            k = int(input())
            print(Solution_1().kSmallestPairs(nums1, nums2, k))
        except:
            break


