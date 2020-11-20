################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201120
# Problem link      : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
################################################################

class Solution:
    # def search(self, nums: List[int], target: int) -> bool:
    #     def sortBack(nums): # find pivot and return the original sorted array
    #         le, ri = 0, len(nums) - 1
    #         while le < ri and nums[le] == nums[ri]: # for extreme case where [2,2,2,0,2,2]
    #             le += 1
    #         while le < ri: # find index of smallest num, and rotate back to original array
    #             mid = (le + ri) // 2 
    #             if nums[mid] <= nums[ri]: # = is important because of duplicates (move right pointer as far left as possible)
    #                 ri = mid
    #             else: # nums[mid] > nums[le]
    #                 le = mid + 1
    #         return nums[le:] + nums[:le] 
    #     def binSearch(nums, target):
    #         lo, hi = 0, len(nums) - 1
    #         while lo <= hi:
    #             mid = (lo + hi) // 2
    #             if nums[mid] == target:
    #                 return True
    #             elif nums[mid] < target:
    #                 lo = mid + 1
    #             else:
    #                 hi = mid - 1
    #         return False
    #     return binSearch(sortBack(nums), target)
    
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False
        le, ri = 0, len(nums) - 1
        while le <= ri:
            mid = (le + ri) // 2
            if nums[mid] == target:
                return True                 
            if nums[le] < nums[mid] or (nums[le] == nums[mid] and nums[le] > nums[ri]): # first half (le<->mid part) is ordered
                if nums[le] <= target <= nums[mid]:
                    ri = mid - 1
                else:
                    le = mid + 1
            elif nums[mid] < nums[ri] or (nums[mid] == nums[ri] and nums[le] > nums[ri]): # second half (mid<->ri part) is ordered
                if nums[mid] <= target <= nums[ri]:
                    le = mid + 1    
                else:
                    ri = mid - 1
            else: # nums[mid] == nums[le] == nums[ri] # tricky part (cannot know which part is ordered)
                le += 1
                ri -= 1
        return False
