################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200906
# Problem link      : https://leetcode.com/problems/image-overlap/
################################################################

class Solution:
#     def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
#         n_rows, n_cols = len(A), len(A[0]) # same for A and B

#         def overlap(r, c):
#             a = [l[max(c,0):min(n_cols+c,n_cols)] for l in A[max(r,0):min(n_rows+r,n_rows)]]
#             # a = A[max(r,0):min(n_rows+r,n_rows)][max(c,0):min(n_cols+c,n_cols)]
#             b = [l[max(-c,0):min(n_cols-c,n_cols)] for l in B[max(-r,0):min(n_rows-r,n_rows)]]
#             # b = B[max(-r,0):min(n_rows-r,n_rows)][max(-c,0):min(n_cols-c,n_cols)]
#             res = 0 
#             for i in range(len(a)):
#                 for j in range(len(a[0])):
#                     res += a[i][j] & b[i][j]
#             return res
        
#         ans = 0
#         for r in range(-n_rows+1, n_rows):
#             for c in range(-n_cols+1, n_cols):
#                 ans = max(overlap(r,c), ans)
#         return ans
                    
    # @lee215 sick solution
    def largestOverlap(self, A, B):
        A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item] # coordinates of 1's in image A
        B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item] # coordinates of 1's in image B
        count = collections.Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B) # count amout of pairs of coords with exactly the same shift and keep maximum (linear transformation vectors)
        return max(count.values() or [0])  # if the input has no 1, count will be None, that why we need or [0]

    # !! convolution of two matrices has the same result !!

    