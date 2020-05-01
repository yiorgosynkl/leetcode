class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        x = { 0: -1 } # key: count -> val: first time index
        count = 0
        res = 0
        for i in range(0, len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count not in x:
                x[count] = i
            else:
                res = max(res, i - x[count])
        return res

#  O(n^2)        
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         res = 0
#         for i in range(1, len(nums)):
#             times = [0,0] # zeros and ones
#             for i in range(i, -1, -1):
#                 times[nums[i]] += 1
#                 if times[0] == times[1]:
#                     res = max(res, times[0] * 2)
#         return res
