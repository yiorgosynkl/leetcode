################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200716
# Problem link      : https://leetcode.com/problems/powx-n/
################################################################

class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     return x ** n
            
    # def myPow(self, x: float, n: int) -> float:
    #     ans = 1
    #     times = x if n > 0 else 1/x
    #     for i in range(abs(n)):
    #         ans *= times
    #     return ans
    
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     ans = x if n > 0 else 1/x
    #     mem = {1: ans} # power : value
    #     n, i = abs(n), 1
    #     while i < n:
    #         if 1 <= i <= n // 2:
    #             ans *= ans
    #             i = 2*i # i += i + 1
    #             mem[i] = ans
    #         else:
    #             idx = 1 << len(bin(n - i)[3:]) # first power of 2 leq than n - i
    #             ans *= mem[idx]
    #             i += idx
    #     return ans

    # def myPow(self, x, n):
    #     if not n:
    #         return 1
    #     if n < 0:
    #         return 1 / self.myPow(x, -n)
    #     if n % 2:
    #         return x * self.myPow(x, n-1) # example: 2^7 = 2 * 2^6
    #     return self.myPow(x*x, n/2) # example: 2^10 = 2^(2*5) = (2^2)^5 = 4^5
    
    # iterative approach 
    def myPow(self, x, n):
        if n < 0:
            x, n = 1/x, -n
        ans = 1
        while n > 0: # the 1s in n binary tell us which x^i to multiply to
            if n & 1: # last bit is 1
                ans *= x
            x *= x # increase the base so the loop goes x, x^2, x^4, ...
            n >>= 1
        return ans
