# -*- coding: utf-8 -*-

# runtime O(2n) = O(n)
# one pass to separate red,
# a second pass to separate white,
# done

R, W, B = range(3)

def dutch_flag(arr):
    first_high = 0
    for p in (W, B):  # order matters
        # same as quick-sort partition
        for i in range(first_high, len(arr)):
            if arr[i] < p:
                arr[i], arr[first_high] = arr[first_high], arr[i]
                first_high += 1
    return arr


print(dutch_flag([
    R, W, B, R, R, W, B, W, R, W, B, B, R
]))
# Expected RRRRWWWWBBBB
