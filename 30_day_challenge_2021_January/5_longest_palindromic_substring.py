################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210119
# Problem link      : https://leetcode.com/problems/longest-palindromic-substring/
################################################################

class Solution:
    # # dynamic programming
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) <= 1: return s
    #     dp = [[1]* len(s) for _ in range(len(s))] # initialise
    #     ans = s[0]
    #     for l in range(1, len(s)):
    #         for i in range(0, len(s)-l):
    #             dp[i][i+l] = int(s[i]==s[i+l]) & dp[i+1][i+l-1]
    #             if dp[i][i+l] == 1: ans = s[i:i+l+1]
    #     return ans
    
    # # dynamic programming refactored
    # def longestPalindrome(self, s: str) -> str:
    #     if not s: 
    #         return s
    #     dp = [[False]* len(s) for _ in range(len(s))] # initialise
    #     ans = s[0]
    #     for i in range(len(s)): 
    #         dp[i][i] = True
    #     for i in range(len(s)-1):
    #         if s[i]==s[i+1]:
    #             dp[i][i+1] = True
    #             ans = s[i:i+2]
    #     for l in range(2, len(s)):
    #         for i in range(0, len(s)-l):
    #             if s[i]==s[i+l] and dp[i+1][i+l-1]:
    #                 dp[i][i+l] = True
    #                 ans = s[i:i+l+1] 
    #     return ans
    
#     # almost 3 times faster, doing the same operations
#     def longestPalindrome(self, s):
#         ans = ''
#         max_len = 0
#         n = len(s)
#         DP = [[0] * n for _ in range(n)]
#         for i in range(n):
#             DP[i][i] = True
#             max_len = 1
#             ans = s[i]
#         for i in range(n-1):
#             if s[i] == s[i+1]:
#                 DP[i][i+1] = True
#                 ans = s[i:i+2]
#                 max_len = 2
#         for j in range(n):
#             for i in range(0, j-1):
#                 if s[i] == s[j] and DP[i+1][j-1]:
#                     DP[i][j] = True
#                     if max_len < j - i + 1:
#                         ans = s[i:j+1]
#                         max_len = j - i + 1
#         return ans

    
    # def longestPalindrome(self, s):
    #     def helper(s,l,r):
    #         while 0<=l and r < len(s) and s[l]==s[r]:
    #                 l-=1; r+=1
    #         return s[l+1:r]
    #     res = ""
    #     for i in range(len(s)):
    #         # # odd case, like "aba"
    #         # tmp = helper(s, i, i)
    #         # if len(tmp) > len(res):
    #         #     res = tmp
    #         # # even case, like "abba"
    #         # tmp = helper(s, i, i+1)
    #         # if len(tmp) > len(res):
    #         #     res = tmp
    #         res = max(helper(s,i,i), helper(s,i,i+1), res, key=len)
    #     return res
    
    # manacher's algorithm, time: O(n)
    # https://hackernoon.com/manachers-algorithm-explained-longest-palindromic-substring-22cb27a5e96f
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        s='#'+'#'.join(s)+'#'
        pos=maxright = 0
        RL=[0]*len(s)
        maxcenter=0
        for i in range(len(s)):
            if i<maxright:
                RL[i]=min(maxright-i,RL[pos*2-i])
            else:
                RL[i]=0
            while i-RL[i]-1>=0 and i+RL[i]+1<len(s) and s[i-RL[i]-1]==s[i+RL[i]+1]:
                RL[i]+=1
            if i+RL[i]>maxright:
                maxright=RL[i]+i
                pos=i
            if RL[i]>RL[maxcenter]:
                maxcenter=i
        return s[maxcenter-RL[maxcenter]:maxcenter+RL[maxcenter]+1].replace('#','')

