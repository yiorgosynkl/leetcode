################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200515
# Problem link      : https://leetcode.com/problems/maximum-sum-circular-subarray/
################################################################

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(arr):
            ans, summ = float('-inf'), 0
            for num in arr:
                summ = max(summ, 0) + num
                ans = max(ans, summ)
            return ans
        pos_ans = kadane(A)
        neg_ans = sum(A) + kadane([-i for i in A])
        return max(pos_ans, neg_ans) if neg_ans != 0 else pos_ans
    
    # lee215
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
    #
    # case 1: [      |   max   |      ]  kadane's algorithm
    # case 2: [ max  |   min   |  max ]  kadane's algorithm to find the min subarray (maxiumum of opposite numbers)
    #                   , after that subtract from the sum of the whole array (and max subarray sum is left)
        
#     def maxSubarraySumCircular(self, A: List[int]) -> int:
#         def kadane(i):
#             arr = A[i:] + A[:i]
#             ans, summ = float('-inf'), 0
#             for num in arr:
#                 summ = max(summ, 0) + num
#                 ans = max(ans, summ)
#             return ans
        
#         ans = float('-inf')
#         for i in range(len(A)):
#             ans = max(ans, kadane(i))
#         return ans
