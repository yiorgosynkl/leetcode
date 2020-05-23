################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200523
# Problem link      : https://leetcode.com/problems/interval-list-intersections/
################################################################

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a, b = 0, 0
        c = []
        while a < len(A) and b < len(B):
            a_start, a_end = A[a]
            b_start, b_end = B[b]
            c_start, c_end = max(a_start, b_start), min(a_end, b_end)
            if c_start <= c_end:
                c.append([c_start, c_end])
            if a_end < b_end: 
                a += 1
            elif b_end < a_end:
                b += 1
            else:
                a += 1
                b += 1
        return c
            