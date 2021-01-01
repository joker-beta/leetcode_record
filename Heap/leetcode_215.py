# -*- coding:utf-8 -*-
""" leetcode-215. 数组中的第K个最大元素
题目描述：
        在未排序的数组中找到第 `k` 个最大的元素。
        请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

例子：
	输入: [3,2,1,5,6,4] 和 k = 2
	输出: 5
"""

import heapq as hq
class Solution:
    def findkthLargest(self, arr, k):
        """查找最大的第 k 个元素（构建最小堆）"""
        if (arr == []) or (k <= 0):
            return None
        stack = []
        for num in arr:
            if len(stack) < k:
                hq.heappush(stack, num)
            else:
                if stack[0] < num:
                    hq.heapreplace(stack, num)
        ans = []
        while stack:
            ans.append(hq.heappop(stack))
        return ans[0]

arr = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findkthLargest(arr, k))



# [类比]：查找最小的第 k 个元素
class Solution_1:
    def findkthSmall(self, arr, k):
        """查找最小的第 k 个元素"""
        if (arr == []) or (k <= 0):
            return None
        stack = []
        for num in arr:
            if len(stack) < k:
                hq.heappush(stack, -num)
            else:
                if stack[0] < -num:
                    hq.heapreplace(stack, -num)
        ans = []
        while stack:
            ans.append(hq.heappop(stack))
        return -ans[0]

arr1 = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution_1().findkthSmall(arr, k))





# [类比-2]：将k个升序排序的列表合并成一个升序列表
import heapq as hq
class Solution_2:
    def mergeOfkList(self, arr):
        stack = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                hq.heappush(stack, arr[i][j])
        ans = []
        while stack:
            ans.append(hq.heappop(stack))
        return ans

n = 4
m = 6
arr = [[j + i*n for j in range(n)] for i in range(m)]
print(arr)
print(Solution_2().mergeOfkList(arr))