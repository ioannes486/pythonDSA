import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    시간 0시부터 24시까지
    한번에 하나의 화물차만 작업이 가능하다
- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
    시간을 증가시키면서 그때 가능한 경우의 수 확인하기
    그때 가능한 경우위 수 중 가장 소요시간이 낮은 애 찾기
    
"""

def is_truck_available(start, end):
    for j in range(start, end):
        if visited[j] == True:
            return False
    return True

def assign_truck(start, end):
    for j in range(start, end):
        visited[j] = True

def solve():
    result = 0
    for i in range(N):
        truck = arr[i]
        if is_truck_available(truck[0], truck[1]):
            result += 1
            assign_truck(truck[0], truck[1])


    return result


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key=lambda x: x[1] - x[0])
    visited = [False]* 25
    # 출력
    print(f"#{test_case} {solve()}")
