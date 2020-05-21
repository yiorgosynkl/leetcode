################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200521
# Problem link      : https://leetcode.com/problems/count-square-submatrices-with-all-ones/
################################################################

# solution by lee215
# class Solution:
#     def countSquares(self, A):
#         for i in xrange(1, len(A)):
#             for j in xrange(1, len(A[0])):
#                 A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
#         return sum(map(sum, A))


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = [[0 for i in range(n)] for j in range(m)]
        count_squre = 0
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    ans[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    ans[i][j] = matrix[i][j] + min(ans[i-1][j],ans[i-1][j-1],ans[i][j-1])
                count_squre += ans[i][j]
        print(ans)
        return count_squre
      

# import numpy as np
# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         array = np.array(matrix)
#         rows, cols = len(matrix), len(matrix[0])
#         sums = np.zeros(shape=(rows+1,cols+1))
#         # sums[0, 0] = array[0, 0]
#         # for i in range(1, rows+1):
#         #     sums[i, 0] = sums[i - 1, 0] + array[i, 0]
#         # for j in range(1, cols+1):
#         #     sums[0, j] = sums[0, j - 1] + array[0, j]
#         for i in range(1, rows+1):
#             for j in range(1, cols+1):
#                 sums[i, j] = sums[i, j-1] + sums[i-1, j] - sums[i-1, j-1] + array[i-1, j-1]
#         # print(sums)
#         count = 0
#         for e in range(1, min(rows, cols) + 1): # loop edge length
#             for i in range(rows - e + 1): # loop upper left corner of subarray
#                 for j in range(cols - e + 1):
#                     if sums[i+e,j+e] - sums[i,j+e] - sums[i+e,j] + sums[i,j] == e**2:
#                         # print(i, j, i+e, j+e)
#                         count += 1
#         return count