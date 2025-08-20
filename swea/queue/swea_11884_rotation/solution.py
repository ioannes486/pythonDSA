import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N : 수열의 크기
    M : 회전의 수
- 조건(제약사항)

- 구하는 값
    M번 회전했을 때 수열의 맨 앞에 있는 숫자 출력하기
- 아이디어
"""


def solve(N, M, arr):
    front = -1
    rear = N-1

    for _ in range(M):
        front = (front + 1) % N
        temp = arr[front] # dequeue

        rear = (rear + 1) % N
        arr[rear] = temp

        arr[rear]

    return arr[front + 1]


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 출력
    print(f"#{test_case} {solve(N, M, arr)}")