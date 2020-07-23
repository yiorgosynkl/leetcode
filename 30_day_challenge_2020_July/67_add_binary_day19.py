################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200719
# Problem link      : https://leetcode.com/problems/add-binary/
################################################################

class Solution:
    # pythonic 1-liner
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
        
    # # strings and nums
    # def addBinary(self, a: str, b: str) -> str:
    #     if len(b) > len(a):
    #         a, b = b, a
    #     b = (len(a) - len(b)) * '0' + b
    #     print(a)
    #     print(b)
    #     start = [(int(a[i]), int(b[i])) for i in range(len(a))]
    #     ans, c = [], 0 # carry
    #     for i, j in reversed(start):
    #         ssum = i+j+c
    #         ans.append(ssum % 2)
    #         c = ssum // 2
    #     if c == 1:
    #         ans.append(1)
    #     return ''.join([str(num) for num in reversed(ans)])
    
    # # logcical gates
    # def addBinary(self, a: str, b: str) -> str:
    #     a, b, c = int(a, 2), int(b, 2), 0 # carry
    #     s, p, r = 0, 1, 0 # sum, power of 2, result
    #     while a or b:
    #         b1, b2 = (a & 0b1), (b & 0b1) # two bits to add 
    #         s, c = b1 ^ b2 ^ c, (b1 & b2) | (b1 & c) | (b2 & c) # carry and sum
    #         r += p*s 
    #         a >>= 1; b >>= 1; p <<= 1
    #     r += p*c
    #     return bin(r)[2:]

    # # recursive
    # def addBinary(self, a, b):
    #     if len(a)==0: return b
    #     if len(b)==0: return a
    #     if a[-1] == '1' and b[-1] == '1':
    #         return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
    #     if a[-1] == '0' and b[-1] == '0':
    #         return self.addBinary(a[0:-1],b[0:-1])+'0'
    #     else:
    #         return self.addBinary(a[0:-1],b[0:-1])+'1'
