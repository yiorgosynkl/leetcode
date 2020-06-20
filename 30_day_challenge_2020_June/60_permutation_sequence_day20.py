################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200620
# Problem link      : https://leetcode.com/problems/permutation-sequence/
################################################################

# import functools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def par(n):
            vals = [1,1,2,6,24,120,720,5040,40320,362880]
            return vals[n]
            # if n == 0: return 1
            # return functools.reduce(lambda x,y: x*y, [i for i in range(1,n+1)])
        
        def perm(nums, k):
            if len(nums) == 1: return str(nums[0])
            times = par(len(nums) - 1)
            sel = k // times # selected digit
            return str(nums[sel]) + perm(nums[:sel] + nums[sel+1:], k % times)
        
        return perm([i for i in range(1, n+1)], k - 1)

# the division gives the place of the first num
# then i solve the same problem with 1 less number
