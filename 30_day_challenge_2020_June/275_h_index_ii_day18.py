################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200618
# Problem link      : https://leetcode.com/problems/h-index-ii/
################################################################

class Solution:
    def hIndex(self, cit: List[int]) -> int:
        if not cit: return 0
        lo, hi = 0, min(cit[-1], len(cit))
        while lo < hi:
            h = (lo + hi + 1) // 2 # if it's .5 than round up (because hi is decreasing)
            if cit[-h] >= h: # does the h-th best paper has more than h citations? 
                lo = h
            else:
                hi = h - 1
        return lo
    
    # def hIndex(self, citations):
    #     n = len(citations)
    #     l, r = 0, n-1
    #     while l <= r:
    #         mid = (l+r)/2
    #         if citations[mid] >= n-mid:
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     return n-l
            