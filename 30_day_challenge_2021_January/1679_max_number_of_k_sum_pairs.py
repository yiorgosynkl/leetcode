################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210118
# Problem link      : https://leetcode.com/problems/max-number-of-k-sum-pairs/
################################################################

from collections import defaultdict, Counter

class Solution:
    # time: O(n)
    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     seen, ans = {}, 0
    #     for n in nums:
    #         if k - n in seen.keys() and seen[k-n] > 0:
    #             seen[k-n] -= 1
    #             ans += 1
    #         else:
    #             seen[n] = seen.get(n, 0) + 1
    #     return ans
    # # with defaultdict, time: O(n)
    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     d, res = defaultdict(int), 0
    #     for num in nums:
    #         if d[k - num] > 0:
    #             d[k - num] -= 1
    #             res += 1
    #         else:
    #             d[num] += 1
    #     return res
    
    # @DBabichev with Counter, time: O(n)
    def maxOperations(self, nums, k):
        cnt, ans = Counter(nums), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans//2
    
    # def maxOperations(self, nums, k):
    #     c = Counter(nums)
    #     return sum(min(c[k-n], c[n]) for n in c.keys()) >> 1
    
    # # O(nlogn) 2 pointers
    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     i, j = 0, len(nums)-1
    #     res = 0
    #     while(i<j):
    #         summ = nums[i]+nums[j]
    #         if(summ == k):
    #             i+=1
    #             j-=1
    #             res+=1
    #         elif(summ < k):
    #             i+=1
    #         else:
    #             j-=1
    #     return res