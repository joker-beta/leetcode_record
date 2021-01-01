# -*- coding:utf-8 -*-
""" leetcode-295 数据流中的中位数
题目描述：
    如何得到一个数据流中的中位数？
        1，如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
        2，如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    我们使用 `Insert()` 方法读取数据流，使用 `GetMedian()` 方法获取当前读取数据的中位数。
"""

# [思路]：
#   我们不用把所有的数据进行排序，只需要保证数据左半边的数都小于右半边的数，
#   那么根据左半边的数的最大值和右半边的数的最小值，就可以得到中位数。
#       1，若输入的数据个数是奇数，比如1，2，3，4，5.我们可以把左边的1，2存入一个大顶堆中，
#          把右边的3，4，5存入一个小顶堆中。那么中位数就是小顶堆的 top()
#       2，若输入的数据个数是偶数，比如1，2，3，4.我们可以把左边的1，2存入大顶堆中，
#          把右边的3，4存入一个小顶堆中。那么中位数就是两个堆的 top() 的和再取平均。
#
# 整个过程我们需要维护两个地方：
#   两个堆的 size() 最大只能相差1，大顶堆的 top()必须小于等于小顶堆的 top()。
#-------------------------------------------------------------------------------------
# [实现方法]:
#   1，每插入一个数之前，先判断两个堆的 size() 是否相等。
#       a，若相等，先将这个数插入大顶堆，然后将大顶堆的 top()插入小顶堆。
#          这么做可以保证小顶堆的所有数永远大于等于大顶堆的 top()
#       b，若不相等，先将这个数插入小顶堆，然后将小顶堆的 top() 插入大顶堆。
#           这么做可以保证大顶堆的所有数永远小于等于小顶堆的 top()。
#   2，整个过程我们都动态做到了平衡两个堆的 size()，即保证它们的 size() 最大只相差了1。
#
# [转]：作者：superkakayong
#       链接：https://leetcode-cn.com/problems/find-median-from-data-stream/solution/zi-jie-ti-ku-295-kun-nan-shu-ju-liu-de-zhong-wei-s/

import heapq as hq
class Solution:
    def __init__(self):
        self.heap_less = []   # 模拟小顶堆
        self.heap_greater = []   # 模拟大顶堆
        self.count = 0   # 记录当前输入数据的个数

    def Insert(self, num):
        """将当前数据流压入大小堆中"""
        # 1，若当前输入数据个数为奇数
        if self.count & 1 == 0:
            hq.heappush(self.heap_greater, num)   # 先将当前数压入大顶堆中
            temp = hq.heappop(self.heap_greater)  # 再将(重新排序后的)大顶堆的，堆顶元素弹出
            hq.heappush(self.heap_less, -temp)    # 最后将弹出的元素按相反数压入小顶堆
        # 2，若当前输入数据个数为偶数
        else:
            hq.heappush(self.heap_less, -num)     # 先将当前元素按相反数压入小顶堆
            temp = -hq.heappop(self.heap_less)    # 再将(重新排序后的)小顶堆的，堆顶元素弹出
            hq.heappush(self.heap_greater, temp)  # 最后将弹出的元素压入大顶堆
        self.count += 1   # 记录当前压入堆的元素长度+1

    def GetMedian(self):
        """根据小顶堆和大顶堆的堆顶元素，计算数据流的中位数"""
        if self.count & 1 == 0:
            return (-self.heap_less[0] + self.heap_greater[0]) / 2.0
        return -self.heap_less[0]

