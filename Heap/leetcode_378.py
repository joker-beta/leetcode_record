# -*- coding:utf-8 -*-
""" leetcode-378. 有序矩阵中第K小的元素
[题目]：
        给定一个 `n x n` 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 `k` 小的元素。
        请注意，它是排序后的第 `k` 小元素，而不是第 `k` 个不同的元素。

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
"""
from typing import List
import heapq as hq
class Solution_1:
    """复杂度O(n*m)"""
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(ans) == k:
                    if ans[0] < -matrix[i][j]:
                        hq.heapreplace(ans, -matrix[i][j])
                    else:
                        hq.heappush(ans, -matrix[i][j])
        return -hq.heappop(ans)


class Solution_2:
    """二分查找"""
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            """统计数组中有多少个数比mid少"""
            i, j = n-1, 0
            num = 0
            while (i >= 0) and (j < n):
                if matrix[i][j] <= mid:
                    num += (i + 1)
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left)//2
            if check(mid):
                mid = right   # 若比当前遍历的数，小的数的个数>=k，说明第k小的数要比mid小
            else:
                mid = left + 1  # 否则，要比mid大
        return left



if __name__ == '__main__':
    while True:
        try:
            [n, m] = list(map(int, input()))
            matrix = [[i+j for j in range(m)] for i in range(n)]
            k = int(input())
            print(Solution_1.kthSmallest(matrix, k))
        except:
            break


