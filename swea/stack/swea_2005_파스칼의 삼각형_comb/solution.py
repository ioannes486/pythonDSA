import sys
from math import comb

sys.stdin = open("input.txt", "r")


def solve(N):
    for i in range(N):
        for j in range(i + 1):
            print(comb(i, j), end=" ")
        print()


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    # 출력
    print(f"#{test_case}")
    solve(N)
