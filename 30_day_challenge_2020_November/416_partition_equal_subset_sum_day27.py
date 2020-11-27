################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201127
# Problem link      : https://leetcode.com/problems/partition-equal-subset-sum/
################################################################

class Solution:
    # # exponentially many subsets (2^n)
    # # instead use DP (save if sum is possible)
    # def canPartition(self, nums: List[int]) -> bool:
    #     s = sum(nums)
    #     if s % 2 != 0:
    #         return False
    #     s = s // 2
    #     prv = [1] + [0]*s       
    #     for num in nums:
    #         nxt = [1] + [0]*s  
    #         for i in range(s+1):
    #             nxt[i] = prv[i] if i - num < 0 else max(prv[i], prv[i - num])
    #         prv = nxt
    #     return prv[s]
    
    
    


    # # better version of DP
    # def canPartition(self, nums: List[int]) -> bool:
    #     fs, hs = sum(nums), sum(nums)//2 # half full sum
    #     if fs != 2*hs: return False
    #     dp = [True] + [False]*hs      
    #     for num in nums:
    #         for i in reversed(range(num, hs+1)): # reverse order because leftmost data affect rightmost
    #             dp[i] = (dp[i] or dp[i - num])
    #         if dp[hs]: return True
    #     return False
    
    
    

    # use binary instead of array for more efficiency (wow)
    # okay because we have infinate integers
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_val = 0 # even this is not needed, we could use the leftmost bit to determine max sum
        bits = 1  # holds the total number of sums achievable eg [2,4,5] -> sum 12 -> 13 bit number with ones for the achievable sums (0000000000001) 
        for num in nums:
            sum_val += num
            bits |= bits << num #

        return (not sum_val % 2 == 1) and (bits >> (sum_val // 2)) & 1 == 1
    
    
    

#     # memoization solution for target
#     def canFindSum(self, nums, target, ind, n, d):
#         if target in d: return d[target] 
#         if target == 0: d[target] = True
#         else:
#             d[target] = False
#             if target > 0:
#                 for i in range(ind, n):
#                     if self.canFindSum(nums, target - nums[i], i+1, n, d):
#                         d[target] = True
#                         break
#         return d[target]
    
#     def canPartition(self, nums):
#         s = sum(nums)
#         if s % 2 != 0: return False
#         return self.canFindSum(nums, s/2, 0, len(nums), {})
    
    
    


    # # brute force with tree structure
    # def canPartition(self, nums):
    #     s = sum(nums)
    #     if s % 2 == 1: return False
    #     def dfs(nums, t): # numbers and target sum
    #         if t == 0: return True
    #         if t < 0 or not nums: return False
    #         return dfs(nums[1:], t - nums[0]) or dfs(nums[1:], t) # try achieving result (with and without num, 2 choices)
    #     return dfs(nums, s//2)
    
    
    

    # # memoization with tree structure
    # def canPartition(self, nums):
    #     s, n = sum(nums), len(nums)
    #     if s % 2 == 1: return False
    #     memo = [[-1 for t in range(s//2 + 1)] for i in range(n)] # memory
    #     def dfs(i, t): # start index (nums[index:]) and target sum
    #         if memo[i][t] >= 0: 
    #             return memo[i][t]
    #         if nums[i] == t:
    #             memo[i][t] = 1
    #         elif t <= 0 or i == n-1:
    #             memo[i][t] = 0
    #         else:
    #             memo[i][t] = max(dfs(i+1, t - nums[i]), dfs(i+1, t))  # try achieving result (with and without num, 2 choices)
    #         return memo[i][t]
    #     return dfs(0, s//2) 




    # find all possible sums in super quick time
    # def canPartition(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     possible_sums = {0}
    #     for n in nums:
    #         possible_sums.update({(v + n) for v in possible_sums})
    #     return (sum(nums) / 2.)  in possible_sums  
