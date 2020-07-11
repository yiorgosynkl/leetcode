################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200711
# Problem link      : https://leetcode.com/problems/subsets/
################################################################

from itertools import chain, combinations

class Solution:
    # backtracking approach
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1))
    
    # recursive approach
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = [[]]
    #     for num in nums:
    #         ans += [ll + [num] for ll in ans]
    #     return ans
        
    # binary representations approach
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans, n = [], len(nums)
    #     # 1st way
    #     nth_bit = 1 << n
    #     for i in range(2**n): # generate bitmask, from 0..00 to 1..11
    #         bitmask = bin(i | nth_bit)[3:] # left padding (remove 0b1 at the beginning)
    #         ans.append([num for idx, num in enumerate(nums) if bitmask[-1-idx] == '1'])
    #     # 2nd way
    #     # for i in range(2**n, 2**(n+1)):
    #     #     bitmask = bin(i)[3:][::-1] # left padding (remove 0b1 at the beginning)
    #     #     ans.append([num for idx, num in enumerate(nums) if bitmask[idx] == '1'])
    #     return ans
    
    # # backtracking approach
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     def backtrack(first = 0, curr = []):
    #         # if the combination is done
    #         if len(curr) == k:  
    #             output.append(curr[:])
    #         for i in range(first, n):
    #             # add nums[i] into the current combination
    #             curr.append(nums[i])
    #             # use next integers to complete the combination
    #             backtrack(i + 1, curr)
    #             # backtrack
    #             curr.pop()
    #     output = []
    #     n = len(nums)
    #     for k in range(n + 1):
    #         backtrack()
    #     return output