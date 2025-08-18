
import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def max_sum(N,M,arr):
    max_val = 1
    min_val = 10000 * N
    for i in range(N-M+1):
        result = 0
        for j in range(i,i+M):
            result += arr[j]
        if max_val < result:
            max_val = result
        if min_val > result:
            min_val = result

    return max_val - min_val



for test_case in range(1, T + 1):

    N, M = map(int, input().split())    # 안녕하세요
    arr = list(map(int, input().split()))

    print(f"#{test_case} {max_sum(N,M,arr)}")