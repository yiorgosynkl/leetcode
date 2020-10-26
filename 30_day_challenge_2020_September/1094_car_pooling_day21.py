################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201026
# Problem link      : https://leetcode.com/problems/car-pooling/
################################################################

from operator import itemgetter
# sorted(trips, key=itemgetter(2))

class Solution:
#     #  O(N logN)
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         timestamp = []
#         for trip in trips:
#             timestamp.append([trip[1], trip[0]])
#             timestamp.append([trip[2], -trip[0]])
#         timestamp.sort()

#         used_capacity = 0
#         for time, passenger_change in timestamp:
#             used_capacity += passenger_change
#             if used_capacity > capacity:
#                 return False
#         return True


    # @lee215
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for i, c in sorted(x for pas, s, e in trips for x in [[s, pas], [e,-pas]]):
            # the sorting will take the time and then the passenger, else we should check that i is different than next i
            capacity -= c
            if capacity < 0: 
                return False
        return True
    
#     # O(N)
#     # bucket sort, because 0 <= trip[1] < trip[2] <= 1000
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         timestamp = [0] * 1001
#         for trip in trips:
#             timestamp[trip[1]] += trip[0]
#             timestamp[trip[2]] -= trip[0]

#         used_capacity = 0
#         for passenger_change in timestamp:
#             used_capacity += passenger_change
#             if used_capacity > capacity:
#                 return False

#         return True

