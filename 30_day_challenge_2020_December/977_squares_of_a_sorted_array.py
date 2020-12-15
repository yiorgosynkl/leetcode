################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201215
# Problem link      : https://leetcode.com/problems/squares-of-a-sorted-array/
################################################################

class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     i = 0
    #     while i < len(nums) and nums[i] < 0:
    #         i += 1
    #     j = i - 1
    #     sq = []
    #     while j >= 0 or i < len(nums):
    #         if j < 0 or (i < len(nums) and abs(nums[j]) > abs(nums[i])):
    #             sq.append(nums[i]**2)
    #             i += 1
    #         else: # i >= len(nums) or (j >= 0 and abs(nums[j]) <= abs(nums[i])):
    #             sq.append(nums[j]**2)
    #             j -= 1
    #     return sq

    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg, pos = [n**2 for n in nums if n < 0], [n**2 for n in reversed(nums) if n >= 0] # positives include 0s
        sq = []
        while neg or pos:
            if not neg or (pos and pos[-1] < neg[-1]): 
                sq.append(pos.pop())
            else: 
                sq.append(neg.pop())
        return sq
    
    
    # starting from edges and converge to the middle
    def sortedSquares(self, A):
        answer = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer

    # actually it's O(n) using timsort algorithm (standard sorting of Python)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([v**2 for v in A])
