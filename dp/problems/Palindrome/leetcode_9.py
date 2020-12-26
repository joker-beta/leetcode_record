# -*- coding:utf-8 -*-
""" leetcode-9 回文数
[题目]：
        判断一个整数是否是回文数。
        回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
	输入: 121			输出: true

示例 2:
	输入: -121		输出: false
	解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
	输入: 10			输出: false
	解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution_1:
    def isPalidrome(self, x: int) -> bool:
        ans = 1
        # x = abs(x)  根据(其他类似)题目的具体要求对负数情况做处理
        # 确定x是即为数
        while (x//ans >= 10):
            ans = ans * 10
        # 判断是否是回文
        while (x != 0):
            # 对比最高位和个位
            if (x//ans) != (x%10):
                return False
            # 更新x，同时去掉最高位和个位
            x = (x%ans) // 10
            # 更新位数统计，由于上一步每次去掉两个数位
            ans = ans // 100
        return True


class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        """两边往中间逼近"""
        # x = abs(x)   # 同样考虑x是负数的情况
        arr = list(str(x))   # 直接将数字转为字符串列表
        # 设置左右标记进行对称对比判断
        left, right = 0, len(arr)-1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True



class Solution_3:
    def isPalindrome(self, x: int) -> bool:
        """中心往外扩散"""
        # x = abs(x)   # 同样考虑x是负数的情况
        arr = list(str(x))
        mid = len(arr)//2   # 确定字符串中间的位置
        if len(arr)%2 == 0:
            left, right = mid-1, mid
        else:
            left, right = mid-1, mid+1
        while (left >= 0) and (right < len(arr)):
            if arr[left] != arr[right]:
                return False
            left -= 1
            right += 1
        return True


if __name__ == '__main__':
    x = None
    print(Solution_1().isPalidrome(x))
    print(Solution_2().isPalindrome(x))
    print(Solution_3().isPalindrome(x))


