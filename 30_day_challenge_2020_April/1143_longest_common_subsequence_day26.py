################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200426
# Problem link      : https://leetcode.com/problems/longest-common-subsequence/
################################################################

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
    
        # To use less space, put the shortest string first
        # if len(text1) > len(text2):
        #     text1, text2 = text2, text1
        # prv = [0] * (len(text1) + 1)
        # nxt = [0] * (len(text1) + 1)
        # for i2 in range(len(text2)):
        #     for i1 in range(len(text1)):
        #         nxt[i1 + 1] = max(nxt[i1], prv[i1 + 1], prv[i1] + (text1[i1] == text2[i2]))
        #     prv, nxt = nxt, prv
        # return prv[-1]
        
#         !!! pass by object reference !!! (watch out)
#         DP = [[0]* len(text1)]* len(text2)
#         def get(i,j):
#             return 0 if (i < 0 or j < 0) else DP[i][j] 
#         for i in range(len(text2)):
#             for j in range(len(text1)):
#                 if text2[i] == text1[j]:
#                     DP[i][j] = (1 + get(i - 1, j - 1))
#                 else:
#                     DP[i][j] = max(get(i-1, j), get(i, j-1))
#         return DP[len(text2) - 1][len(text1) - 1]