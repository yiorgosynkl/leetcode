################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210125
# Problem link      : https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
################################################################

class Solution:
    # def kLengthApart(self, nums: List[int], k: int) -> bool:
    #     prv = -k-1
    #     for i, n in enumerate(nums):
    #         if n == 1:
    #             if i - prv <= k:
    #                 return False
    #             prv = i
    #     return True
    
    # bit manipulation
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # convert binary array into int
        x = 0
        for num in nums:
            x = (x << 1) | num
        
        # base case
        if x == 0 or k == 0:
            return True
        
        # remove trailing zeros
        while x & 1 == 0:
            x = x >> 1
        
        while x != 1:
            # remove trailing 1-bit
            x = x >> 1
            
            # count trailing zeros
            count = 0
            while x & 1 == 0:
                x = x >> 1
                count += 1
                
            # number of zeros in-between 1-bits
            # should be greater than or equal to k
            if count < k:
                return False
        
        return True