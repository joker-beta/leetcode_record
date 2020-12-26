### 一些说明
处理最长子序列长度的计算问题，我们通过构造特定的数组来将其转化为动态规划问题。

#### 一维LIS问题
若要计算序列`arr`中满足某个条件`P`的最长子序列长度，我们构造
```python
dp = [0 for _ in range(len(arr))]
```
其中`dp[i]`表示以`arr[i]`结尾，满足条件`P`的最长子序列长度，那么进一步根据条件P的具体要求来推到状态转移方程。
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

#### 二维LIS问题
若要计算序列arr1和arr2中满足条件P的最长子序列长度，我们构造
```python
dp = [[0 for j in range(len(arr2))] for i in range(len(arr1))]
```
其中dp[i][j]表示以arr1[i]和arr2[j]结尾的满足P的最长公共子序列长度。
比如，计算最长公共子序列(leetcode-1143——不一定连续)或者子数组(leetcode-718——要求连续)，那么状态转移方程为
```python
# leetcode-1143
# 1，若相同，则同时对比前一个位置的情况
if arr1[i] == arr2[j]:
    dp[i][j] = dp[i-1][j-1] + 1
# 2，若当前遍历最后位置的字符不相同，则分别对比前一个位置的情况
else:
    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
 
 
# leetcode-718    
# 1，若两个数组当前遍历的最后一个元素相同，那么只需要判断之前的子数组
if arr1[i] == arr2[j]:
    dp[i][j] = dp[i-1][j-1] + 1
# 2，若不相同，说明以最后一个元素结尾的子数组长度为0
else:
    dp[i][j] = 0
```
