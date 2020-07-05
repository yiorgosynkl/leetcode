################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200705
# Problem link      : https://leetcode.com/problems/hamming-distance/
################################################################

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
    
    # def hammingDistance(self, x, y):
    #     """
    #     :type x: int
    #     :type y: int
    #     :rtype: int
    #     """
    #     x = x ^ y # xor
    #     ones = 0
    #     while x: # interesting and efficient way to count ones
    #         ones += 1
    #         x = x & (x - 1)
    #     return ones
    # x -1 actually takes the last 1 of x, turns it to zero and all the rightmost 0s to 1s  
    # x & (x-1) will remove the rightmost 1
    
    
    # def hammingDistance(self, x: int, y: int) -> int:
    #     def fix(x, w):
    #         res = bin(x)[2:] # string
    #         if w > len(res):
    #             res = str(int(x < 0))* (w-len(res)) + res # sign extend
    #         return res
    #     l = max(len(bin(x)), len(bin(y))) - 2 # length (number of bits)
    #     x, y = fix(x, l), fix(y, l)        
    #     print(x, y)
    #     return sum([int(x[i] != y[i]) for i in range(l)])
