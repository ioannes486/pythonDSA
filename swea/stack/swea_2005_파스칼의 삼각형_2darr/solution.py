import sys

sys.stdin = open("input.txt", "r")
SIZE = 11

memo = [[0] * SIZE for _ in range(SIZE)]

for i in range(SIZE):
    for j in range(i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    # 출력
    print(f"#{test_case}")
    for i in range(N):
        for j in range(i + 1):
            print(memo[i][j], end=" ")
