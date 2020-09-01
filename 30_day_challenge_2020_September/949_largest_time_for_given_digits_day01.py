################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200901
# Problem link      : https://leetcode.com/problems/largest-time-for-given-digits/
################################################################

from itertools import permutations

class Solution:
#     def largestTimeFromDigits(self, A: List[int]) -> str:
#         out, time = "", -1
#         for i, j, k, l in permutations(A, 4):
#             hours, mins = i*10+j, k*10+l
#             if 0 <= hours < 24 and 0 <= mins < 60:
#                 if time < hours * 60 + mins:
#                     out, time = '{}{}:{}{}'.format(i,j,k,l), hours * 60 + mins
#         return out
    
    # @lee215
    def largestTimeFromDigits(self, A: List[int]) -> str:
        return max(["%d%d:%d%d" % t for t in permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
