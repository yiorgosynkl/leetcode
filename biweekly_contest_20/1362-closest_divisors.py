################################################################
# Project           : leetcode
# Program name      : 1362-closest_divisors.py
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200224
# Description       : find the closest two integers in absolute difference whose product equals num + 1 or num + 2
################################################################

from math import sqrt, floor

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        # first loop
        num += 1
        best = num - 1 # first divisor is 1 other is the num
        alpha_best = 1
        bravo_best = num
        for alpha in range(2, floor(sqrt(num)) + 1):
            if (num % alpha == 0):
                bravo = num // alpha # bravo > alpha
                print('alpha, bravo : ', alpha, bravo)
                if best > bravo - alpha:
                    best = bravo - alpha
                    print(best)
                    alpha_best = alpha
                    bravo_best = bravo
        # second loop
        num += 1
        # best = min(best, num - 1) 
        for alpha in range(2, floor(sqrt(num)) + 1):
            if (num % alpha == 0):
                bravo = num // alpha # bravo > alpha
                if best > bravo - alpha:
                    best = bravo - alpha
                    alpha_best = alpha
                    bravo_best = bravo
        return [alpha_best, bravo_best]
        