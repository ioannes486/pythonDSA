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
    result = 0

    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = 1
    while idx < N:
        for i in range(idx):
            if(arr[i][0] > arr[idx][0] and arr[i][1] < arr[idx][1]) or (arr[i][0] < arr[idx][0] and arr[i][1] > arr[idx][1]):
                result += 1
        idx += 1


    # 출력
    print(f"#{test_case} {result}")