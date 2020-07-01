################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200701
# Problem link      : https://leetcode.com/problems/arranging-coins/
################################################################

import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        s, plus = 0, 1
        while s <= n:
            s, plus = s + plus, plus + 1
        return plus - 2 # minus 1 for the last increment, minus 1 because we increased until out of bounds
    
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #int is simply to floor the floating point so we get the largest integer smaller than the expression
        return int((math.sqrt(8 * n + 1)-1)/2)
