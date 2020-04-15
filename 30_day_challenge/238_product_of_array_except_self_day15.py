class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        length = len(nums)
        left = [None] * length
        right = [None] * length
        res = [None] * length
        for i in range(0, length):
            prod *= nums[i]
            left[i] = prod
        prod = 1
        for i in reversed(range(length)):
            prod *= nums[i]
            right[i] = prod
        res[0] = right[1]
        res[length - 1] = left[length - 2]
        for i in range(1, length - 1):
            res[i] = left[i - 1] * right[i + 1]
        return res

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = [1 for _ in nums]

#         left = 1
#         right = 1
        
#         for i in range(len(nums)):
#             ans[i] *= left
#             ans[-1-i] *= right
#             left *= nums[i]
#             right *= nums[-1-i]
        
#         return ans

# from functools import reduce
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prod = reduce(lambda a,b: a*b, nums)
#         return list(map(lambda a: prod // a, nums))