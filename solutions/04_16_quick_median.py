# -*- coding: utf-8 -*-

# runtime O(n) average (but n^2 worst)
# use quicksort method but find median in one partition only
# making this n + n/2 + n/4 + n/8... = 2n = n


# DOES NOT WORK


def partition(arr, low, high):
    # at the end i == high, and first_high is the divisor
    # between lesser and greater than p
    p = high
    first_high = low
    for i in range(low, high):
        # put lesser to the left of first_high
        if arr[i] < arr[p]:
            arr[i], arr[first_high] = arr[first_high], arr[i]
            first_high += 1
    arr[p], arr[first_high] = arr[first_high], arr[p]
    return first_high


def _quick_median(arr, low, high, k):
    if low < high:
        return
    p = partition(arr, low, high)
    if high-p == k-1:
        print(arr[p])
    if high-p >= k:
        _quick_median(arr, p + 1, high, k)
    else:
        _quick_median(arr, low, p - 1, k-(high-p))


def quick_median(arr):
    # XXX this is Kth largest element
    _quick_median(arr, 0, len(arr)-1, len(arr) / 2)
    return arr


def _quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        _quick_sort(arr, low, p-1)
        _quick_sort(arr, p+1, high)


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr)-1)
    return arr


print(quick_median(
    [8,7,3,9,23,9,4,7,34,2,2,3,4,5,0,1,-1,123,865,234,87]))
