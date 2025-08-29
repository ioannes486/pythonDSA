import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    A: 기지국 : 1칸
    B: 기지국 : 2칸
    C: 기지국 : 3칸
    
- 변수

- 조건(제약사항)
    3가지 종류의 기지국 수 : 각각 1칸, 2칸,3칸을 커버합
    기지국이 있는 곳에 집이 있진 않는듯
    1개의 집은 1개의 셀에 있다
- 구하는 값
    기지국에 커버되지 않는 집의 수
- 아이디어
    집의 총 수에서 기지국에서 커버하는 수 뺴기
    기지국이 커버하는 범위는 Y로 바꾸기, 커버하는 영역에 기지국이 있으면 바꾸지 않기
"""

station_coverages = {
    "A": 1,
    "B": 2,
    "C": 3,
}

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def solve(N, arr):
    home_count = 0

    for i in range(N):
        for j in range(N):
            location_category = arr[i][j]
            if location_category in "ABC":
                coverage = station_coverages[location_category]
                for n in range(1, coverage + 1):
                    for k in range(4):
                        ni = i + n * di[k]
                        nj = j + n * dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == "H":
                                arr[ni][nj] = "Y"

    for i in range(N):
        for j in range(N):
            if arr[i][j] == "H":
                home_count += 1

    return home_count


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 출력
    print(f"#{test_case} {solve(N, arr)}")
