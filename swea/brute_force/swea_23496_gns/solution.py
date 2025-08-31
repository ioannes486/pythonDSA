import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
- 변수
    N:테스트케이스의 길이
    
- 조건(제약사항)
    작은 수부터 차례로 정렬하여 출력하라

- 구하는 값

- 아이디어
"""


def solve():

    return


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    reference = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    N = int(input())
    arr = list(input().split())

    cnt_arr = [0] * 10
    for i in range(N):
        item = arr[i]

        # 순차탐색
        idx = 0
        for j in range(10):
            if reference[i] == item:
                idx = j
                break

    cnt_arr[idx] += 1

    # temp = [0]*N

    # for number in cnt_arr:
    #     temp[number]

    # 출력
    print(f"#{test_case} {cnt_arr}")
