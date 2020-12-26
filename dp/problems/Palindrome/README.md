### 一些说明
关于回文数或者回文串的相关问题，主要涉及回文子串的长度计算，子串输出，最长子串个数统计等。
若输入的不是字符串`arr`，比如输入数字，我们可以直接将其转为字符串处理，当然也可以直接处理(`leetcode-9`)。

不管怎么说，这些问题中最基本的就是判断一个字符串是否是回文，主要是两种策略，一个是从字符串两端往中间走，一个是从字符串中间往两端走(中心扩散)。
我们将核心的代码贴出来。
```python
# [方法一]：从两边往中间走
left, right = 0, len(arr)-1
while left < right:
    if arr[left] != arr[right]:
        return False
    left += 1
    right -= 1
return True


# [方法二]：中心扩散
mid = len(arr)//2   # 确定字符串中间的位置
# 下面的4行是对于输入字符串长度奇偶的判断，用来确定子串的中心位置
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
```
当然，大部分问题不会仅仅要我们判断子串是否是回文，而是将该判断作为原问题中的一个子问题处理，这时候我们可能需要在主函数中调用中心扩散判断函数，这里以`leetcode-647为例，看看调用代码。
```python
class Solution:
    """记录回文子串的个数"""
    def countSubstrings(self, s: str) -> int:
        # 这里我们不考虑其他特殊情况，只看看调用部分代码
        ......
        # 统计回文串的个数
        self.ans = 0
        # 对每个位置依次利用中心扩散法统计回文串的个数
        for i in range(len(s)):
            self.fun(s, i, i)    # 统计长度为奇数的回文串，回文串中心为s[i]
            self.fun(s, i, i+1)  # 统计长度为偶数的回文串，回文串中心为空字符
        return self.ans

    def fun(self, s, left, right):
        """(中心扩散)统计字符s[left],...,s[right]内回文串个数"""
        while (left >= 0 and right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1
            self.ans += 1
```
