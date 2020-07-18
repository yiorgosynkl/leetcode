################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200717
# Problem link      : https://leetcode.com/problems/top-k-frequent-elements/
################################################################

from collections import defaultdict
from collections import Counter

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     return sorted(list(set(nums)), key = lambda x: nums.count(x), reverse = True)[:k]
    
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     c = defaultdict(int)
    #     for num in nums:
    #         c[num] += 1
    #     return [key for key, val in sorted(c.items(), key=lambda item: item[1], reverse=True)][:k]

    # @leetcode    
    # https://leetcode.com/articles/top-k-frequent-elements/    
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
    #     # O(1) time 
    #     if k == len(nums):
    #         return nums
        
    #     # 1. build hash map : character and how often it appears
    #     # O(N) time
    #     count = Counter(nums)   
    #     # 2-3. build heap of top k frequent elements and
    #     # convert it into an output array
    #     # O(N log k) time
    #     return heapq.nlargest(k, count.keys(), key=count.get) 
    