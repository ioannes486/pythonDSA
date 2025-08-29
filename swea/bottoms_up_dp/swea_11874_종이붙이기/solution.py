# 재귀 함수
# 0번쨰 항 부터, N-1번째 까지 계산을 해야 An을 계산 할 수가 있음
# 0부터 N-1번째 항까지 값을 담으려면 dp크기가 N까지겠지


def recur(N):
    global dp  # 모든 재귀함수에 대해서 값을 저장하기 위함

    if N <= 1:
        return 1

    if dp[N] != 0:
        # 값이 무적권 1이상이니까
        # 0이 아니면 값을 이미 한번 계산해서 저장했다는 뜻
        return dp[N]

    return 2 * recur(N - 2) + recur(N - 1)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) // 10
    dp = [0] * (N + 1)

    print(f"#{test_case} {recur(N)}")
