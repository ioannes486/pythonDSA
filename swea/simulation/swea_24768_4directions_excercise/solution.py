import sys

sys.stdin = open("input.txt", "r")


def solve(N, arr):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total_abs_sum = 0
    for i in range(N):
        for j in range(N):
            abs_sum = 0
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    target = arr[i][j] - arr[ni][nj]
                    if target >= 0:
                        abs_sum += target
                    else:
                        abs_sum -= target
            total_abs_sum += abs_sum

    return total_abs_sum


T = int(input())
for test_case in range(1, T + 1):
    # 입출력 받기
    N = int(input())

    # 배열 받기
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{test_case} {solve(N, arr)}")
