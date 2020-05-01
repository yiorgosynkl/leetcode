################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200423
# Problem link      : https://leetcode.com/problems/bitwise-and-of-numbers-range/
################################################################

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        out = [ch for ch in '{0:b}'.format((n))]
        power = 0
        while 2 ** power <= (n - m):
            out[-1-power] = '0'
            power += 1
        return m & int(''.join(out), 2)
    
#     the bitwise and of the range is keeping the common bits of m and n from left to right 
#     until the first bit that they are different, padding zeros for the rest.
    # def rangeBitwiseAnd(self, m, n):
    #     i = 0
    #     while m != n: # we remove rightmost digits until they are the same
    #         m >>= 1 # div 2
    #         n >>= 1
    #         i += 1
    #     return n << i # we fill with zeros
    
#     recursive style of the above idea
#     @staticmethod
#     def rangeBitwiseAnd(m: int, n: int) -> int:
#         return (Solution.rangeBitwiseAnd(m >> 1, n >> 1) << 1) if (m < n) else m
    
    

        