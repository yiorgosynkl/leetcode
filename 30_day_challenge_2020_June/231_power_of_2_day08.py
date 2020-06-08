################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200608
# Problem link      : https://leetcode.com/problems/power-of-two/
################################################################

class Solution:
    def isPowerOfTwo(self, n: int) -> bool: # binary math trick O(1)
        return n > 0 and ((n & (n-1)) == 0)
    
    # def isPowerOfTwo(self, n: int) -> bool: # count bits with value 1 O(1)
    #     print(bin(n))
    #     return n > 0 and bin(n).count("1") == 1


    # def isPowerOfTwo(self, n: int) -> bool: # iterative O(logn)
    #     if n <= 0: return False
    #     while  n % 2 == 0: n = n // 2
    #     return n == 1
        