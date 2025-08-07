





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    arr = list(map(int, input().split()))

    max_val = -9999999
    for i in range(N):
        for j in range(N):
            target = arr[i] - arr[j]
            if target > max_val:
                max_val = target

    print(f"#{test_case} {max_val}")
    # ///////////////////////////////////////////////////////////////////////////////////










