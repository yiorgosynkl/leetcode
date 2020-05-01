# class Solution:
#     def countElements(self, arr: List[int]) -> int:
#         nums = defaultdict(list)
#         for i in arr:
#             if i in nums.keys(): nums[i] += 1
#             else: nums[i] = 1
#         res = 0
#         for num, times in nums.items():
#             if num + 1 in nums.keys():
#                 res += times
#         return res

class Solution:
    def countElements(self, arr: List[int]) -> int:
        x = set(arr)
        return sum([1 for i in arr if i+1 in x])
 