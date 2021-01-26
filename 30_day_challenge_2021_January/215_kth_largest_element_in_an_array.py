################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210116
# Problem link      : https://leetcode.com/problems/kth-largest-element-in-an-array/
################################################################

import math
import random

class Solution:
    # @yiorgosynkl, quickselect
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr):      
            pivot, pi = arr[-1], 0
            for i in range(len(arr) - 1): 
                if arr[i] <= pivot: 
                    arr[pi], arr[i] = arr[i], arr[pi] 
                    pi += 1
            arr[pi], arr[-1] = arr[-1], arr[pi] 
            return pi 
        
        def kthSmallest(arr, k): 
            if k <= 0 or k > len(arr):
                return math.inf
            mid = partition(arr) 
            if (k == mid + 1): 
                return arr[mid]
            elif (k < mid + 1):
                return kthSmallest(arr[:mid], k)
            else: # (mid + 1 < k):
                return kthSmallest(arr[mid+1:], k - (mid + 1))
        
        random.shuffle(nums) # shuffle list to guarantee O(N)
        return kthSmallest(nums, len(nums) - k + 1)

#     # quickselect (code from geekforgeeks)
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def partition(arr, l, r):      
#             x = arr[r] 
#             i = l 
#             for j in range(l, r): 

#                 if arr[j] <= x: 
#                     arr[i], arr[j] = arr[j], arr[i] 
#                     i += 1

#             arr[i], arr[r] = arr[r], arr[i] 
#             return i 
        
#         def kthSmallest(arr, l, r, k): 
#             # if k is smaller than number of 
#             # elements in array 
#             if (k > 0 and k <= r - l + 1): 

#                 # Partition the array around last 
#                 # element and get position of pivot 
#                 # element in sorted array 
#                 index = partition(arr, l, r) 

#                 # if position is same as k 
#                 if (index - l == k - 1): 
#                     return arr[index] 

#                 # If position is more, recur  
#                 # for left subarray  
#                 if (index - l > k - 1): 
#                     return kthSmallest(arr, l, index - 1, k) 

#                 # Else recur for right subarray  
#                 return kthSmallest(arr, index + 1, r,  
#                                     k - index + l - 1) 
#             return -1
        
#         return kthSmallest(nums, 0, len(nums)-1, len(nums) - k + 1)

    # # simplest, O(nlogn)
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return sorted(nums)[len(nums)-k]

    # keep k largest elements in priority queue
    
    
    
    
#________________ solutions by @OldCodingFarmer ________________#

#     # O(nlgn) time
#     def findKthLargest1(self, nums, k):
#         return sorted(nums, reverse=True)[k-1]

#     # O(nk) time, bubble sort idea, TLE
#     def findKthLargest2(self, nums, k):
#         for i in xrange(k):
#             for j in xrange(len(nums)-i-1):
#                 if nums[j] > nums[j+1]:
#                     # exchange elements, time consuming
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#         return nums[len(nums)-k]

#     # O(nk) time, selection sort idea
#     def findKthLargest3(self, nums, k):
#         for i in xrange(len(nums), len(nums)-k, -1):
#             tmp = 0
#             for j in xrange(i):
#                 if nums[j] > nums[tmp]:
#                     tmp = j
#             nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
#         return nums[len(nums)-k]

#     # O(k+(n-k)lgk) time, min-heap
#     def findKthLargest4(self, nums, k):
#         heap = []
#         for num in nums:
#             heapq.heappush(heap, num)
#         for _ in xrange(len(nums)-k):
#             heapq.heappop(heap)
#         return heapq.heappop(heap)

#     def findKthLargest(self, nums, k):
#         heap = nums[:k]
#         heapify(heap)
#         for n in nums[k:]:
#             heappushpop(heap, n)
#         return heap[0]

#     # O(k+(n-k)lgk) time, min-heap        
#     def findKthLargest5(self, nums, k):
#         return heapq.nlargest(k, nums)[-1]

#     # O(n) time, quick selection
#     def findKthLargest(self, nums, k):
#         # convert the kth largest to smallest
#         return self.findKthSmallest(nums, len(nums)+1-k)

    # def findKthSmallest(self, nums, k):
    #     # choose the right-most element as pivot   
    #     def partition(nums, l, r):
    #         low = l
    #         while l < r:
    #             if nums[l] < nums[r]:
    #                 nums[l], nums[low] = nums[low], nums[l]
    #                 low += 1
    #             l += 1
    #         nums[low], nums[r] = nums[r], nums[low]
    #         return low

    #     if nums:
    #         pos = partition(nums, 0, len(nums)-1)
    #         if k > pos+1:
    #             return self.findKthSmallest(nums[pos+1:], k-pos-1)
    #         elif k < pos+1:
    #             return self.findKthSmallest(nums[:pos], k)
    #         else:
    #             return nums[pos]
        