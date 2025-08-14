import sys
sys.stdin = open("input.txt", "r")

# 메모이제이션 테이블
dp = [0] * 11

def factorial(number):

    if number <= 1:
        return 1

    if dp[number] != 0:
        return dp[number]

    dp[number] = number * factorial(number-1)

    return dp[number]

def comb(i,j):
    if j == 0:
        return 1

    if j == i:
        return 1
    result = (factorial(i)//factorial(j))//factorial(i-j)
    return result

def solve(N):
    for i in range(N):
        for j in range(i+1):
            print(comb(i,j), end=" ")
        print()


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    # 출력
    print(f"#{test_case}")
    solve(N)