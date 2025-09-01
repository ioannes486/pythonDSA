import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N 배열의 크기 3이상 10이하
- 조건(제약사항)
    같은 행에서는 하나의 숫자만 고를 수 있다.
- 구하는 값

- 아이디어
"""
def perm(level, cursum):
    global mini
    if cursum > mini:
        return

    if level == N:
        mini = min(mini, cursum)
        return
    else:
        for i in range(level, N):
            order[i], order[level] = order[level], order[i]
            perm(level+1, cursum + arr[order[level]][level])
            order[i], order[level] = order[level], order[i]

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    order = [i for i in range(N)]
    mini = 10 * N
    perm(0, 0)

    # 출력
    print(f"#{test_case} {mini}")