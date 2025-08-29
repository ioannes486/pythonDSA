import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    8 : 생성해야 할 암호 자리수
- 변수
    N : 처리 할 숫자 수
- 조건(제약사항)
    숫자가 감소할 때 0보다 작아지는 경우는 0으로 유지된다
    1개의 사이클이 끝나면 다시 1부터 감소한다.
- 구하는 값
    8자리 숫자암호
- 아이디어
    피자랑 똑같네
    마지막으로 뺄쌤 연산을 수행하고 0이 되면 그 원소를 옮긴 다음 암호 출력하기
"""


def solve(arr, N):

    cycle_count = 1

    front = 0
    rear = N - 1
    while True:

        if cycle_count == 6:
            cycle_count = 1

        # 뺄셈 연산하기
        arr[front] = arr[front] - cycle_count

        #  큐의 가장 첫 원소를 두번째 원소로, 가장 마지막 원소를 첫번째 원소로
        front = (front + 1) % N
        rear = (rear + 1) % N

        if arr[rear] <= 0:
            arr[rear] = 0
            result = ""
            for i in range(N):
                result += str(arr[(i + front) % N])
                result += " "
            return result.rstrip()

        # 한 사이클을 돌면 사이클 초기화
        cycle_count += 1


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    tc = int(input())
    arr = list(map(int, input().split()))
    N = 8

    # 출력
    print(f"#{tc} {solve(arr, N)}")
