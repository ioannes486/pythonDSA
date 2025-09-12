import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
1. 부분집합 코드 복습하기
"""

def get_sub(tar):

    cnt = 0
    for i in range(N):
        if tar & 0x1:
            cnt += arr[i]
        tar >>= 1

    return cnt

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))

    # 1. 비트마스크를 이용한 부분집합 구현하기
    result = 0
    for target in range(1 << N):
        total = get_sub(target)
        if total == K:
            result += 1


    # 출력
    print(f"#{test_case} {result}")