# oneliner
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)

# first solution
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         myset = set()
#         for num in nums:
#             if num in myset:
#                 myset.remove(num)
#             else:
#                 myset.add(num)
#         print(myset)
#         return myset.pop() 