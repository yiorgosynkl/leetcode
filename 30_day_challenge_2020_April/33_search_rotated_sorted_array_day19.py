################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200419
# Problem link      : https://leetcode.com/problems/search-in-rotated-sorted-array/
################################################################


def binSearch(nums, target):
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    if nums[left] == target: # boundary conditions
        return left
    elif target < nums[left]:
        return -1
    if nums[right] == target:
        return right
    elif nums[right] < target:
        return -1
    mid = (left + right) // 2 # start search
    while left < mid:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    return -1

def findPivot(nums):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2 # start search
    while left < mid:
        if nums[mid] < nums[left]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2
    return right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1 or nums[0] < nums[-1]:
            return binSearch(nums, target)
        pivot = findPivot(nums) # start of original array
        if pivot and target > nums[-1]:
            ans = binSearch(nums[:pivot], target)
        else:
            ans = binSearch(nums[pivot:], target)
            if not ans == -1:
                ans += pivot
        return ans

    # cleaner solution
    def search(self, nums: List[int], target: int) -> int:
        # find pivot and return the original sorted array
        def sortBack(nums):
            le, ri = 0, len(nums) - 1
            while le < ri: # find index of smallest num, and rotate back to original array
                mid = (le + ri) // 2 
                if nums[mid] <= nums[ri]: # = is important because of duplicates (move right pointer as far left as possible)
                    ri = mid
                else: # nums[mid] > nums[le]
                    le = mid + 1
            return nums[le:] + nums[:le], le
        # binary search for if target exists
        def binSearch(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1
        nums, rot = sortBack(nums) # sorted nums and rotation distance
        ans = binSearch(nums, target)
        return (ans + rot) % len(nums) if ans >= 0 else -1



# ------------------ idea nubmer 1 -----------------------

# Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
# [12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
# If target is let's say 7, then we adjust nums to this:
# [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# And then we can simply do ordinary binary search. Actually we adjust elements on the fly only
# If nums[mid] and target are "on the same side" of nums[0], 
# we just take nums[mid]. Otherwise we use -infinity or +infinity as needed.   

# def search(self, nums, target):
#         lo, hi = 0, len(nums)

#         while lo < hi:
#             mid = (lo + hi) / 2
            
#             if (nums[mid] < nums[0]) == ( target < nums[0]):
#                 if (nums[mid] < target):
#                     lo = mid + 1
#                 elif (nums[mid] > target):
#                     hi = mid
#                 else:
#                     return mid
#             elif target < nums[0]:
#                 lo = mid + 1
#             else:
#                 hi = mid

#         return -1

# smaller if else
# double num = (nums[mid] < nums[0]) == (target < nums[0])
#            ? nums[mid]
#            : target < nums[0] ? -INFINITY : INFINITY;


# ------------------ idea nubmer 2 -----------------------

# def search(self, nums, target):
#     lo, hi = 0, len(nums) - 1
#     while lo < hi:
#         mid = (lo + hi) / 2
#         if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
#             lo = mid + 1
#         else:
#             hi = mid
#     return lo if target in nums[lo:lo+1] else -1

# and Python using bisect
# class Solution:
#     def search(self, nums, target):
#         self.__getitem__ = lambda i: \
#             (nums[0] <= target) ^ (nums[0] > nums[i]) ^ (target > nums[i])
#         i = bisect.bisect_left(self, True, 0, len(nums))
#         return i if target in nums[i:i+1] else -1

# Remember the array is sorted, except it might drop at one point.

# If nums[0] <= nums[i], then nums[0..i] is sorted (in case of "==" it's just one element, 
# and in case of "<" there must be a drop elsewhere). So we should keep searching 
# in nums[0..i] if the target lies in this sorted range, i.e., if nums[0] <= target <= nums[i].

# If nums[i] < nums[0], then nums[0..i] contains a drop, and thus nums[i+1..end] is sorted 
# and lies strictly between nums[i] and nums[0]. So we should keep searching in nums[0..i] 
# if the target doesn't lie strictly between them, 
# i.e., if target <= nums[i] < nums[0] or nums[i] < nums[0] <= target

# Those three cases look cyclic:

#     nums[0] <= target <= nums[i]
#                target <= nums[i] < nums[0]
#                          nums[i] < nums[0] <= target
