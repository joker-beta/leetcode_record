# -*- coding:utf-8 -*-
""" leetcode-973. 最接近原点的 K 个点
[题目]：
        我们有一个由平面上的点组成的列表 `points`。需要从中找出 `K` 个距离原点 `(0, 0)` 最近的点。

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
"""

import heapq as hq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []  # 构建堆
        for i, [x, y] in enumerate(points):
            hq.heappush(h, (x**2 + y**2, i))
        ans = []
        for _ in range(k):
            ans.append(points[hq.heappop(h)[1]])
        return ans


if __name__ == '__main__':
    while True:
        try:
            n = int(input())  # 二维数组行数
            k = int(input())
            points = []
            for _ in range(n):
                points.append(list(map(int, input())))
            print(Solution().kClosest(points, k))
        except:
            break


