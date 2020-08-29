################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200829
# Problem link      : https://leetcode.com/problems/pancake-sorting/
################################################################

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:  
        def reverse(A, k):
            return list(reversed(A[0:k])) + A[k:]
        ans = []
        times = len(A)
        while times:
            maxi = A.index(max(A[:times]))
            A = reverse(A, maxi+1)
            ans.append(maxi+1)
            A = reverse(A, times)
            ans.append(times)
            times -= 1
        return ans
        
    # @lee215
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1): # nums from 1 to len(A)
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res