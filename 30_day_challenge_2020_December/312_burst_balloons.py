################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201213
# Problem link      : https://leetcode.com/problems/burst-balloons/
################################################################

class Solution:
    # def maxCoins(self, nums: List[int]) -> int:
    #     nums = [1] + nums + [1]
    #     n = len(nums)
    #     dp = [[0 for _ in range(n)] for _ in range(n)]
    #     # initialise dp            
    #     for i in range(1, n-1):
    #         dp[i-1][i+1] = nums[i-1] * nums[i] * nums[i+1]
    #     for ln in range(3, n): # 3, ..., n - 1
    #         for lo, hi in zip(range(n-ln), range(ln, n)): # starting (lo) and ending (hi) ballons are alive
    #             best = 0
    #             for k in range(lo+1, hi): # lo+1, ..., hi-1
    #                 # print(lo, k, hi, dp[lo][k], dp[k][hi], nums[lo]*nums[k]*nums[hi])
    #                 best = max(best, dp[lo][k] + dp[k][hi] + nums[lo]*nums[k]*nums[hi])
    #             dp[lo][hi] = best # TODO: pythonise
    #     return dp[0][n-1]
            
    # dp logic, bottom-up, time: O(n^3), space: O(n^2)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # initialise dp            
        for i in range(1, n-1):
            dp[i-1][i+1] = nums[i-1] * nums[i] * nums[i+1]
        for gap in range(3, n): # 3, ..., n - 1
            for lo, hi in zip(range(n-gap), range(gap, n)): # starting (lo) and ending (hi) ballons are alive
                dp[lo][hi] = max(dp[lo][m] + dp[m][hi] + nums[lo]*nums[m]*nums[hi] for m in range(lo+1, hi)) # m is the middle last-bursted ballon
        return dp[0][n-1]

    # actually we want a to do dp
    # dp(i,j) has the maximum score achieved with ballons i and j alive (i<j) and then inbetween ballons bursted
    # we can find the dp(i,j) by trying different all inbetween ballons as last-bursted ballon
    #
    # we assume array [1, ..., 1], where leftmost and rightmost ballons cannot be bursted
    # initialise dp:
    # dp(i,i) = 0, where i = 1, ..., n
    # dp(i,i+1) = 0, where i = 1, ..., n-1
    # dp(i-1, i+1) = N[i-1]*N[i]*N[i+1], where i = 2, ..., n-1
    #
    # make dp:
    # dp(i, j) = max( dp(i,k) + dp(k,j) + N[i]*N[k]*N[j] ), k = {i+1, ..., j-1}, where 1 <= i < j <= n


    # # dp logic using dictinary
    # def maxCoins(self, nums: List[int]) -> int:
    #     nums = [1] + nums + [1]
    #     n = len(nums)
    #     dp = {}
    #     # initialise dp         
    #     for i in range(n-1):
    #         dp[(i, i+1)] = 0
    #     for i in range(1, n-1):
    #         dp[(i-1,i+1)] = nums[i-1] * nums[i] * nums[i+1]
    #     # bottom - up fill with dp formula
    #     for gap in range(3, n): # 3, ..., n - 1
    #         for lo, hi in zip(range(n-gap), range(gap, n)): # starting (lo) and ending (hi) ballons are alive
    #             dp[(lo,hi)] = max(dp[(lo,m)] + dp[(m,hi)] + nums[lo]*nums[m]*nums[hi] for m in range(lo+1, hi)) # m is the middle last-bursted ballon
    #     return dp[(0,n-1)]