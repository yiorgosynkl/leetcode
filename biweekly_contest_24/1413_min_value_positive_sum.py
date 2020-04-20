################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200418
# Problem link      : https://leetcode.com/contest/biweekly-contest-24/problems/minimum-value-to-get-positive-step-by-step-sum/
################################################################

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minsum = 200
        ssum = 0
        for num in nums:
            ssum += num
            minsum = min(minsum, ssum)
        # print(minsum)
        return max(-minsum + 1, 1)
