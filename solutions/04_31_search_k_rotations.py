# -*- coding: utf-8 -*-

# runtime O(log n)
# space O(1)

# XXX return index + 1 for the rotations, instead of the largest
#     could also find the smallest num
def find_largest_num(arr):
    #if arr[0] < arr[-1]:
    #    return arr[-1]
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:  # must be in right side
            if arr[mid+1] < arr[mid]:  # is it the middle the largest?
                return arr[mid]
            low = mid+1 # skip middle, we just checked it's not it
        else:
            if arr[mid-1] > arr[mid]:
                return arr[mid-1]
            high = mid-1


print(find_largest_num(
    [1,2,4,7,9,10,15,19]
))
# k = 2 rotations
print(find_largest_num(
    [15,19,1,2,4,7,9,10]
))
# k = 6 rotations
print(find_largest_num(
    [4,7,9,10,15,19,1,2]
))
# k = 4, middle
print(find_largest_num(
    [9,10,15,19,1,2,4,7]
))
print(find_largest_num(
    [19,1,2,4,7,9,10,15]
))
print(find_largest_num(
    [19,1,2,4,7,9,10,15,16]
))
