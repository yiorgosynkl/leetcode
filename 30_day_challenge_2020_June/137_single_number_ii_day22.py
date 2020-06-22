################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200622
# Problem link      : https://leetcode.com/problems/single-number-ii/
################################################################

class Solution:        
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        b1, b0 = 0, 0
        for num in nums:
            b0 = (b0 ^ num) & (~b1)
            b1 = (b1 ^ num) & (~b0)
        return b0
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums.sort()
    #     if n == 1 or nums[0] != nums[1] : return nums[0]
    #     if nums[n-2] != nums[n-1]: return nums[n-1]
    #     for i in range(1,n-1):
    #         if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
    #             return nums[i]
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     dic  = {}
    #     for num in nums:
    #         dic[num] = dic.get(num, 0) + 1
    #     for key, val in dic.items():
    #         if val == 1:
    #             return key
    #     return None