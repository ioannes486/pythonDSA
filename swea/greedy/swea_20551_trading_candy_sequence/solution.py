import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def solve(A, B, C):
    result = 0
    if C < 3 or B < 2 or A < 1:
        return -1

    if B >= C:
        result += B - (C-1)
        B = C-1

    if A >= B:
        result += A - (B-1)


    return result


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    A, B, C = map(int,input().split())


    # 출력
    print(f"#{test_case} {solve(A, B, C)}")