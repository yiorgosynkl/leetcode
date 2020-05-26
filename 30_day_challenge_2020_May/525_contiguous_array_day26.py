################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200526
# Problem link      : https://leetcode.com/problems/contiguous-array/
################################################################

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, ans = 0, 0
        times = { 0: -1 } # count, first_idx
        for idx, num in enumerate(nums):
            count += 1 if num else -1
            times[count] = times.get(count, idx)
            ans = max(ans, idx - times[count])
        return ans
    
    # def findMaxLength(self, nums: List[int]) -> int:
    #     x = { 0: -1 } # key: count -> val: first time index
    #     count = 0
    #     res = 0
    #     for i in range(0, len(nums)):
    #         count += 1 if nums[i] == 1 else -1
    #         if count not in x:
    #             x[count] = i
    #         else:
    #             res = max(res, i - x[count])
    #     return res

    # def findMaxLength(self, nums: List[int]) -> int:
    #     res = 0
    #     for i in range(1, len(nums)):
    #         times = [0,0] # zeros and ones
    #         for i in range(i, -1, -1):
    #             times[nums[i]] += 1
    #             if times[0] == times[1]:
    #                 res = max(res, times[0] * 2)
    #     return res
