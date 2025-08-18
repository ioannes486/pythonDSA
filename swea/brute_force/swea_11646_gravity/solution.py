import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())


def solve(N, arr):
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if result < cnt:
            result = cnt
    return result


for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f"#{test_case} {solve(N, arr)}")