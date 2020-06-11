################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200611
# Problem link      : https://leetcode.com/problems/sort-colors/
################################################################

class Solution:
    # one pass, 3 pointers, best solution
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     lo, i, hi = 0, 0, len(nums)-1
    #     while i <= hi:
    #         if nums[i] == 2:
    #             nums[i], nums[hi] = nums[hi], nums[i]
    #             hi -= 1
    #         elif nums[i] == 0: 
    #             nums[i], nums[lo] = nums[lo], nums[i]
    #             lo += 1
    #             i += 1
    #         else:
    #             i += 1
    #     return nums

    # one pass, continuous change, cool solution
    def sortColors(self, nums: List[int]) -> None:
        i0, i1, i2 = 0, 0, 0
        for num in nums:
            print(num)
             # if num <= 2: # happens always
            nums[i2] = 2; i2 += 1
            if num <= 1: # happens for num 0 or 1
                nums[i1] = 1; i1 += 1
            if num == 0: # happens for num 0
                nums[i0] = 0; i0 += 1
            print(nums)
        return nums

    # one to two pass
    # def sortColors(self, nums: List[int]) -> None:
    #     lo, hi = 0, len(nums) - 1
    #     while lo < hi:
    #         if nums[hi] == 2: 
    #             hi -= 1
    #         elif nums[lo] == 2:
    #             nums[lo], nums[hi] = nums[hi], nums[lo]
    #         else:
    #             lo += 1
    #     lo = 0
    #     while lo < hi:
    #         if nums[hi] == 1: 
    #             hi -= 1
    #         elif nums[lo] == 1:
    #             nums[lo], nums[hi] = nums[hi], nums[lo]
    #         else:
    #             lo += 1        
    #     return nums

    # 2 passes
    # def sortColors(self, nums: List[int]) -> None:
    #     counts = [0, 0, 0]
    #     for num in nums:
    #         counts[num] += 1
    #     for i in range(0, counts[0]): nums[i] = 0
    #     for i in range(counts[0], sum(counts[0:2])): nums[i] = 1
    #     for i in range(sum(counts[0:2]), sum(counts)): nums[i] = 2
    #     return nums
            
        