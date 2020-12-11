################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201211
# Problem link      : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
################################################################

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, n, c = 0, None, 0 # i: index of pos for new value, n: the last num, c: times last num encountered
        for j in range(len(nums)):
            if n != nums[j]:
                n, c = nums[j], 0
            c += 1
            if c <= 2:
                nums[i] = nums[j]
                i += 1
        return i
        
#     # @StefanPochmann
#     def removeDuplicates(self, nums):
#         i = 0
#         for n in nums:
#             if i < 2 or n > nums[i-2]:
#                 nums[i] = n
#                 i += 1
#         return i

    def removeDuplicates(self, nums):
        slow, fast = 2, 2
        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
