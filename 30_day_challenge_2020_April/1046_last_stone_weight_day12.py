################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200412
# Problem link      : https://leetcode.com/problems/last-stone-weight/
################################################################

from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones) 
        while len(stones) > 1:
            # print(stones)
            alpha = heappop(stones)
            bravo = heappop(stones)
            new = - abs(alpha - bravo)
            if new:
                heappush(stones, new)
        if stones:
            return -stones[0]
        return 0
    
# class Solution:
#     def lastStoneWeight(self, A):
#         h = [-x for x in A]
#         heapq.heapify(h)
#         while len(h) > 1 and h[0] != 0:
#             heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
#         return -h[0]
