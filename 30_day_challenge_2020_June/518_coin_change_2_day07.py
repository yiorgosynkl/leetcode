################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200607
# Problem link      : https://leetcode.com/problems/coin-change-2/
################################################################

# unbound knapsack
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n_coins = len(coins)
        prv, nxt = [1] + [0]*amount, [1] + [0]*amount # two lines of dp array 
        for coin in coins:
            for j in range(1, amount+1):
                nxt[j] = prv[j] if j < coin else nxt[j-coin] + prv[j]
            prv, nxt = nxt, prv
        return prv[amount]
    
#     def change(self, amount: int, coins: List[int]) -> int:
#         n_coins = len(coins)
#         dp = [[0 for _ in range(amount+1)] for _ in range(n_coins+1)]
#         dp[0][0] = 1
#         # 0 -> amount, 0 -> n_coins
#         for i in range(1, n_coins+1):
#             coin = coins[i-1]
#             for j in range(0, amount+1):
#                 dp[i][j] = dp[i-1][j] if j < coin else dp[i][j-coin] + dp[i-1][j]
#         return dp[n_coins][amount]

# why changing loop order doesn't work??
# To get the correct answer, the correct dp definition should be dp[i][j]="number of ways to get sum 'j' using 'first i' coins". 
# Now when we try to traverse the 2-d array row-wise by keeping only previous row array(to reduce space complexity), 
# we preserve the above dp definition as dp[j]="number of ways to get sum 'j' using 'previous /first i coins' " 
# but when we try to traverse the 2-d array column-wise by keeping only the previous column, the meaning of dp array 
# changes to dp[j]="number of ways to get sum 'j' using 'all' coins".
