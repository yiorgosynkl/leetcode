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