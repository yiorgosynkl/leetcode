class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0 
        switch_idx = 0
        while True:
            while zero_idx < len(nums) and nums[zero_idx] != 0: 
                zero_idx += 1
            switch_idx = max(switch_idx, zero_idx + 1)
            while switch_idx < len(nums) and nums[switch_idx] == 0:
                switch_idx += 1
            if switch_idx >= len(nums): return nums
            nums[zero_idx] = nums[switch_idx]
            nums[switch_idx] = 0        
        