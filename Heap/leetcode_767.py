# -*- coding:utf-8 -*-
""" leetcode-767. 重构字符串
[题目]：
        给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
        若可行，输出任意可行的结果。若不可行，返回空字符串。

输入: S = "aab"
输出: "aba"

输入: S = "aaab"
输出: ""
"""

"""
[思路]：
    要保证相邻字符不同，我们需要贪心地对字符串进行重构，也就是在下一次重构的时候，把剩余字符串里最多的字符放到我们的重构字符串里。
    然后把本次重构去掉的字符再添加回去（放回的个数-1，因为我们已经用过一次了）。

1，如何理解剩余字符串？
    假设已知当前字符串里字母a出现的次数最多，那么这次我们肯定是把字母a添加到答案中，接下来我们把字符串里的所有字母a都去掉，这就是剩余字符串。
    在下一次重构的时候，假设这时字符串里字母b出现的次数最多，那么我们就把字母b添加到答案中，然后去掉字符串里所有的字母b，再把上一次去掉的a再放回去（放回的个数-1）。
    以此类推……
    如果暴力地对字符串进行删除和添加的操作，那么我们的时间复杂度会达到O(n^2)。
    我们可以借助最大堆这个数据结构把时间复杂度降低到O(nlog26)，也就是O(n)。最大堆保证了堆顶永远是出现次数最多的那个字母。

2，什么情况下无法完成重构？
    出现次数最多的那个字母大于字符串的长度的一半，向上取整。即长度为10的字符串，字母出现次数大于5；长度为11的字符串，字母出现的次数大于6。

作者：MiloMusiala
链接：https://leetcode-cn.com/problems/reorganize-string/solution/cjavapython-zui-da-dui-by-yanghk/
"""
import heapq as hq
class Solution:
    def reorganizeString(self, S: str) -> str:
        # 统计S字符串中各字符出现的次数
        res = {}
        for s in S:
            if s in res:
                res[s] += 1
            else:
                res[s] = 1
        # 若出现次数最多的字符数，比S长度的一半还多，说明没法构造出相邻元素不相同的字符串
        if max(res.values()) > (len(S) + 1)//2:
            return ""
        # 对出现次数排序，构建大顶堆
        p = []
        for item, count in res.items():
            hq.heappush(p, (-count, item))
        # 根据堆顶元素进行构建字符串
        ans = ""
        pre = (0, None)
        while p:
            i, s = hq.heappop(p)
            ans += s
            # 上一次弹出堆顶的元素，若还能取，则再次加入堆中
            if pre[0] < 0:
                hq.heappush(p, pre)
            # 保存当前弹出堆顶的元素s和相应的次数-1，由于堆中保存的是相反数，所以这里相当于+1
            pre = (i + 1, s)
        return ans



if __name__ == '__main__':
    while True:
        try:
            s = input()
            print(Solution().reorganizeString(s))
        except:
            break


