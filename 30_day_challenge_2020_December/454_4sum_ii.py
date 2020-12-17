################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201217
# Problem link      : https://leetcode.com/problems/4sum-ii/
################################################################

from collections import defaultdict

class Solution:
    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     return sum([int(a+b+c+d==0) for a in A for b in B for c in C for d in D])
        
    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     ds = {-d: D.count(d) for d in set(D)}
    #     return sum([ds.get(a+b+c, 0) for a in A for b in B for c in C]) 
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB, CD = defaultdict(int), defaultdict(int)
        for a in A:
            for b in B:
                AB[a+b] += 1
        for c in C:
            for d in D:
                CD[+c+d] += 1
        out = 0
        for num, ts in AB.items(): # num and times
            out += ts*CD[-num]
        return out
    
#     # without defaultdict
#     def fourSumCount(self, A, B, C, D):
#             ab = {}
#             for i in A:
#                 for j in B:
#                     ab[i+j] = ab.get(i+j, 0) + 1

#             ans = 0
#             for i in C:
#                 for j in D:
#                     ans += ab.get(-i-j, 0)       
#             return ans
    
#     # @StefanPochmann
#     def fourSumCount(self, A, B, C, D):
#         AB = collections.Counter(a+b for a in A for b in B)
#         return sum(AB[-c-d] for c in C for d in D)
