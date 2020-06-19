################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200619
# Problem link      : https://leetcode.com/problems/longest-duplicate-substring/
################################################################

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def findsub(S: str, l: int):
            hashes = set()
            for i in range(len(S) - l + 1):
                h = hash(S[i:i+l])
                if h in hashes: return S[i:i+l]
                else: hashes.add(h)
            return ''        
                
        ans = ''
        lo, hi = 0, len(S)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            sub = findsub(S, mid)
            if sub == '':
                hi = mid - 1
            else:
                ans = sub
                lo = mid
        return ans
            