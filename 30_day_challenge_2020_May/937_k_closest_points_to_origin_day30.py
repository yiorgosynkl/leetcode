################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200530
# Problem link      : https://leetcode.com/problems/k-closest-points-to-origin/
################################################################

import bisect

def dist(item):
    return item[0]**2 + item[1]**2

# partition with last element as pivot 
def partition(nums, lo, hi):
    pivot = dist(nums[hi])
    e = lo # enter pivot index
    for i in range(lo, hi):
        if dist(nums[i]) < pivot:
            nums[e], nums[i] = nums[i], nums[e] # swap 
            e += 1
    nums[e], nums[hi] = nums[hi], nums[e] # swap
    return e

# find the k-th smallest element (0-index)
def quickselect(nums, lo, hi, k):
    e = partition(nums, lo, hi)
    if k == e:
        return nums[:k+1]
    elif k < e:
        return quickselect(nums, lo, e - 1, k)
    else:
        return quickselect(nums, e + 1, hi, k)

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return quickselect(points, 0, len(points) - 1, K - 1)
    
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         return sorted(points, key = lambda point: point[0]**2 + point[1]**2)[:K]
    
#     # O(N*logK)
#     def kClosest(self, points, K):
#             return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
        
    