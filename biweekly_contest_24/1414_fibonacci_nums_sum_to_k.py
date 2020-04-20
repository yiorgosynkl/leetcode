################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200418
# Problem link      : https://leetcode.com/contest/biweekly-contest-24/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
################################################################

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])
        count = 0
        for fib in reversed(fibs):
            if fib <= k:
                print(k)
                k -= fib 
                count += 1
        return count
