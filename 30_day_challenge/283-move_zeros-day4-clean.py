class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        while slow < len(nums) and nums[slow] != 0:
            slow += 1
        for fast in range(slow + 1, len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                nums[fast] = 0
                slow += 1
        return nums