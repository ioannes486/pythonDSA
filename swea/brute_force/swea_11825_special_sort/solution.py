def solve(N, arr):
    # 테스트케이스마다 최대, 최솟값 갱신
    result_list = []
    dp = [0] * N
    for i in range(10):
        if i % 2 == 0:
            # 짝수면 최댓값
            max_val = 1
            max_idx = 0
            for j in range(N):
                if dp[j] != -1:
                    if max_val < arr[j]:
                        max_val = arr[j]
                        max_idx = j
            dp[max_idx] = -1
            result_list.append(arr[max_idx])
        else:
            min_val = 100
            min_idx = 0
            for j in range(N):
                if dp[j] != -1:
                    if min_val > arr[j]:
                        min_val = arr[j]
                        min_idx = j

            dp[min_idx] = -1
            result_list.append(arr[min_idx])
    return result_list


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))
    result_list = solve(N, arr)

    # 출력
    print(f"#{test_case}", end=" ")
    for item in result_list:
        print(item, end=" ")
    print()
