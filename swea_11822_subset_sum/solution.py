
NUMBER_OF_SUBSETS = 2**12
def solve(N, K):
    result = 0
    arr = [i for i in range(1,13)]

    for i in range(NUMBER_OF_SUBSETS):
        # 각 부분집합에 대한 연산
        subset_sum = 0
        subset_cnt = 0
        for j in range(12):
            if i & (1<<j): # 부분집합인 경우
                # 원소수가 N개인지 판별하기
                subset_cnt += 1  # 부분집합의 원소 수
                subset_sum += arr[j] # 부분집합의 합


        if (subset_sum == K) and (subset_cnt == N):
            result += 1
    return result


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, K = map(int, input().split())
    # 출력
    print(f"#{test_case} {solve(N, K)}")