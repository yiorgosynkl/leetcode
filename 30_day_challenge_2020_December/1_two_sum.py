################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201208
# Problem link      : https://leetcode.com/problems/two-sum/
################################################################

# import numpy as np

class Solution:
    # O(n*logn)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     sort_index = np.argsort(nums)
    #     left = 0 # index
    #     right = len(nums) - 1 # index
    #     while(left < right):
    #         if (nums[sort_index[left]] + nums[sort_index[right]] == target):
    #             return [sort_index[left], sort_index[right]]
    #         elif (nums[sort_index[left]] + nums[sort_index[right]]  <= target):
    #             left += 1
    #         else:
    #             right -= 1
    #     return [0,0]
    
    # O(n) complexity using 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        his = {} # history of numbers
        for i, n in enumerate(nums):
            if target - n in his:
                return [i, his[target - n]]
            his[n] = i
        return [0,0] # never reaches this