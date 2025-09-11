from collections import deque

arr = [1,6,4,7,54,37,4,5,3]

def merge(left, right):
    result_length = len(left) + len(right)
    result = [0] * result_length

    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1


    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1
    return result

# def merge(left, right):
#     result = []
#     left = deque(left)
#     right = deque(right)
#
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.popleft())
#         else:
#             result.append(right.popleft())
#
#     if left:
#         result += left
#
#     if right:
#         result += right
#
#     return result
#

def merge_sort(arr):
    arr_length = len(arr)

    if arr_length < 2:
        return arr

    mid = arr_length //2

    left = arr[:mid]
    right = arr[mid:]

    next_left = merge_sort(left)
    next_right = merge_sort(right)

    return merge(next_left, next_right)

soreted_arr = merge_sort(arr)

print(soreted_arr)