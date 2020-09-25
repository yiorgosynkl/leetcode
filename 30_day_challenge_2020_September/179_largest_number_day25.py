################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200925
# Problem link      : https://leetcode.com/problems/largest-number/
################################################################

import functools 

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, nums):
        compare = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        # compare = lambda a, b: (b+a > a+b) - (b+a < a+b)
        _nums = list(map(str, nums))
        _nums
        _nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        return str(int(''.join(_nums)))    
        # return ans if ans[0] != '0' else '0'

#     # @StefanPochmann
#     def largestNumber(self, nums):
#         return str(int(''.join(sorted(map(str, nums), key=lambda s:s*9, reverse=True))))
