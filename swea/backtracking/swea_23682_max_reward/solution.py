import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def dfs(lev, dp):
    global ans
    money = int(''.join(arr))

    if (lev, money) in dp:
        return

    dp.append((lev, money))
    if lev == cnt:
        ans = max(ans, money)
        return

    if lev == N:
        print()


    for i in range(N):
        for j in range(N):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(lev + 1, dp)
            arr[i], arr[j] = arr[j], arr[i]






T = int(input())
for test_case in range(1, T + 1):
    # 입력
    num, cnt = input().split()
    arr = list(num)
    cnt = int(cnt)
    N = len(num)
    path = []
    ans = 0
    dp = []
    dfs(0,dp)

    # 출력
    print(f"#{test_case} {ans}")