################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200427
# Problem link      : https://leetcode.com/problems/maximal-square/
################################################################


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # magic dp equation dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.
        if not matrix:
            return 0
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        
        dp = [[0]*(n_cols+1) for _ in range(n_rows+1)] # one more row and column full of zeros
        ans = 0
        for i in range(1, n_rows+1):
            for j in range(1, n_cols+1):
                if matrix[i-1][j-1] == '1': 
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    ans = max(ans, dp[i][j])
        return ans ** 2
    
        # correct way to initialise:
        # dp = [[0]*(n_cols+1) for _ in range(n_rows+1)]
        # !!! this would cause an ERROR !!! 
        # dp = [[0]*n_cols]*n_rows
        # print(dp)
        # dp[0][0] = 1 # changes the first element of every row
        # print(dp)
        


    # brute force
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         n_rows = len(matrix)
#         n_cols = len(matrix[0])
        
#         def explore(r,c):
#             edge = 0
#             prod = int(matrix[r][c])
#             while prod:
#                 edge += 1
#                 if edge + r == n_rows or edge + c == n_cols:
#                     break
#                 for i in range(edge):
#                     prod *= int(matrix[r+i][c+edge])
#                     prod *= int(matrix[r+edge][c+i])
#                 prod *= int(matrix[r+edge][c+edge])
#             return edge
        
#         res = 0
#         for r in range(n_rows):
#             for c in range(n_cols):
#                 res = max(res, explore(r, c))
#         return res**2

# Stefan Pochman

# overwriting matrix
# class Solution:
#     def maximalSquare(self, A):
#         for i in range(len(A)):
#             for j in range(len(A[i])):
#                 A[i][j] = int(A[i][j])
#                 if A[i][j] and i and j:
#                     A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
#         return len(A) and max(map(max, A)) ** 2

# using 2 rows of extra space 
# class Solution:
#     def maximalSquare(self, A):
#         area = 0
#         if A:
#             p = [0] * len(A[0])
#             for row in A:
#                 s = map(int, row)
#                 for j, c in enumerate(s[1:], 1):
#                     s[j] *= min(p[j-1], p[j], s[j-1]) + 1
#                 area = max(area, max(s) ** 2)
#                 p = s
#         return area
