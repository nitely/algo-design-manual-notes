# -*- coding: utf-8 -*-

# runtime O(log n)


def find_index(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == mid+1:  # 1-index based
            return mid+1
        elif arr[mid] > mid+1:
            high = mid-1
        else:
            low = mid+1
    return -1

# 3
print(find_index(
    [-10, -3, 3, 5, 7, 8]
))

# -1
print(find_index(
    [2,3,4,5,6,7]
))

# 1
print(find_index(
    [1,5,6,7]
))

# 6
print(find_index(
    [0,1,2,3,4,6]
))
