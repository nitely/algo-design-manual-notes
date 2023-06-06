# -*- coding: utf-8 -*-

# rearrange an array of n keys
# so that all the negative keys
# precede all the non-negative keys.

# runtime O(n)
# space O(1)
# it's stable: rearrange the elements in seen order

def rearrange(arr):
    # quick sort partition
    pv = 0
    first_high = 0
    for i in range(len(arr)):
        if arr[i] < pv:
            arr[i], arr[first_high] = arr[first_high], arr[i]
            first_high += 1
    return arr


print(rearrange([
    1,24,54,7,2,-1,4,-3,5,-56,-2,6,-123,542, 0, 1
]))
