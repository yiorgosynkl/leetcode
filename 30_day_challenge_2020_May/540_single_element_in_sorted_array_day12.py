################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200512
# Problem link      : https://leetcode.com/problems/single-element-in-a-sorted-array/
################################################################

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def binary_search(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2 # mid is always and odd place
                # print(lo, mid, hi)
                if nums[mid] == nums[mid - 1]:
                    if mid % 2 == 1:
                        lo = mid + 1
                    else:
                        hi = mid - 2
                elif nums[mid] == nums[mid + 1]:
                    if mid % 2 == 1:
                        hi = mid - 1
                    else:
                        lo = mid + 2
                else:
                    return nums[mid]
            return nums[lo]
        return binary_search(0, len(nums) - 1)      
    
    # def singleNonDuplicate(self, nums):
    #     lo, hi = 0, len(nums) - 1
    #     while lo < hi:
    #         mid = (lo + hi) / 2
    #         if nums[mid] == nums[mid ^ 1]: # odd xor 1 = odd-1, even xor 1 = even+1
    #             lo = mid + 1
    #         else:
    #             hi = mid
    #     return nums[lo]
        
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     bag = set()
    #     for num in nums:
    #         if num in bag:
    #             bag.remove(num)
    #         else:
    #             bag.add(num)
    #     return bag.pop()
        