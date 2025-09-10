import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    low = [x for x in arr[1:] if x <= pivot]
    high = [x for x in arr[1:] if x > pivot]

    return quick_sort(low) + [pivot] + quick_sort(high)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    array = list(map(int, input().split()))

    sorted_array = quick_sort(array)

    result = sorted_array[N // 2]
    # 출력
    print(f"#{test_case} {result}")