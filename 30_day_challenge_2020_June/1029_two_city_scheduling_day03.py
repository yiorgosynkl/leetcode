################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200603
# Problem link      : https://leetcode.com/problems/two-city-scheduling/
################################################################

import bisect

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda cost: cost[0] - cost[1])
        return sum([costs[i][i>=n] for i in range(len(costs))]) 
        # cost[i][0] for 0 -> n-1 and cost[i][1] for n -> 2n-1
        
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         count, n = 0, len(costs) // 2
#         alpha, bravo = [], []
#         for a, b in costs:
#             count += min(a,b)
#             if a > b:
#                 bisect.insort(bravo, a-b)
#             else:
#                 bisect.insort(alpha, b-a)
#         if len(alpha) > len(bravo):
#             count += sum(alpha[:n-len(bravo)])
#         if len(alpha) < len(bravo):
#             count += sum(bravo[:n-len(alpha)])
#         return count

 
        