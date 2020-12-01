################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201201
# Problem link      : https://leetcode.com/problems/sliding-window-maximum/
################################################################

import bisect
from collections import deque

class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     srt, ans = [], []
    #     for n in nums[:k-1]:
    #         bisect.insort(srt, n)
    #     for s, e in zip(range(len(nums)-k+1), range(k-1, len(nums))):
    #         bisect.insort(srt, nums[e])
    #         ans.append(srt[-1])
    #         del srt[bisect.bisect_left(srt, nums[s])]
    #     return ans

    # # slow one liner
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     return [max(nums[st:st+k]) for st in range(len(nums) - k + 1)]
    
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     # left is big, right is small
    #     # we keep indices instead of values so we can conclude that the leftmost is inside the window
    #     q = deque([]) 
    #     for i in range(k-1):
    #         n = nums[i]
    #         while q and nums[q[-1]] < n: q.pop()
    #         q.append(i)
    #     ans = []
    #     for i in range(k-1, len(nums)):
    #         n = nums[i]
    #         while q and q[0] < i - k + 1: q.popleft()
    #         while q and nums[q[-1]] < n: q.pop()
    #         q.append(i)
    #         ans.append(nums[q[0]])
    #     return ans
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, out = deque([]), [] # sorted array of indices and output
        for i, n in enumerate(nums):
            if q and q[0] < i - k + 1: q.popleft() # remove indices out of window
            while q and nums[q[-1]] < n: q.pop() # remove indices with value smaller than the rightmost
            q.append(i)
            if i >= k-1: out.append(nums[q[0]]) # full window
        return out
