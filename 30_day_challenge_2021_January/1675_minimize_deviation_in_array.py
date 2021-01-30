################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210130
# Problem link      : https://leetcode.com/problems/minimize-deviation-in-array/
################################################################

import math
from heapq import heappush, heappop, heapreplace, heapify

class Solution:
    # @DBabichev
    def minimumDeviation(self, nums):
        heap = []
        for num in nums:
            tmp = num
            while tmp%2 == 0: tmp//=2
            heap.append((tmp, max(num, tmp*2)))
        
        mx = max(i for i,j in heap)
        heapify(heap)
        ans = math.inf

        while len(heap) == len(nums):
            num, limit = heappop(heap)
            ans = min(ans, mx - num)
            if num < limit:
                heappush(heap, (num*2, limit))
                mx = max(mx, num*2)
            
        return ans
    
    # # @lee215,  time O(n * logn * logM), space: O(n), using min-heap
    # def minimumDeviation(self, A):
    #     pq = []
    #     for a in A:
    #         heapq.heappush(pq, [a / (a & -a), a])
    #     res = float('inf')
    #     ma = max(a for a, a0 in pq)
    #     while len(pq) == len(A):
    #         a, a0 = heapq.heappop(pq)
    #         res = min(res, ma - a)
    #         if a % 2 == 1 or a < a0:
    #             ma = max(ma, a * 2)
    #             heapq.heappush(pq, [a * 2, a0])
    #     return res

    # # @lee215, using max heap (use min heap, change sign when add/remove a num from the heap)
    # # we add the opposite values and change num when we remove them
    # # since odd can only be doubled once, doulbe them and try shrinking all of them
    # def minimumDeviation(self, A):
    #     pq = []
    #     for a in A:
    #         heapq.heappush(pq, -a * 2 if a % 2 else -a)
    #     res = float('inf')
    #     mi = -max(pq)
    #     while len(pq) == len(A):
    #         a = -heapq.heappop(pq)
    #         res = min(res, a - mi)
    #         if a % 2 == 0:
    #             mi = min(mi, a / 2)
    #             heapq.heappush(pq, -a / 2)
    #     return res
