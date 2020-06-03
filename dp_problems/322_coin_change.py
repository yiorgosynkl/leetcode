################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200602
# Problem link      : https://leetcode.com/problems/coin-change/
################################################################

class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     n_coins = len(coins)
    #     dp = [[float("inf") for _ in range(amount+1)] for _ in range(n_coins+1)] # 0 -> amount, 0 -> n_coins
    #     dp[0][0] = 0
    #     for i in range(1, n_coins+1):
    #         coin = coins[i-1]
    #         for j in range(0, amount+1):
    #             dp[i][j] = dp[i-1][j] if j < coin else min(dp[i-1][j], 1 + dp[i][j-coin])
    #     return -1 if dp[n_coins][amount] == float("inf") else dp[n_coins][amount]
    
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        dp = [0] + amount*[MAX]
        for i in range(1, amount+1):
            dp[i] = min(dp[i - c] if i >= c else MAX for c in coins) + 1
        return -1 if dp[amount] == MAX else dp[amount]
