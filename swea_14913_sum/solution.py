import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수 N, 배열크기(100)

- 변수 arr

- 조건 
- 배열의 크기는 100 바이 100
각 행의 값은 float('-inf') 보다 아래임
동일한 최대값이 있을 경우 하나의 값만 출력한다

- 제약사항

- 구하는 값
가로합, 세로 합, 직선합 중에 최댓값

가로합이랑 세로합은 상수니깐 미리 구해놓자
"""

def solve(arr):
    # 변수 초기화
    # 대각 합 두개
    trace_sum_left_to_right = 0
    trace_sum_right_to_left = 0

    # 수직, 수평합
    vertical_sum = -float('inf')
    horizontal_sum = -float('inf')

    # 대각합 구하기
    for i in range(100):
        trace_sum_left_to_right += arr[i][i]
        trace_sum_right_to_left += arr[i][100-1-i]

    # 수직 , 수평합 구하기
    # 1. 수평합 구하기
    for i in range(100):
        temporal_horizontal_sum = 0
        for j in range(100):
            temporal_horizontal_sum += arr[i][j]
        if horizontal_sum < temporal_horizontal_sum:
            horizontal_sum = temporal_horizontal_sum

    # 2. 수직합 구하기
    for i in range(100):
        temporal_vertical_sum = 0
        for j in range(100):
            temporal_vertical_sum += arr[j][i]
        if vertical_sum < temporal_vertical_sum:
            vertical_sum = temporal_vertical_sum

    # 3. 다 모아서 최댓값 구하기
    max_sum = trace_sum_left_to_right
    for value in (trace_sum_right_to_left, vertical_sum, horizontal_sum):
        if max_sum < value:
            max_sum = value

    return max_sum


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    arr = [list(map(int, input().split())) for _ in range(100)]



    # 출력
    print(f"#{test_case} {solve(arr)}")