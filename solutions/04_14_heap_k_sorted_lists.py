# -*- coding: utf-8 -*-

# runtime O(n*log(k)), where n is the
# len of all lists put together and
# k is the number of lists.
# heap push is log(k) in the number of lists.
# space O(n)

# The input lists are assumed to be sorted.
# Using heapq.merge() would make the runtime
# n + n*log(n) = 2n*log(n) = n*log(n)

# This solution works even if the lists don't fit in memory,
# they could be streams of data, and the result as well.

import heapq


def k_sort(k_lists):
    result = []
    heap = []
    heads = [0 for _ in k_lists]
    for i, kl in enumerate(k_lists):
        heapq.heappush(heap, (kl[0], i))
    while heap:
        n, i = heapq.heappop(heap)
        heads[i] += 1
        result.append(n)
        if heads[i] < len(k_lists[i]):
            heapq.heappush(heap, (k_lists[i][heads[i]], i))
    return result


print(k_sort([
    list(sorted([1,6,7,3,7,5,3,9,3,9,3,1,2,123,34,23])),
    list(sorted([5345,7,347,3,6,85,4523,7,55,672,9,98])),
    list(sorted([8,7,3,9,23,9,4,7,34,2,2,3,4,5,0,1,-1,123,865,234,87])),
]))
