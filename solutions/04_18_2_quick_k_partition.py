# -*- coding: utf-8 -*-

# runtime O(n)

# Put numbers lesser than k before k
# and greater after k, output order does not matter
# (otherwise it would be a sort)
# this is not in Skiena book, but it's very similar to
# the dutch flags problem

# no dup support
def k_partition(arr, k):
    p = k
    first_high = 0
    for i in range(len(arr)):
        # assumes there are no k dups,
        # otherwise we could
        # increase a first_k and put them
        # at the end then use two-pointers
        # to reverse the right side
        if arr[i] == p:
            arr[i], arr[-1] = arr[-1], arr[i]
        if arr[i] < p:
            arr[i], arr[first_high] = arr[first_high], arr[i]
            first_high += 1
    arr[-1], arr[first_high] = arr[first_high], arr[-1]
    return arr


# two passes:
# put lesser than k to the left
# put equal to k to the end of left (middle)
def k_partition_dup(arr, k):
    p = k
    first_high = 0
    for i in range(len(arr)):
        if arr[i] < p:
            arr[i], arr[first_high] = arr[first_high], arr[i]
            first_high += 1
    for i in range(first_high, len(arr)):
        if arr[i] == p:
            arr[i], arr[first_high] = arr[first_high], arr[i]
            first_high += 1
    return arr


# same as dutch flags ;)
def k_partition_dup_v2(arr, k):
    first_high = 0
    # put lesser than k to the left
    # put lesser than k+1 meaning k to the left
    for p in (k, k+1):
        for i in range(first_high, len(arr)):
            if arr[i] < p:
                arr[i], arr[first_high] = arr[first_high], arr[i]
                first_high += 1
    return arr


print(k_partition([
    2,1,9,3,6,-2,4,7,-1
], 4))


print(k_partition_dup([
    2,1,4,9,3,6,-2,4,4,7,-1,4
], 4))
