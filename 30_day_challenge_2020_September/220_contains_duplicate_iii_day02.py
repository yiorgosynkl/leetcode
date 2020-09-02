################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200902
# Problem link      : https://leetcode.com/problems/contains-duplicate-iii/
################################################################

import bisect
from collections import deque
from sortedcontainers import SortedList

class Solution:
    # O(n*k)
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(i+1, min(len(nums),i+k+1)):
    #             if abs(nums[i]-nums[j]) <= t:
    #                 return True
    #     return False

    # O(n logk)
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     s = [] # sorted subset of nums
    #     q = deque()
    #     for num in nums:
    #         if len(q) == k+1: 
    #             del s[bisect.bisect_left(s, q.popleft())]
    #         q.append(num)
    #         bisect.insort_left(s, num)
    #         add_idx = bisect.bisect_left(s, num)
    #         if (add_idx > 0 and num - s[add_idx-1] <= t) or (add_idx < len(s) - 1 and s[add_idx+1] - num <= t): return True
    #     return False
    
    # ordered dictionary, bucket sort
    # def containsNearbyAlmostDuplicate(self, nums, k, t):
    #     if k < 1 or t < 0:
    #         return False
    #     dic = collections.OrderedDict()
    #     for n in nums:
    #         key = n if not t else n // t
    #         for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
    #             if m is not None and abs(n - m) <= t:
    #                 return True
    #         if len(dic) == k:
    #             dic.popitem(False)
    #         dic[key] = n
    #     return False

    # sorted list @DBabichev
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        slist = SortedList()
        for i in range(len(nums)):
            if i > k: slist.remove(nums[i-k-1])   
            pos1 = bisect_left(slist, nums[i] - t)
            pos2 = bisect_right(slist, nums[i] + t)
            if pos1 != pos2: return True
            slist.add(nums[i])
        return False

# We are searching for a data structure that holds k elements sorted, while removing or adding new elements has logk complexity. 
# This can be done with sorted list or bisect in python.
# bucket sorting with ordered dictionary is even quicker
