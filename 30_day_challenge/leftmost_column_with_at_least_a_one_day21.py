# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        [n, m] = mat.dimensions()
        def binary_search(row, lo, hi):
            if mat.get(row, hi) == 0:
                return hi + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if mat.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            return hi
        
        res = m
        for row in range(n):
            res = min(res, binary_search(row, 0, res - 1))
            if res == 0: return 0
        
        if res == m: return -1
        return res
    
# complexity O(n + logm * m), best case Omega(n + logm)
    
# complexity O(n + m), best case Omega(n + logm)
# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         M, N = binaryMatrix.dimensions()
        
#         r, c = 0, N - 1 
#         leftmost_col = -1
#         while r < M and c >= 0:
#             if binaryMatrix.get(r,c) == 1:
#                 leftmost_col = c
#                 c -= 1
#             else:
#                 r += 1
#         return leftmost_col
        
        
        