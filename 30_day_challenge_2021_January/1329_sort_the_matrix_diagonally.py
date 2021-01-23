################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210123
# Problem link      : https://leetcode.com/problems/sort-the-matrix-diagonally/
################################################################

from collections import defaultdict 

class Solution:
    # def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    #     rs, cs = len(mat), len(mat[0])
    #     for df in range(-rs+1, cs): # df = c - r --> c = df + r
    #         srt = sorted([mat[r][df+r] for r in range(max(0,-df), min(rs, cs-df))])
    #         for i, r in enumerate(range(max(0,-df), min(rs, cs-df))):  
    #             mat[r][df+r] = srt[i]
    #     return mat
    
    # # O(n^2) bubble sort
    # def diagonalSort(self, mat):
    #     rs, cs = len(mat), len(mat[0]) 
    #     for k in range(min(rs, cs)):
    #         for r in range(rs-1):
    #             for c in range(cs-1):
    #                 if mat[r][c] > mat[r+1][c+1]:
    #                     mat[r][c], mat[r+1][c+1] = mat[r+1][c+1], mat[r][c]
    #     return mat

       
    # @lee215, dictionary easy way to pass, space: O(N*M)
    def diagonalSort(self, A):
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)
        for i in xrange(n):
            for j in xrange(m):
                d[i - j].append(A[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in xrange(n):
            for j in xrange(m):
                A[i][j] = d[i - j].pop()
        return A
    
#     # @StefanPochmann, space: O(N*M)
#     def diagonalSort(self, A):
#         m, n = len(A), len(A[0])
#         def sort(i, j):
#             ij = zip(range(i, m), range(j, n))
#             vals = iter(sorted(A[i][j] for i, j in ij))
#             for i, j in ij:
#                 A[i][j] = next(vals)
#         for i in range(m): sort(i, 0)
#         for j in range(n): sort(0, j)
#         return A
    
#     # @StefanPochmann, more general version
#     def diagonalSort(self, A):
#         m, n = len(A), len(A[0])
#         def sort(i, j):
#             vals = []
#             while i < m and j < n:
#                 vals.append(A[i][j])
#                 i += 1
#                 j += 1
#             vals.sort()
#             while i and j:
#                 j -= 1
#                 i -= 1
#                 A[i][j] = vals.pop()
#         for i in range(m): sort(i, 0)
#         for j in range(n): sort(0, j)
#         return A
    