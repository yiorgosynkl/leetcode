################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200509
# Problem link      : https://leetcode.com/problems/valid-perfect-square/
################################################################

from math import sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def binary_search(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if mid**2 == num:
                    return True
                elif mid**2 < num:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False
        return binary_search(1, num)
        
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num).is_integer()
