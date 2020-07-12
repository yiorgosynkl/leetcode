################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200712
# Problem link      : https://leetcode.com/problems/reverse-bits/
################################################################

class Solution:
    # pythonic 1-liner
    # def reverseBits(self, n: int) -> int:
    #     return int(bin(n | 1 << 32)[3:][::-1], 2)
        
    # arithmetic
    # def reverseBits(self, n: int) -> int:
    #     bits = []
    #     for i in range(32):
    #         bits.append(n % 2)
    #         n = n // 2
    #     ans, power = 0, 1
    #     for bit in reversed(bits):
    #         ans += power*bit
    #         power *= 2
    #     return ans
    
    # logic
    # def reverseBits(self, n: int) -> int:
    #     ans = 0
    #     for i in range(32):
    #         ans, n = (ans << 1) | (n & 1), n >> 1
    #     return ans        
        
# optimisation for cache hits
# import functools
# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#         ret, power = 0, 24
#         while n:
#             ret += self.reverseByte(n & 0xff) << power
#             n = n >> 8
#             power -= 8
#         return ret

#     # memoization with decorator
#     @functools.lru_cache(maxsize=256)
#     def reverseByte(self, byte):
#         return (byte * 0x0202020202 & 0x010884422010) % 1023

    # divide and conquer 
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
