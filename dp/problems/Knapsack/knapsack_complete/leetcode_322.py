# -*- coding:utf-8 -*-
""" leetcode-322. 零钱兑换（最少硬币个数）
[题目]：
        给定不同面额的硬币coins和一个总金额amount。
        编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
        如果没有任何一种硬币组合能组成总金额，返回-1。你可以认为每种硬币的数量是无限的。

示例 1：
	输入：coins = [1, 2, 5], amount = 11
	输出：3
	解释：11 = 5 + 5 + 1

示例 2：
	输入：coins = [2], amount = 3
	输出：-1

示例 3：
	输入：coins = [1], amount = 0
	输出：0

示例 4：
	输入：coins = [1], amount = 1
	输出：1

示例 5：
	输入：coins = [1], amount = 2
	输出：2

提示：
* `1 <= coins.length <= 12`
* `1 <= coins[i] <= 231 - 1`
* `0 <= amount <= 231 - 1`
"""

# [思路]：
# 每个硬币可以选择无数次。计算可以凑成总金额所需的最少的硬币个数。
# 若没有任何一种硬币组合能组成总金额，返回-1.
#
# dp[i][j]为考虑前i种硬币，凑成金额为j的最少数目。
# 考虑第i种硬币，我们可以不拿，或者拿1,...,k个，直到把金额拿爆
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-c]+1, dp[i-1][j-2*c]+2,...,dp[i-1][j-k*c]+k)
# 由于其中包含了大量的冗余计算，为了化简，我们考虑
# dp[i][j-c] = min(dp[i-1][j-c], dp[i-1][j-2*c]+1,...,dp[i-1][j-k*c]+k-1)
# 则，dp[i][j] = min(dp[i-1][j], dp[i][j-c]+1)
# 再进一步空间压缩，注意到dp[i][j]只和上一层一个状态dp[i-1][j]和这一层的一个状态dp[i][j-c]有关。
# 可以将状态优化为一维数组，dp[j] = min(dp[j], dp[j-c]+1)

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins == []:
            return -1
        if amount == 0:
            return 0
        # dp[i]表示凑成金额i需要的最少硬币数
        dp = [float('INF') for _ in range(amount + 1)]
        # dp[0]=0表示金额为0时，最小硬币凑法为0，其余要初始化为inf
        # 因为这题要求的是恰好金额为m时的最小硬币数，所以有些状态可能达不到。
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                # 若当前遍历金额i为coins中的金额数coin相同，那么只需要一枚该硬币
                # 这也是需要设定dp[0]=0的原因
                dp[i] = min(dp[i], dp[i-coin] + 1)
        # 若dp[amount]=Inf，说明之前遍历的金额数i，都不能用coins中的硬币做组合表示
        if dp[-1] == float('INF'):
            return -1
        else:
            return dp[-1]
