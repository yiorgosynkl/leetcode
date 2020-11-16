################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201116
# Problem link      : https://leetcode.com/problems/longest-mountain-in-array/
################################################################

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A: return 0
        n = len(A)
        ltr, rtl = [1]*n, [1]*n # left to right, right to left
        for i in range(1, n): ltr[i] = ltr[i-1] + 1 if A[i] > A[i-1] else 1
        for i in reversed(range(0, n-1)): rtl[i] = rtl[i+1] + 1 if A[i] > A[i+1] else 1
        return max(ltr[i] + rtl[i] - 1 if ltr[i] >= 2 and rtl[i] >= 2 else 0 for i in range(n))
        
    # # 1-pass solution
    # def longestMountain(self, A: List[int]) -> int:
    #     if not A: 
    #         return 0
    #     n, idx = len(A), 1
    #     ans = 0
    #     while idx < n:
    #         while idx < n and A[idx-1] > A[idx]: 
    #             idx += 1 # get passed the starting negative slope
    #         mnt = 1
    #         while idx < n and A[idx-1] < A[idx]:
    #             mnt += 1
    #             idx += 1
    #         if idx == n: 
    #             break
    #         if A[idx-1] == A[idx]:
    #             idx += 1
    #             continue
    #         while idx < n and A[idx-1] > A[idx]:
    #             mnt += 1
    #             idx += 1
    #         ans = max(mnt, ans)
    #     return ans
    
#     # @lee215 one pass
#     def longestMountain(self, A):
#         res = up = down = 0
#         for i in range(1, len(A)):
#             if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
#             up += A[i - 1] < A[i]
#             down += A[i - 1] > A[i]
#             if up and down: res = max(res, up + down + 1)
#         return res

    # # seems O(n^2) but each element will be checked at most twice, so O(n)
    # # straightforward solution
    # def longestMountain(self, A, res = 0):
    #     for i in range(1, len(A) - 1):
    #         if A[i + 1] < A[i] > A[i - 1]:
    #             l = r = i
    #             while l and A[l] > A[l - 1]: l -= 1
    #             while r + 1 < len(A) and A[r] > A[r + 1]: r += 1
    #             if r - l + 1 > res: res = r - l + 1
    #     return res
    
#     # official solution
#     def longestMountain(self, A):
#         N = len(A)
#         ans = base = 0

#         while base < N:
#             end = base
#             if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
#                 #set end to the peak of this potential mountain
#                 while end+1 < N and A[end] < A[end+1]:
#                     end += 1

#                 if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
#                     #set 'end' to right-boundary of mountain
#                     while end+1 < N and A[end] > A[end+1]:
#                         end += 1
#                     #record candidate answer
#                     ans = max(ans, end - base + 1)

#             base = max(end, base + 1)

#         return ans
