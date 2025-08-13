def recur(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    return 2 * recur(N-2) + recur(N-1)
T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input()) // 10
    dp = [0] * (N + 1)
    # 출력
    print(f"#{test_case} {recur(N)}")