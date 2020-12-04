################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201204
# Problem link      : https://leetcode.com/problems/the-kth-factor-of-n/
################################################################

from math import sqrt, ceil
from collections import deque

class Solution:
    # def kthFactor(self, n: int, k: int) -> int:
    #     facs = [i for i in range(1, n+1) if n%i==0]
    #     return facs[k-1] if len(facs) >= k else -1
    
#     def kthFactor(self, n: int, k: int) -> int:
#         c = 0
#         for i in range(1, sqrt(n+1)):
#             c += int(n%i == 0)
#             if c == k: return i
#         return -1
        
    # # O(n^0.5)
    # # !!important, go until the square root, after that the divisors are in pairs with before
    # def kthFactor(self, n: int, k: int) -> int:
    #     facs = deque([])
    #     if sqrt(n).is_integer(): facs.append(int(sqrt(n)))
    #     for i in reversed(range(1, ceil(sqrt(n)))):
    #         if n%i == 0:
    #             facs.appendleft(i)
    #             facs.append(n//i)
    #     return facs[k-1] if len(facs) >= k else -1
    
#     # @DBabichev same idea, different approach
#     def kthFactor(self, n, k):
#         f1, f2 = [], []
#         for s in range(1, int(sqrt(n)) + 1 ):
#             if n % s == 0:
#                 f1 += [s]
#                 f2 += [n//s]
                
#         if f1[-1] == f2[-1]: f2.pop()
            
#         factors = f1 + f2[::-1]
#         return -1 if len(factors) < k else factors[k-1]

    # O(n^2), O(1) space (idea from @rock)
    def kthFactor(self, n, k):
        for i in range(1, ceil((n+1)**0.5)): # 1st pass, include root
            k -= int(n%i==0) # decrease if divisor found
            if k==0: return i
        for i in reversed(range(1, ceil(n**0.5))): # 2nd padd, exlude root
            k -= int(n%i==0)
            if k==0: return n//i
        return -1