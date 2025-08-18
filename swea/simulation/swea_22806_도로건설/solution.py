import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    각 셀은 높이가 달라서 도로를 지나가는 셀들은 같은 높이로 만들어야 한다
    높이가 A인 곳의 높이를 B로 만들기 위해서는 차이만큼의 비용이 필요하다
    -> abs()사용
    높이는 1이상 5이하임
    최소 비용이 같은 경우가 둘 이상일 때는 낮은 높이로 도로를 건설한다. 초과/미만 부등호 사용하기
    
- 구하는 값
    가로와 세로 도로를 최소 비용으로 건설하는 높이와 비용
- 아이디어
    1. 가로와 세로의 높이 탐색
    2. 기준높이와 차이의 절댓값을 모두 더했을 때 가장 최소가 되는 지점 구하기
    3. 기준 높이는 1에서 5까지임
    
"""


di = [1,0,-1,0]
dj = [0,1,0,-1]
def solve(N, arr):
    min_cost_sum = float('inf')
    final_height = 0
    loc_i = 0
    loc_j = 0

    for i in range(N):
        for j in range(N):

            for target_height in range(5):
                cost_sum = abs(arr[i][j] - target_height)
            # 십자 영역 순회하면서 더하기
                for dist in range(1, N):
                    for idx in range(4):
                        ni = i + (dist*di[idx])
                        nj = j + (dist*dj[idx])
                        if 0<=ni<N and 0<=nj<N:
                            cost_sum += abs(arr[ni][nj] - target_height)


                if min_cost_sum >= cost_sum:
                    min_cost_sum = cost_sum
                    final_height = target_height





    return min_cost_sum, final_height


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cost, height = solve(N, arr)
    # 출력
    print(f"#{test_case} {min_cost} {height}")