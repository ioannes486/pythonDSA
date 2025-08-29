import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    배열의 길이 N
- 변수
    집합의 원소들
- 조건(제약사항)

- 구하는 값
    합이 존재하면 0, 합이 존재하지 않으면 1
- 아이디어
"""


def solve(N, arr):  #
    # 모든 부분집합 구하기
    for i in range(1, 1 << N):
        temp_sum = 0
        for j in range(N):
            if i & (1 << j):
                # 합을 다 더해보기
                temp_sum += arr[j]
        # 합을 구했을 때 0이면 1반환
        if temp_sum == 0:
            return 1
    # 못 구했으면 0 반환
    return 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))
    # 출력
    print(f"#{test_case} {solve(N, arr)}")
