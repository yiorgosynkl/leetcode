################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201106
# Problem link      : https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
################################################################

import math
import itertools
# import bisect

class Solution:
    # # brute force
    # def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    #     for i in itertools.count(start=1): # count from 1 to infinity
    #         if sum(math.ceil(n/i) for n in nums) <= threshold:
    #             return i

    # quick solution using binary search, O(nlogn)
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums) 
        while lo < hi:
            d = (lo + hi) // 2
            if sum(math.ceil(n/d) for n in nums) <= threshold:
                hi = d
            else:
                lo = d + 1
        return hi
    
    # # @StefanPochman crazy solution 
    # # binary search function on a lazy fake list (which computes its values on the fly)
    # def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    #     class List:
    #         def __getitem__(self, d):
    #             return sum(ceil(x / d) for x in nums) <= threshold
    #     return bisect_left(List(), True, 1, max(nums))

# other binary search problems: Divide Chocolate, Capacity To Ship Packages In N Days, Koko Eating Bananas, Minimize Max Distance to Gas Station, Split Array Largest Sum

