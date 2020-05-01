class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum[prices[i+1] - prices[i] for i in range(0, len(prices) - 1)]
        