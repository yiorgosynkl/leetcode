class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        score = float('-inf') # the best score of subarray ending at num (Dynamic Programming)
        for num in nums:
            score = max(score + num, num)
            best = max(best, score)
        return best
        