arr = [1,6,4,7,54,37,4,5,3]


def apart(left, right):
    pivot = arr[left]
    i,j = left+1, right
    while i <= j:
        while pivot >= arr[i] and i <= j:
            i += 1

        while pivot <= arr[j] and i <= j:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = apart(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr)-1)

print(arr)