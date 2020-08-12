################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200811
# Problem link      : https://leetcode.com/problems/h-index/
################################################################

class Solution:
    # def hIndex(self, citations: List[int]) -> int:
    #     def sorted_hIndex(self, cit: List[int]) -> int:
    #         if not cit: return 0
    #         lo, hi = 0, min(cit[-1], len(cit))
    #         while lo < hi:
    #             h = (lo + hi + 1) // 2 # if it's .5 than round up (because hi is decreasing)
    #             if cit[-h] >= h: # does the h-th best paper has more than h citations? 
    #                 lo = h
    #             else:
    #                 hi = h - 1
    #         return lo
    #     return sorted_hIndex(sorted(citations))
    
    # counting sort (count multiplicity of elements that belong to a given range)
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0]* (n+1) # number of papers with i citations
        for cit in citations:
            counts[min(cit, n)] += 1
        p, h = counts[n], n # papers, h score
        while p < h:
            h -= 1
            p += counts[h]
        return h
            
