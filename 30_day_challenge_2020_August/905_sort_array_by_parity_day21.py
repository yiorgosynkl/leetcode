################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200821
# Problem link      : https://leetcode.com/problems/sort-array-by-parity/
################################################################

class Solution:
    # two pointers, left and right
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        le, ri = 0, len(A) - 1
        while le < ri:
            if A[le] % 2 > A[ri] % 2: A[le], A[ri] = A[ri], A[le]
            if A[le] % 2 == 0: le += 1
            if A[ri] % 2 == 1: ri -= 1
        return A

    # two pointers, fast and slow
    # def sortArrayByParity(self, A: List[int]) -> List[int]:
    #     slow, fast = 0, 0
    #     for fast in range(len(A)):
    #         if A[fast] % 2 == 0:
    #             A[slow], A[fast] = A[fast], A[slow]
    #             slow += 1
    #     return A

    # new lists
    # def sortArrayByParity(self, A: List[int]) -> List[int]:
    #     return [ev for ev in A if ev % 2 == 0] + [od for od in A if od % 2 == 1]
    
    # def sortArrayByParity(self, A: List[int]) -> List[int]:
    #     return sorted(A, key=lambda x: x % 2)
