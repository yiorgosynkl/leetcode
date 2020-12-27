################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201226
# Problem link      : https://leetcode.com/problems/decode-ways/
################################################################

class Solution:
#     def numDecodings(self, s: str) -> int:
#         if len(s) == 1:
#             return 0 if s[0] == '0' else 1
#         if s[0] == '0' or (s[1] == '0' and s[0] > '2'):
#             return 0
#         dp = [1, 1] # first element is written in one way
#         for i, c in zip(range(1, len(s)), s[1:]):
#             if c == '0':
#                 if s[i-1] == '1' or  s[i-1] == '2':
#                     dp.append(dp[-2])
#                 else:
#                     return 0
#             else:
#                 if s[i-1] == '1' or  (s[i-1] == '2' and c in ['1', '2', '3', '4', '5', '6']):
#                     dp.append(dp[-2] + dp[-1])
#                 else:
#                     dp.append(dp[-1])        
#         return dp[-1]
            
#     # @chrisjunlee
#     def numDecodings(s): 
#         if not s:
#             return 0

#         dp = [0 for _ in range(len(s) + 1)] 

#         # base case initialization
#         dp[0] = 1 
#         dp[1] = 0 if s[0] == "0" else 1   #(1)

#         for i in range(2, len(s) + 1): 
#             # One step jump (is the one digit number ok?)
#             if 0 < int(s[i-1:i]) <= 9:    #(2)
#                 dp[i] += dp[i - 1]
#             # Two step jump (is the two digit number ok?)
#             if 10 <= int(s[i-2:i]) <= 26: #(3)
#                 dp[i] += dp[i - 2]
#         return dp[-1]
    
#     # @StefanPochmann
#     def numDecodings(self, s):
#         return reduce(lambda(v,w,p),d:(w,(d>'0')*w+(9<int(p+d)<27)*v,d),s,(0,s>'',''))[1]*1
    
    
    def numDecodings(self, s):
        # w tells the number of ways, v tells the previous number of ways, d is the current digit, p is the previous digit
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w
