################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210114
# Problem link      : https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
################################################################

import math 

class Solution:
    # dfs search, reaching time limit
    # def minOperations(self, nums: List[int], x: int) -> int:
    #     self.ans = math.inf
    #     def dfs(nums, x, count):
    #         if x == 0:
    #             self.ans = min(self.ans, count)
    #             return
    #         if not nums or x < 0:
    #             return
    #         dfs(nums[1:], x - nums[0], count + 1)
    #         dfs(nums[:-1], x - nums[-1], count + 1)
    #         return
    #     dfs(nums, x, 0)
    #     return self.ans if self.ans != math.inf else -1    
    
    # def minOperations(self, nums: List[int], x: int) -> int:
    #     target = sum(nums) - x
    #     if target < 0 : return -1
    #     lo, hi, ssum  = 0, -1, 0  # including lo, hi
    #     ans = math.inf
    #     while True:
    #         if ssum == target:
    #             ans = min(ans, len(nums) - (hi - lo + 1))
    #         if hi < lo or ssum <= target:
    #             hi += 1
    #             if hi == len(nums): break
    #             ssum += nums[hi]
    #         else:
    #             ssum -= nums[lo]
    #             lo += 1
    #     return ans if ans != math.inf else -1

    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0 : return -1
        lo, hi, ssum  = 0, 0, 0  # including lo, excluding hi, ssum = sum(nums[lo:hi])
        ans = math.inf
        while True:
            if ssum == target:
                ans = min(ans, len(nums) - (hi - lo))
            if hi <= lo or ssum <= target:
                if hi == len(nums): break
                ssum += nums[hi]
                hi += 1
            else:
                ssum -= nums[lo]
                lo += 1
        return ans if ans != math.inf else -1
    
    # # @rock, sliding window
    # def minOperations(self, nums: List[int], x: int) -> int:
    #     target, size, win_sum, lo, n = sum(nums) - x, -1, 0, -1, len(nums)
    #     for hi, num in enumerate(nums):
    #         win_sum += num
    #         while lo + 1 < n and win_sum > target:
    #             lo += 1
    #             win_sum -= nums[lo]
    #         if win_sum == target:
    #             size = max(size, hi - lo)
    #     return -1 if size < 0 else n - size

#     # calculate prefix sum and then find a matching suffix sum
#     def minOperations(self, nums: List[int], x: int) -> int:
#         mp = {0: 0}
#         prefix = 0
#         for i, num in enumerate(nums, 1): 
#             prefix += num
#             mp[prefix] = i 
            
#         ans = mp.get(x, inf)
#         for i, num in enumerate(reversed(nums), 1): 
#             x -= num
#             if x in mp and mp[x] + i <= len(nums): ans = min(ans, i + mp[x])
#         return ans if ans < inf else -1 
