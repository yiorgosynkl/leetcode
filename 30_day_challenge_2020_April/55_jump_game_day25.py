################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200425
# Problem link      : https://leetcode.com/problems/jump-game/
################################################################

# from functools import reduce

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        upper = 0
        for idx, val in enumerate(nums):
            upper = max(upper, idx + val)
            if len(nums) - 1 <= upper: # if upper can reach the last number
                return True
            if upper == i:
                return False
    
    # stefan pochmann
    # def canJump(self, nums):
    #     m = 0
    #     for i, n in enumerate(nums):
    #         if i > m:
    #             return False
    #         m = max(m, i+n)
    #     return True

    # def canJump(self, nums):
    #     return reduce(lambda m, (i, n): max(m, i+n) * (i <= m), enumerate(nums, 1), 1) > 0

    # def canJump(self, nums):
    #     goal = len(nums) - 1
    #     for i in range(len(nums))[::-1]:
    #         if i + nums[i] >= goal:
    #             goal = i
    #     return not goal
            
        