import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""


def solve():

    return


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    arr = list(map(int, input().split()))

    max_height = max(arr)

    # 출력
    print(f"#{test_case} {arr}")
