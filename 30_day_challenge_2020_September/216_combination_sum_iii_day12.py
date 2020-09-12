################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200912
# Problem link      : https://leetcode.com/problems/combination-sum-iii/
################################################################

from itertools import combinations

class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         ans = []
#         for t in combinations(range(1,10), k):
#             if sum(t) == n: ans.append(list(t))
#         return ans
            
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(t) for t in combinations(range(1,10), k) if sum(t) == n]
    
#     # @StefanPochmann
#     # recursive
#     def combinationSum3(self, k, n):
#         def combs(k, n, cap):
#             if not k:
#                 return [[]] * (not n)
#             return [comb + [last]
#                     for last in range(1, cap)
#                     for comb in combs(k-1, n-last, last)]
#         return combs(k, n, 10)

#     # iterative
#     def combinationSum3(self, k, n):
#     combs = [[]]
#     for _ in range(k):
#         combs = [[first] + comb
#                  for comb in combs
#                  for first in range(1, comb[0] if comb else 10)]
#     return [c for c in combs if sum(c) == n]

#     # reduce
#     def combinationSum3(self, k, n):
#         return [c for c in
#                 reduce(lambda combs, _: [[first] + comb
#                                          for comb in combs
#                                          for first in range(1, comb[0] if comb else 10)],
#                        range(k), [[]])
#                 if sum(c) == n]

