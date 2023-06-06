# -*- coding: utf-8 -*-

# see https://leetcode.com/problems/4sum/, for the same solution
# but skipping duplicated sub-arrays

# runtime O(n^(k-1) + n*log(n))
# space O(n^(k-1)) (because it returns the sets)

# two-pointer solution
def two_sum(arr, t):
    arr.sort()
    result = []
    i = 0
    j = len(arr)-1
    while i < j:
        tt = arr[i] + arr[j]
        if tt == t:
            result.append([arr[i], arr[j]])
        if tt <= t:
            i += 1
        if tt >= t:
            j -= 1
    return result

# this is basically fixing numbers and shrinking the array
def _k_sum(arr, k, t, i, partial, result):
    assert k >= 2
    if k == 2:
        for pairs in two_sum(arr[i:], t):
            result.append(partial + pairs)
        return
    # O(n^(k-1)) crap, the "- 1" is because two_sum is O(n) instead of O(n^2)
    for i in range(i, len(arr)):
        _k_sum(arr, k - 1, t - arr[i], i + 1, partial + [arr[i]], result)

def k_sum(arr, k, t):
    assert k >= 2
    arr.sort()
    result = []
    _k_sum(arr, k, t, 0, [], result)
    return result

# 2, 7
print(two_sum([2, 7, 11, 15], 9))
print(k_sum([2, 7, 11, 15], 2, 9))
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
print(k_sum([-1, 0, 1, 2, -1, -4], 3, 0))
