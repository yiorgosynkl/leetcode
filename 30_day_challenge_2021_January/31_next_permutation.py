################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210131
# Problem link      : https://leetcode.com/problems/next-permutation/
################################################################

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # starting from least significant digit find first dip moving to the left
        # that means find first num that has at least one bigger num to the right
        i = len(nums) - 1 
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1        
        # if i == 0, we have reached max possible value, 
        # nums are sorted in descending, so reverse and they will be in ascending order 
        if i == 0:
            nums[:] = nums[::-1] # or nums.reverse()
            return nums
        # i points to the last num before the fall
        # pivot is the number after the fall
        pivot = i - 1  
        # now we search for the smallest num that is bigger than pivot (right subarray is already sorted though!)
        while i < len(nums) - 1 and nums[pivot] < nums[i+1]:
            i += 1
        nums[pivot], nums[i] = nums[i], nums[pivot] # swap the numbers, the right subarray remains sorted
        nums[pivot+1:] = nums[pivot+1:][::-1]  # now reverse the right subarray (it becomes ascending order which is best possible)
    
    # @OldCodingFarmer
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
    