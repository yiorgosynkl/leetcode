################################################################
# Project           : leetcode/two_sum
# Program name      : two_sum_brute_force.py.cpp
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200213
# Description       : find two indexes for nums of input list that sum to target input
################################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
