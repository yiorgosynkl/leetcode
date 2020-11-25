################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201125
# Problem link      : https://leetcode.com/problems/smallest-integer-divisible-by-k/
################################################################

class Solution:
    # def smallestRepunitDivByK(self, K: int) -> int:
    #     if K == 1: return 1
    #     ans, lg, found = 1, 1, set()
    #     while ans != 0:
    #         if ans in found: # loop starts
    #             return -1
    #         else:
    #             found.add(ans % K)
    #         ans = (10*ans + 1) % K
    #         lg = lg + 1
    #     return lg
    
    # def smallestRepunitDivByK(self, K: int) -> int:
    #     if K % 10 not in {1, 3, 7, 9}: return -1
    #     mod, mod_set = 0, set()
    #     for length in range(1, K + 1):
    #         mod = (10 * mod + 1) % K
    #         if mod == 0: return length
    #         if mod in mod_set: return -1
    #         mod_set.add(mod)
    #     return -1
    
    # @lee215 (O(1) space)
    def smallestRepunitDivByK(self, K):
        if K % 2 == 0 or K % 5 == 0: return -1
        r = 0
        for N in range(1, K + 1):
            r = (r * 10 + 1) % K
            if r == 0: return N

    # def smallestRepunitDivByK(self, K: int) -> int:
    #     rem = 0 # remainder
    #     for lg in range(1,K+1): # possible lengths (due to pigeonhole)
    #         rem = (rem * 10 + 1) % K
    #         if rem == 0: return lg
    #     return -1