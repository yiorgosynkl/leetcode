def binary_search(nums, lo, hi, target):
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# def binary_search_recursive(nums, lo, hi, target):
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target: 
#             binary_search_recursive(nums, mid + 1, hi, target)
#         else:
#             binary_search_recursive(nums, lo, mid - 1, target)
#     return -1

def binary_search_all(nums, target):
    return binary_search(nums, 0, len(nums) - 1, target)
