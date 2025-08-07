def i_hate_flies(N, M, arr):
    # 변수 초기화
    result = 0

    # 배열 순회하기
    for i in range(N-M+1):
        for j in range(N-M+1):
            flies_amount_total = 0

            # 파리 때리기
            for p in range(M):
                for q in range(M):
                    flies_amount_total += arr[i + p][j + q]

            # 파리 때려서 나온 합이 초기화된 최댓값보다 크면 갱신
            if result < flies_amount_total:
                result = flies_amount_total
    return result


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{test_case} {i_hate_flies(N, M ,arr)}")
