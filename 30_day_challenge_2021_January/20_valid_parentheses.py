################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210120
# Problem link      : https://leetcode.com/problems/valid-parentheses/
################################################################

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        match = { ']':'[', '}':'{', ')':'(' }
        for c in s:
            if c in match.values():
                stk.append(c)
            elif c in match.keys() and stk and stk[-1] == match[c]:
                stk.pop()
            else:
                return False
        return not stk     
        
#     def isValid(self, s):
#         while '[]' in s or '()' in s or '{}' in s:
#             s = s.replace('[]','').replace('()','').replace('{}','')
#         return not len(s)
