### 一些说明
处理最长子序列长度的计算问题，我们通过构造特定的数组来将其转化为动态规划问题。

一般地，对于一维LIS问题，若要计算序列arr中满足某个条件P的最长子序列长度，我们构造
```python
dp = [0 for _ in range(len(arr))]
```
其中dp[i]表示以arr[i]结尾，满足条件P的最长子序列长度，那么进一步根据条件P的具体要求来推到状态转移方程。
比如，条件P为递增(leetcode-300)或者连续递增(leetcode-674)，那么状态转移方程为
```python
# leetcode-300
for i in range(len(nums)):
    for j in range(i):
        # 递增条件判断
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)   # 状态转移
            
# leetcode-674
for i in range(1, len(nums)):
    # 原来数组可能存在重复元素，所以要求严格递增
    if nums[i-1] < nums[i]:
        dp[i] = max(dp[i], dp[i-1] + 1)   # 状态转移
```
