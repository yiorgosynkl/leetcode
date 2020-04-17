import numpy as np

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_index = np.argsort(nums)
        left = 0 # index
        right = len(nums) - 1 # index
        while(left < right):
            if (nums[sort_index[left]] + nums[sort_index[right]] == target):
                return [sort_index[left], sort_index[right]]
            elif (nums[sort_index[left]] + nums[sort_index[right]]  <= target):
                left += 1
            else:
                right -= 1
        return [0,0]

# brute force
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     return [i, j]