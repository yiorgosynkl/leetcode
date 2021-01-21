################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210121
# Problem link      : https://leetcode.com/problems/find-the-most-competitive-subsequence/
################################################################

class Solution:
    # # time: O(n*k)
    # def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    #     lo, hi = 0, len(nums) - k + 1
    #     ans = []
    #     while hi <= len(nums):
    #         x = min(nums[lo:hi])
    #         ans.append(x)
    #         lo = nums.index(x) + 1
    #         hi += 1
    #     return ans
        
    # def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    #     ans = []
    #     while k > 0:
    #         x = min(nums[:len(nums)-k+1])
    #         ans.append(x)
    #         nums = nums[nums.index(x)+1:]
    #         k -= 1
    #     return ans

    # @lee215, mono increasing stack
    def mostCompetitive(self, nums, k):
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and len(stack) - 1 + len(nums) - i >= k: # pop if nums in stack (len(stack)) and nums left to check (len(nums) - i) should be more than k
                stack.pop()
            if len(stack) < k:
                stack.append(n)
        return stack
    
    # # @DBabichev
    # def mostCompetitive(self, nums, k):
    #     attempts = len(nums) - k # you can at most remove so many elements to make it better
    #     stack = []
    #     for num in nums:
    #         while stack and num < stack[-1] and attempts > 0:
    #             stack.pop()
    #             attempts -= 1
    #         stack.append(num)
    #     return stack[:k]