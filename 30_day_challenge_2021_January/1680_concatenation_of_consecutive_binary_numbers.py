################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210127
# Problem link      : https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
################################################################

class Solution:
    # def concatenatedBinary(self, n: int) -> int:
    #     s = ''.join([bin(i)[2:] for i in range(1, n+1)])
    #     return int(s, 2) % (10**9 + 7)
        
    
#     # time limit exceeded
#     def concatenatedBinary(self, n: int) -> int:
#         MODNUM = 10**9 + 7
#         total = 0
#         shift = 1   # number of digits we should shift
#         cnt = 2**(shift-1)
#         for i in range(1, n+1):
#             total = (total << shift) | i
#             cnt -= 1
#             if cnt == 0:
#                 shift += 1
#                 cnt = 2**(shift-1)
#         return total % MODNUM

    def concatenatedBinary(self, n: int) -> int:
        MODNUM = 10**9 + 7
        total = 0
        shift = 1   # number of digits we should shift
        cnt = 2**(shift-1)
        for i in range(1, n+1):
            total = ((total << shift) | i) % MODNUM     # valid operation
            cnt -= 1
            if cnt == 0:
                shift += 1
                cnt = 2**(shift-1)
        return total

#     # recursive approach, time: O(n)
#     def concatenatedBinary(self, n: int) -> int:
#         if n < 1: return -1
#         if n == 1: return 1
#         return (self.concatenatedBinary(n-1) << len(bin(n)[2:]) | n) % (10**9 + 7)

#     # mathematical approach, time: O(n)
#     # f(n) = f(n-1) * 2^floor(logn) + n
#     def concatenatedBinary(self, n: int) -> int:
#         MODNUM = 10**9 + 7
#         total = 0
#         rndlog = 1   # logarithm of base two rounded down (integer)
#         cnt = 2**(rndlog-1)
#         for i in range(1, n+1):
#             total = (total * 2**rndlog + i) % MODNUM     # valid operation
#             cnt -= 1
#             if cnt == 0:
#                 rndlog += 1
#                 cnt = 2**(rndlog-1)
#         return total
    
#     # @alanlzl, time: O(n)
#     def concatenatedBinary(self, n: int) -> int:
#         ans, l, MOD = 0, 0, 10 ** 9 + 7
#         for x in range(1, n + 1):
#             # x & -x comes from Fenwick Tree,
#             # checks if x is something like 100...0
#             if x & (-x) == x: l += 1
#             ans = (ans * (1 << l) + x) % MOD
#         return ans 

#     # @DBabichev O(log^2 n)
#     def concatenatedBinary(self, n):
#         def bin_pow(num): return [1<<i for i, b in enumerate(bin(num)[:1:-1]) if b == "1"]
#         ans, MOD, q = 0, 10**9 + 7, len(bin(n)) - 3

#         B = bin_pow((1<<q) - 1) + bin_pow(n - (1<<q) + 1)[::-1]
#         C = list(range(1, q+1)) + [q+1]*(len(B) - q)
#         D = list(accumulate(i*j for i,j in zip(B[::-1], C[::-1])))[::-1][1:] + [0]
        
#         for a, b, c, d in zip(accumulate(B), B, C, D):
#             t1 = pow(2, b*c, MOD) - 1
#             t2 = pow(pow(2, c, MOD)-1, MOD - 2, MOD)
#             ans += t2*((a-b+1+t2)*t1-b)*pow(2, d, MOD)

#         return ans % MOD

