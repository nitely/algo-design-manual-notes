# -*- coding: utf-8 -*-

# runtime O(log n + log m)

def find_num(matrix, x):
    assert matrix
    assert matrix[-1][-1] >= x
    assert matrix[0][0] <= x

    # Find row
    row = -1
    low = 0
    high = len(matrix)-1  # num of rows
    while low <= high:
        mid = (low+high)//2
        if matrix[mid][0] > x:  # before row
            high = mid-1
        elif matrix[mid][0] <= x and matrix[mid][-1] >= x:
            row = mid
            break
        else:  # after row
            assert matrix[mid][-1] < x
            low = mid+1
    assert row >= 0, "Not found"
    # Find column in row
    column = -1
    low = 0
    high = len(matrix[0])-1
    while low <= high:
        mid = (low+high)//2
        if matrix[row][mid] == x:
            column = mid
            break
        elif matrix[row][mid] < x:
            low = mid+1
        else:
            high = mid-1
    assert column >= 0, "Not found"
    return (row, column)

print(find_num([
    [11,12,13,15,16,18,19],
    [20,21,22,23,25,26,27],
    [33,35,37,38,39,98,99]
], 20))
