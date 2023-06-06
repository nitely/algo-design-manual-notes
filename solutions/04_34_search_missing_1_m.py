# -*- coding: utf-8 -*-

# runtime O(log n)


# assumes array starts with value 1
# otherwise the first missing is 1
# also assumes a value is missing
# otherwise the first missing is n+1
def find_hole2(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == mid+1:
            assert mid+1 < len(arr), "no holes?"
            if arr[mid+1] > mid+2:
                return mid+2
            low = mid+1
        else:
            # "<" can't happen because it would
            # imply duplicates or starting with
            # a value lesser than 1
            assert arr[mid] > mid+1
            if arr[mid-1] == mid:
                return mid+1
            high = mid-1


# finds the non-existing number between two numbers
# shrinking each side each time [1 (2) 3]
#
# * at the end high is always lesser than low,
#   meaning high needs +2 while low needs +1 (next the hole)
def find_hole(arr):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] > mid + 1:
            h = mid - 1
        elif arr[mid] <= mid + 1:  # < cant happen really
            l = mid + 1
    return l + 1  # or h+2


# 5
print(find_hole(
    [1,2,3,4,6,7,8]
))

# 2
print(find_hole(
    [1,3,4,6,7,8]
))

# 2
print(find_hole(
    [1,4,6,7,8]
))

# 4
print(find_hole(
    [1,2,3,5,6,8]
))

# 5
print(find_hole(
    [1,2,3,4,6,8]
))

# 7
print(find_hole(
    [1,2,3,4,5,6,8]
))
