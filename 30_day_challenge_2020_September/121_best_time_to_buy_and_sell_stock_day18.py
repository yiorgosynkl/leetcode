################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200918
# Problem link      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
################################################################

class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices: return 0
    #     base, res = prices[0], 0
    #     for p in prices:
    #         base = min(base, p)
    #         res = max(res, p - base)
    #     return res
        
#     #  create the price differences matrix
#     #  find maximum subarray with Kadane's algorithm 
#     #  dp formula: dp[i] = max(dp[i-1], 0) + arr[i], base: dp[0] = arr[0]
#     def maxProfit(self, prices: List[int]) -> int:
#         changes = [e-b for e, b in zip(prices[1:], prices[:-1])]
#         dp = [0] # base, subarray ending at i
#         for c in changes:
#             dp.append(max(dp[-1], 0) + c)
#         return max(dp)
    
    def maxProfit(self, prices: List[int]) -> int:
        best, last = 0, 0
        for c in [e-b for e, b in zip(prices[1:], prices[:-1])]:
            last = max(last, 0) + c
            best = max(best, last)
        return best
    