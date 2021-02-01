################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210201
# Problem link      : https://leetcode.com/problems/number-of-1-bits/
################################################################

class Solution:
    # @yiorgosynkl
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n > 0:    # loop 
            out += n & 1
            n >>= 1
        return out

    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:        # loop as many times as the 1s
            n &= n - 1  # remove the least significant 1
            c += 1
        return c
    
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
