# partition with last element as pivot 
def partition(nums, lo, hi):
    pivot = nums[hi]
    e = lo # enter pivot index
    for i in range(lo, hi):
        if nums[i] < pivot:
            nums[e], nums[i] = nums[i], nums[e] # swap 
            e += 1
    nums[e], nums[hi] = nums[hi], nums[e] # swap
    print(nums)
    return e

# find the k-th smallest element (0-index)
def quickselect(nums, lo, hi, k):
    e = partition(nums, lo, hi)
    if k == e:
        return nums[e]
    elif k < e:
        return quickselect(nums, lo, e - 1, k)
    else:
        return quickselect(nums, e + 1, hi, k)

# nums array is passed by reference
# it changes during partition and used for the next quickselect
