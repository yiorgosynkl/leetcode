################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200708
# Problem link      : https://leetcode.com/problems/3sum/
################################################################

from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for ta in range(0, len(nums) - 2):
            if ta > 0 and nums[ta] == nums[ta-1]: # already used target
                continue
            lo, hi = ta + 1, len(nums) - 1
            while lo < hi:
                if nums[ta] + nums[lo] + nums[hi] == 0:
                    if not ans or ans[-1] != [nums[ta],nums[lo],nums[hi]]: # don't add duplicate
                        ans.append([nums[ta],nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1
                elif nums[ta] + nums[lo] + nums[hi] > 0:
                    hi -= 1
                else: # nums[ta] + nums[lo] + nums[hi] < 0
                    lo += 1
        return ans

#     # slow simple
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         return [[i,j,k] for i,j,k in combinations(sorted(nums), 3) if i+j+k==0]

#     # slow simple
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans, seen = [], set()
#         for comb in combinations(sorted(nums), 3):
#             if  sum(comb)==0 and str(comb) not in seen:
#                 ans.append(list(comb))
#                 seen.add(str(comb))
#         return ans
