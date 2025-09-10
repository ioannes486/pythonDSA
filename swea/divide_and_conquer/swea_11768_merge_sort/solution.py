import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어

    병합과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수는 언제 발생하나?
    
"""


def merge(left, right):
    global cnt
    left_length = len(left)
    right_length = len(right)

    if left[left_length-1] > right[right_length-1]:
        cnt += 1

    result = [0] * (left_length + right_length)
    l = r = 0

    while l < left_length and r < right_length:
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < left_length:
        result[l + r] = left[l]
        l += 1

    while r < right_length:
        result[l + r] = right[r]
        r += 1

    return result




def merge_sort(target_list):
    list_length = len(target_list)
    if len(target_list) == 1:
        return target_list

    # 1. 왼쪽 오른쪽을 분할하기
    mid  = list_length // 2
    left = target_list[:mid]
    right = target_list[mid:]

    # 2. 다음 단계도 왼쪽, 오른쪽 분할하기
    next_left = merge_sort(left)
    next_right = merge_sort(right)

    return merge(next_left, next_right)


    # 3.N이 1일때부터 하기




T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_list = merge_sort(arr)
    # 출력
    print(f"#{test_case} {sorted_list[N//2]} {cnt}")