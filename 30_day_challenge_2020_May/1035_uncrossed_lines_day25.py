################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200525
# Problem link      : https://leetcode.com/problems/uncrossed-lines/
################################################################

# import collections

class Solution:    
    # def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
    #     dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    #     for i in range(1, len(A)+1):
    #         for j in range(1, len(B)+1):
    #             dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else max(dp[i-1][j], dp[i][j-1])
    #     return dp[len(A)][len(B)]
    
    # more efficient with memory
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        prv = [0] * (m + 1) # [0 for _ in range(m + 1)]
        nxt = [0] * (m + 1) # [0 for _ in range(m + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                nxt[j] = max(prv[j-1] + (A[i-1] == B[j-1]), prv[j], nxt[j-1])
            prv, nxt = nxt, prv
        return prv[m]

    # # more efficient with memory alternative
    # def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
    #     n, m = len(A), len(B)
    #     dp = [[0 for _ in range(m+1)] for _ in range(2)]
    #     for i in range(1, n + 1):
    #         for j in range(1, m + 1):
    #             dp[i%2][j] = dp[i%2^1][j-1]+1 if A[i-1]==B[j-1] else max(dp[i%2^1][j], dp[i%2][j-1])
    #     return dp[n%2][m] 
    
    # lee215
    # def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
    #     dp, n, m = collections.defaultdict(int), len(A), len(B)
    #     for i in range(n):
    #         for j in range(m):
    #             dp[i,j] = max( dp[i-1,j-1] + (A[i]==B[j]), dp[i,j-1], dp[i-1,j])
    #     return dp[n-1,m-1]
    
    # def maxUncrossedLines(self, A, B):
    #     m, n = len(A), len(B)
    #     dp = [0] * (n + 1)
    #     for i in xrange(m):
    #         for j in range(n)[::-1]:
    #             if A[i] == B[j]: dp[j + 1] = dp[j] + 1
    #         for j in range(n):
    #             dp[j + 1] = max(dp[j + 1], dp[j])
    #     return dp[n]
