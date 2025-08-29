import sys

sys.stdin = open("input.txt", "r")


def trace_sum(N, arr):

    # 맨 가운데에서 시작해보자
    i = 2
    j = 2

    # 변수 초기화
    result = arr[i][j]

    # di, dj설정
    di = [1, -1, 1, -1]
    dj = [1, 1, -1, -1]

    # 순회하면서 더하기
    for repeat in range(1, 3):  # 팔 길이가 2임으로 인덱스는 1,2
        for d in range(4):
            ni = i + (di[d] * repeat)
            nj = j + (dj[d] * repeat)
            result += arr[ni][nj]

    return result


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{test_case} {trace_sum(N, arr)}")
