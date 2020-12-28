# -*- coding:utf-8 -*-
""" AcWing-154/leetcode-239 滑动窗口最值查找
[题目]：
        给定一个大小为 n ≤ 10^6 的数组。
        有一个大小为 k 的滑动窗口，它从数组的最左边移动到最右边。
        您只能在窗口中看到 k 个数字。每次滑动窗口向右移动一个位置。

[输入格式]
    输入包含两行。
    第一行包含两个整数n和k，分别代表数组长度和滑动窗口的长度。
    第二行有n个整数，代表数组的具体数值。
    同行数据之间用空格隔开。

[输出格式]
    输出包含两个。
    第一行输出，从左至右，每个位置滑动窗口中的最小值。
    第二行输出，从左至右，每个位置滑动窗口中的最大值。

[输入样例]：
        8 3
        1 3 -1 -3 5 3 6 7
[输出样例]：
        -1 -3 -3 -3 3 3
        3 3 5 5 6 7
"""


from typing import List
class Solution:
    """统计窗口中的最小值"""
    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if (nums == []) or (k < 0):
            return 0
        q = []  # 用来表示单调队列，维护的是数组nums中对应元素的下标
        head, tail = 0, -1   # 设置为队列的头尾位置
        ans = []   # 存放当前窗口的最大值
        for i in range(len(nums)):
            # 若队列头位置对应的数组nums下标位置不超过i-k(窗口大小为k)，说明头位置还可以往后移动
            if (head <= tail) and (q[head] <= i-k):
                head += 1
            # 每轮找出当前窗口最大值，所以队尾对应的nums中元素在队列中呈现单调下降趋势
            # 也就是说，如果当前遍历元素nums[i]大于队尾对应的nums中元素，那么一直将队尾下标往左移
            while (head <= tail) and (nums[q[tail]] >= nums[i]):
                tail -= 1
                q.pop()
            # 直到将当前元素nums[i]对应的下标加入队列后，能使得队列中各下标对应的nums元素呈现下降趋势
            q.append(i)
            tail += 1
            # 由于窗口大小为k，所以当遍历下标元素i大于k-1时，
            # 维护的单调下降队列，在每次更新完之后，队首位置对应的下标元素nums[q[head]]就是当前窗口最大值
            if (i >= k-1):
                ans.append(nums[q[head]])
        return ans


    """统计窗口中的最大值"""
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if (nums == []) or (k < 0):
            return 0
        q = []  # 用来表示单调队列，维护的是数组nums中对应元素的下标
        head, tail = 0, -1   # 设置为队列的头尾位置
        ans = []   # 存放当前窗口的最大值
        for i in range(len(nums)):
            # 若队列头位置对应的数组nums下标位置不超过i-k(窗口大小为k)，说明头位置还可以往后移动
            if (head <= tail) and (q[head] <= i-k):
                head += 1
            # 每轮找出当前窗口最大值，所以队尾对应的nums中元素在队列中呈现单调下降趋势
            # 也就是说，如果当前遍历元素nums[i]大于队尾对应的nums中元素，那么一直将队尾下标往左移
            while (head <= tail) and (nums[q[tail]] <= nums[i]):
                tail -= 1
                q.pop()
            # 直到将当前元素nums[i]对应的下标加入队列后，能使得队列中各下标对应的nums元素呈现下降趋势
            q.append(i)
            tail += 1
            # 由于窗口大小为k，所以当遍历下标元素i大于k-1时，
            # 维护的单调下降队列，在每次更新完之后，队首位置对应的下标元素nums[q[head]]就是当前窗口最大值
            if (i >= k-1):
                ans.append(nums[q[head]])
        return ans



# 利用 lambda 表达式设置 flag 来判断构建的队列是递增还是递减
from collections import deque
class Solution_1:
    def max_min(self, arr, func):
        q = deque()
        ans = []
        for i, v in enumerate(arr):
            if q and (q[0][0] <= i-k):
                q.popleft()   # 相当于上面代码中 head += 1
            while q and func(v, q[-1][1]):
                q.pop()   # 相当于上面代码 tail -= 1
            q.append((i, v))
            if (i >= k-1):
                ans.append(q[0][1])
        return ans







if __name__ == '__main__':
    while True:
        try:
            n, k = list(map(int, input().split()))
            arr = list(map(int, input().split()))
            #ans_min = Solution().minSlidingWindow(arr, k)
            #ans_max = Solution().maxSlidingWindow(arr, k)
            ans_min = Solution_1().max_min(arr, lambda x, y: x <= y)   # 单调递增队列
            ans_max = Solution_1().max_min(arr, lambda x, y: x >= y)   # 单调递减队列
            # 输出窗口最小值
            for i in range(len(ans_min)):
                if i != len(ans_min) - 1:
                    print(ans_min[i], end=' ')
                else:
                    print(ans_min[i])
            # 输出窗口最大值
            for i in range(len(ans_max)):
                if i != len(ans_max) - 1:
                    print(ans_max[i], end=' ')
                else:
                    print(ans_max[i])
        except:
            break
