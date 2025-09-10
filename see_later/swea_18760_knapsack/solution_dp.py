import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N: 물건의 개수
    K: 물건의 총 무게
- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def recur(idx, weight, value):
    global result


    if idx > N:
        return
    if weight > K:
        return

    if idx == N:
        result = max(result, value)
        return


    # 물건을 고르는 경우
    recur(idx+1, weight + arr[idx][0], value + arr[idx][1])

    # 물건을 고르지 않는 경우
    recur(idx+1, weight, value)

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    recur(0,0,0)
    # 출력ㅁ
    print(f"#{test_case} {result}")