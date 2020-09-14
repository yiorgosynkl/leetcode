################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200914
# Problem link      : https://leetcode.com/problems/house-robber/
################################################################

class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     dp = [0, 0]
    #     for m in nums:
    #         dp.append(max(m + dp[-2], dp[-1]))
    #     return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        l, r = 0, 0 # left and right from the rightmost cells of the dp array
        for m in nums:
            l, r = r, max(m + l, r)
        return r