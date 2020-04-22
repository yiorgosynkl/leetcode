################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200422
# Problem link      : https://leetcode.com/problems/subarray-sum-equals-k/
################################################################

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        his = { 0 : 1 }
        ssum = 0
        for num in nums:
            ssum += num          
            if ssum - k in his:
                res += his[ssum - k]
            if ssum in his:
                his[ssum] += 1
            else:
                his[ssum] = 1
        return res
    
    # awice
    # def subarraySum(self, A, K):
    #     count = collections.Counter()
    #     count[0] = 1
    #     ans = su = 0
    #     for x in A:
    #         su += x
    #         ans += count[su-K]
    #         count[su] += 1
    #     return ans
    
    # lee215
    # def subarraySum(self, nums, k):
    #     count, cur, res = {0: 1}, 0, 0
    #     for v in nums:
    #         cur += v
    #         res += count.get(cur - k, 0)
    #         count[cur] = count.get(cur, 0) + 1
    #     return res
        
    # my brute force
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     for key, val in cnt.items():
    #         if key == k:
    #             res += val
    #         elif key < k and k + key in cnt:
    #             res += val * cnt[k + key]
    #     return res
