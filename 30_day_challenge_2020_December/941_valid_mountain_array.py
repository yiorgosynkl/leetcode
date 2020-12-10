################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201210
# Problem link      : https://leetcode.com/problems/valid-mountain-array/
################################################################

class Solution:
    # def validMountainArray(self, arr: List[int]) -> bool:
    #     if len(arr) < 3: return False
    #     i, ln = 0, len(arr)
    #     while i < ln-1 and arr[i] < arr[i+1]: i += 1
    #     if i == 0 or i == ln-1: return False
    #     while i < ln-1 and arr[i] > arr[i+1]: i += 1
    #     return i == ln-1
    
    # @lee215
    def validMountainArray(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1