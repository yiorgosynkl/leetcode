################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200610
# Problem link      : https://leetcode.com/problems/search-insert-position/
################################################################

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_insert(nums, lo, hi, target):
            while lo < hi:
                mid = (lo + hi) // 2
                print(mid)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        return binary_insert(nums, 0, len(nums), target)
    
    # def searchInsert(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """       
    #     return len([x for x in nums if x<target])
