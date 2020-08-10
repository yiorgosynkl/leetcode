################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200810
# Problem link      : https://leetcode.com/problems/excel-sheet-column-number/
################################################################

import functools

class Solution:
#     def titleToNumber(self, s: str) -> int:
#         ans = 0
#         for ch in s:
#             ans = ans * 26 + ord(ch) - ord('A') + 1
#         return ans
    
    # convert 26-base to 10-base number
    def titleToNumber(self, s: str) -> int:
        return functools.reduce(lambda x,y: 26*x+y, [ord(ch)-ord('A')+1 for ch in s])
    
#     def titleToNumber(self, s: str) -> int:
#         return functools.reduce(lambda x,y: 26*x+ord(y)-64, s, 0)
        
#     def titleToNumber(self, s: str) -> int:
#         return sum((ord(ch) - 64) * (26 ** exp) for exp, ch in enumerate(s[::-1]))
