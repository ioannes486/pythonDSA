import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    트럭당 한 개의 컨테이너
    적재용량을 초과하면 안됨
    최대 M대의 트럭이 편도로 한번 운행한다
    
    이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램
    화물을 싣지 못한 트력이 있을 수도 있고 남는 화물이 있을 수도 있음
- 구하는 값
    이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면 옮겨진 화물의 전체 무게
- 아이디어
"""

def solve():
    result = 0
    start = 0

    for truck in trucks:
        for i in range(start, N):
            if (payloads[i] <= truck):
                result += payloads[i]
                payloads[i] = 999999
                break

    return result


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())

    payloads = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    payloads.sort(reverse=True)
    trucks.sort(reverse=True)

    # 출력
    print(f"#{test_case} {solve()}")