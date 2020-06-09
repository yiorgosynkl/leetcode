################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200609
# Problem link      : https://leetcode.com/problems/is-subsequence/
################################################################

class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool: # recursive
    #     if not s: return True
    #     if not t: return False
    #     return self.isSubsequence(s[int(s[0] == t[0]):], t[1:])
    
    # def isSubsequence(self, s: str, t: str) -> bool: # iterative
    #     if not s: return True 
    #     for ch in t:
    #         if s[0]==ch: s = s[1:]
    #         if not s: return True
    #     return False
    
    # Stefan Pochmann
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)
