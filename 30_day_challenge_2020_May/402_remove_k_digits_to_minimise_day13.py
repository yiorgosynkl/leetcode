################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200513
# Problem link      : https://leetcode.com/problems/remove-k-digits/
################################################################

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num.lstrip('0') or '0' # remove leftmost 0 and return '0' if emtpy string ''
        if k >= len(num):
            return "0"  
        for i in range(len(num) - 1):
            if num[i] > num[i+1]:
                return self.removeKdigits(num[:i] + num[i+1:], k - 1)
        return num[:-k]    
    
#     # sols from StefanPochmann
#     def removeKdigits(self, num, k):
#         out = []
#         for d in num:
#             while k and out and out[-1] > d:
#                 out.pop()
#                 k -= 1
#             out.append(d)
#         return ''.join(out[:-k or None]).lstrip('0') or '0'
    
#     # same logic with mine
#     def removeKdigits(self, num, k):
#         sub = re.compile('1[0]|2[01]|3[0-2]|4[0-3]|5[0-4]|6[0-5]|7[0-6]|8[0-7]|9[0-8]|.$').sub
#         for _ in range(k):
#             num = sub(lambda m: m.group()[1:], num, 1)
#         return num.lstrip('0') or '0'

        
#     def removeKdigits(self, num: str, k: int) -> str:
#         if k >= len(num):
#             return "0"
#         # greedily remove front numbers if there is a zero we can reach
#         zero_idx = num.find('0')
#         print(zero_idx)
#         if zero_idx >= 0 and zero_idx <= k:
#             return self.removeKdigits(num[(zero_idx + 1):], k - zero_idx)
#         #greadily remove big front numbers
#         idx = 0
#         while k:
#             if idx == len(num) - 1:
#                 break
#             if num[idx] <= num[idx+1]:
#                 idx += 1
#             else:
#                 num = num[:idx] + num[idx+1:]
#                 print(num)
#                 k -= 1
#                 idx = max(idx-1, 0)
#         # greadily remove last characters (the num digits are sotred to reach this loop)
#         if k > 0:
#             num = num[:-k]
#         return num
