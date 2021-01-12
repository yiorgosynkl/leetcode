################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210111
# Problem link      : https://leetcode.com/problems/merge-sorted-array/
################################################################

class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     l = m + n - 1
    #     m, n = m - 1, n - 1
    #     while l >= 0:
    #         if n < 0 or (m >= 0 and nums1[m] > nums2[n]):
    #             nums1[l] = nums1[m]
    #             m -= 1
    #         else: # m < 0 or (n >= 0 and nums1[m] <= nums2[n]):
    #             nums1[l] = nums2[n]
    #             n -= 1
    #         l -= 1
    #     return nums1
    
    def merge(self, nums1, m, nums2, n):
            while n > 0:
                if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                    nums1[m+n-1] = nums2[n-1]
                    n -= 1
                else:
                    nums1[m+n-1] = nums1[m-1]
                    m -= 1
