################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201218
# Problem link      : https://leetcode.com/problems/increasing-triplet-subsequence/
################################################################

import math 

class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     mn, left = nums[0], [0]
    #     for n in nums[1:]:
    #         left.append(int(mn < n))
    #         mn = min(mn, n)
    #     mx, right = nums[-1], [0]
    #     for n in reversed(nums[:-1]):
    #         right.append(int(n < mx))
    #         mx = max(mx, n)
    #     return any(l + r == 2 for l, r in zip(left, right[::-1]))

    # def increasingTriplet(nums):
    #     first = second = float('inf')
    #     for n in nums:
    #         if n <= first:
    #             first = n
    #         elif n <= second:
    #             second = n
    #         else:
    #             return True
    #     return False
    
    # generalised for increasing sequences of length k, @StefannPochmann, complexity O(n*logk)
    def increasingTriplet(self, nums: List[int]) -> bool:
        k = 3
        inc = [math.inf] * (k - 1)  # each cell i holds the last value of an increasing subsequence of length i
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= k - 1:
                return True
            inc[i] = x
        return k == 0
