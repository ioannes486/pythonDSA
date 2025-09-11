import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    
- 변수
    충전지의 수
- 조건(제약사항)
    최소한의 교환횟수로 목적지에 도착해야 한다.
- 구하는 값
    목적지에 도착하는데 필요한 최소한의 교환횟수 출력하기
    출발지에서 배터리 장착은 교환횟수에서 제외한다 -> 처음 시작은 인덱스가 0임
- 아이디어
"""

def recur(stop_idx, battery_remaining):
    global dp
    if battery_remaining == -1 :
        return 9999999999

    if stop_idx > N-1:
        return 9999999999999

    if stop_idx == N-1:
        return 0

    if dp[stop_idx][battery_remaining] != -1:
        return dp[stop_idx][battery_remaining]

    dp[stop_idx][battery_remaining] = min(recur(stop_idx+1, battery_remaining - 1), recur(stop_idx+1, batteries[stop_idx]-1) + 1)

    return dp[stop_idx][battery_remaining]



T = int(input())
for test_case in range(1, T + 1):
    # 입력
    arr = list(map(int, input().split()))

    N = arr[0]

    batteries = arr[1:]
    result = 9999999999999
    dp = [[-1] * (max(batteries)+1) for _ in range(N+1)]
    ans = recur(0,batteries[0])
    # 출력

    print(f"#{test_case} {ans}")