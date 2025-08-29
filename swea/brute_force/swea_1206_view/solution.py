import sys

sys.stdin = open("sample_input.txt", "r")

"""TODO:
조건 : 양쪽 거리 2 이상의 공간이 확보 될때 조망권이 확보된다.
요구사항 : 조망권이 확보된 세대의 수를 반환
제약 : 0 <= N <=1000
건물높이 : <= 255
맨 왼쪽 두칸과 맨 오른쪽 두 칸은 건물높이가 항상 0이다. index 2 to N-3


"""


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


def my_max(*args):
    max_val = args[0]
    for arg in args:
        if arg > max_val:
            max_val = arg
    return max_val


def solve(N, arr):
    total_cnt = 0
    for i in range(2, N - 2):
        value1 = arr[i - 2]
        value2 = arr[i - 1]
        value3 = arr[i + 1]
        value4 = arr[i + 2]
        cnt = arr[i] - my_max(value1, value2, value3, value4)
        if cnt >= 0:
            total_cnt += cnt
    return total_cnt


for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f"#{test_case} {solve(N, arr)}")
