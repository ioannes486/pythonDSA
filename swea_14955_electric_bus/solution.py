import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def boong_boong(K, N, M, battery):
    # 첫 항 확인하기
    result = 0

    # 다음 빠떼리가 어디있는지 판별하기
    idx = battery[0]

    if idx > K:
        return 0
    while idx < N:
        # K칸에 있으면 바로 이동
        if battery[idx] + K == battery[idx + 1]:
            result += 1
            idx += K

        # K번째 보다 안쪽에 있으면 다음거 확인해보기
        if battery[idx] + K > battery[idx+1]:
            if battery[idx] + K == battery[idx+2]




        elif battery[idx] + K == battery[idx+1]:
            result += 1
            idx += battery[idx]
            continue
        elif battery[idx] + K < battery[idx+1]:
            return 0



for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())

    battery = list(map(int, input().split()))
    print(f"#{test_case} {boong_boong(K, N, M, battery)}")


