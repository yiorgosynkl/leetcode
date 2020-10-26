################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200922
# Problem link      : https://leetcode.com/problems/majority-element-ii/
################################################################

import random

class Solution:        
    # algorithmic
    # def majorityElement(self, nums: List[int]) -> List[int]:
        # from 0 to 2 elements
        # dic = {}
        # for n in nums:
        #     dic[n] = dic.get(n, 0) + 1
        # ans = []
        # for k, v in dic.items():
        #     if v > len(nums) // 3:
        #         ans.append(k)
        # return ans

    # # one liner
    # def majorityElement(self, nums: List[int]) -> List[int]:
    #     return [n for n in set(nums) if nums.count(n) > len(nums) // 3]
        
    # # may return wrong answer but much more quick
    # def majorityElement(self, nums: List[int]) -> int:
    #     TT = 50 # threshold
    #     if len(nums) > TT: nums = random.choices(nums, k=TT) # choose TT random numbers
    #     return [n for n in set(nums) if nums.count(n) > len(nums) // 3]
    
    
    # # probabilistic method, may return wrong answer
    # def majorityElement(self, nums: List[int]) -> int:
    #     if not nums: return []
    #     ans, TT = set(), 10
    #     for i in range(TT):
    #         num = nums[random.randrange(0, len(nums))]
    #         if nums.count(num) > len(nums) // 3:
    #             ans.add(num)
    #     return list(ans)
    
#     # Boyer-Moore Voting Algorithm
#     def majorityElement(self, nums):
#         if not nums:
#             return []
        
#         # 1st pass
#         count1, count2, candidate1, candidate2 = 0, 0, None, None
#         for n in nums:
#             if candidate1 == n:
#                 count1 += 1
#             elif candidate2 == n:
#                 count2 += 1
#             elif count1 == 0:
#                 candidate1 = n
#                 count1 += 1
#             elif count2 == 0:
#                 candidate2 = n
#                 count2 += 1
#             else:
#                 count1 -= 1
#                 count2 -= 1
        
#         # 2nd pass
#         result = []
#         for c in [candidate1, candidate2]:
#             if nums.count(c) > len(nums)//3:
#                 result.append(c)

#         return result

    # @StefanPochmann
    def majorityElement(self, nums):
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]
    