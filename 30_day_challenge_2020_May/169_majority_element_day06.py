################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200506
# Problem link      : https://leetcode.com/problems/majority-element/
################################################################

# import math
# import random

class Solution:
    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
                
    
    # one liner
    # def majorityElement(self, nums: List[int]) -> int:
    #     return sorted(num)[len(num)/2]
    
    # probabilistic always right O(inf)
    # def majorityElement(self, nums: List[int]) -> int:
    #     while True:
    #         idx = random.randrange(0, len(nums))
    #         num = nums[idx]
    #         if nums.count(num) > len(nums)//2:
    #             return num
    
    # may return wrong answer, especially for small arrays
    # def majorityElement(self, nums: List[int]) -> int:
    #     d = {}
    #     times = math.ceil(len(nums) * 0.05) # 5% of nums is used for check
    #     for _ in range (times):
    #         idx = random.randint(0, len(nums) - 1)
    #         print(idx, len(nums))
    #         num = nums[idx]
    #         d[num] = d.get(num, 0) + 1
    #     return max(d.items(), key=operator.itemgetter(1))[0]

    # O(n) algorithmic
    # def majorityElement(self, nums: List[int]) -> int:
    #     d = {}
    #     for num in nums:
    #         d[num] = d.get(num, 0) + 1
    #     return max(d.items(), key=operator.itemgetter(1))[0]

        