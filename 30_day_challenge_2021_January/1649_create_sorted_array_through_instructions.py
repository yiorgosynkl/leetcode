################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 2021010
# Problem link      : https://leetcode.com/problems/create-sorted-array-through-instructions/
################################################################

import bisect

class Solution:
    # # @yiorgosynkl
    # def createSortedArray(self, instructions: List[int]) -> int:
    #     srt, cost = [], 0   # sorted
    #     for num in instructions:
    #         new_cost = min(bisect.bisect_left(srt, num),  len(srt) - bisect.bisect(srt, num))
    #         cost = ( cost + new_cost ) % (1000000007)
    #         bisect.insort(srt, num)     # this operation is expensive
    #     return cost


    # def createSortedArray(self, A: List[int]) -> int:
    #     MOD = 10**9 + 7
    #     order = []    
    #     ans = 0
    #     for i, a in enumerate(A):
    #         l, r = bisect.bisect_left(order, a), bisect.bisect(order, a)
    #         ans += min(l, i-r)
    #         # order.insert(r, a) # TLE, (EDIT: probably AC, see @ManuelP's comment)
    #         # bisect.insort(order, a) # TLE
    #         order[r:r] = [a]      # we can use slice to make it quicker
    #     return ans % MOD    

# from sortedcontainers import SortedList

#     # @DBabichev
#     def createSortedArray(self, instructions):
#         SList = SortedList()
#         ans = 0
#         for num in instructions:
#             ans += min(SList.bisect_left(num), len(SList) - SList.bisect_right(num))
#             ans %= (10**9 + 7)
#             SList.add(num)  

#         return ans


    # @lee215 using binary indexed tree
    # useful link https://cp-algorithms.com/data_structures/fenwick.html
    def createSortedArray(self, A):
        m = max(A)
        # we also have a fantastic array COUNTS of numbers from 0 to m, which holds the cardinality of each element
        c = [0] * (m + 1) # coresponding binary indexed tree for the COUNTS array

        def update(x):  # changes the array c accordingly
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):     # returns the sum from 0 to x of array COUNTS, that means number of nums <= x
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)
    