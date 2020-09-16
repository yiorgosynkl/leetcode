################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200916
# Problem link      : https://leetcode.com/problems/insert-interval/
################################################################

from itertools import combinations

class Solution:
    # def findMaximumXOR(self, nums: List[int]) -> int:
    #     return max([a^b for a,b in combinations(nums, 2)] or [0]) 
        
    # @ DBabichev
    def findMaximumXOR(self, nums):
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i # 0 than 10000000000000000000000000000000 than 11000000000000000000000000000000
            found = set([num & mask for num in nums])
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
        return ans
    # check if 2 numbers can XOR the leftmost bit 
    # we accordingly set the target answer (with 1 if 2 numbers exist, with 0 if 2 numbers don't exist) 

    # @StefanPochmann
    # def findMaximumXOR(self, nums):
    #     answer = 0
    #     for i in range(32)[::-1]:
    #         answer <<= 1
    #         prefixes = {num >> i for num in nums}
    #         answer += any(answer^1 ^ p in prefixes for p in prefixes)
    #     return answer