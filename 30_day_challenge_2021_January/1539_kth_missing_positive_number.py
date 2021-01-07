################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210106
# Problem link      : https://leetcode.com/problems/kth-missing-positive-number/
################################################################

class Solution:
    # # recursive way, O(n)
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     def find(arr, v, k):
    #         if arr and arr[0] == v:
    #             return find(arr[1:], v+1, k)
    #         if k == 1:
    #             return v
    #         return find(arr, v+1, k-1)
    #     return find(arr, 1, k)
    
    # # iterative way,  O(n)
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     v = 1
    #     for n in arr:
    #         if v == n:
    #             v += 1
    #         else:
    #             k -= n - v
    #             v = n
    #             if k <= 0:
    #                 break
    #             else:
    #                 v += 1
    #     return v + k - 1
            
    # # iterative way, slower, O(n+k)
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     v, i = 1, 0
    #     while k > 0:
    #         if i < len(arr) and v == arr[i]:
    #             i += 1
    #         else:
    #             k -= 1
    #         v += 1
    #     return v-1

    # # iterative way,  O(logn)
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     lo, hi = 0, len(arr) - 1
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         miss = arr[mid] - mid - 1   # how many numbers are missing at left of mid
    #         if k <= miss:
    #             hi = mid
    #         else:
    #             lo = mid + 1
    #     miss = arr[lo] - lo - 1   # lo and hi meet in one cell
    #     if k <= miss:  # towards left of mid
    #         return arr[lo] - (miss - k) - 1
    #     else:
    #         return arr[lo] + (k - miss)
        
    # @DBabichev (awesome solution and explanation)
    def findKthPositive(self, arr, k):
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k
