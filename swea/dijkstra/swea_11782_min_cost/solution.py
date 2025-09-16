import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    
- 변수

- 조건(제약사항)
    인접지역으로 이동시에는 기본적으로 1만큼의 연료가 들고 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다
    -> 1 + max(도착지 높이 - 출발지 높이, 0)
- 구하는 값
    이동 가능한 지역의 높이 정보에 따라 최소 연료소비량 출력하기
- 아이디어
"""
from heapq import heappop, heappush

INF = int(21e8)

di = [0,1,0,-1]
dj = [1,0,-1,0]
def dijkstra(start_i, start_j):
    # 1. 모든 초기거리값 초기화하기
    pq = [(0, start_i, start_j)]
    dists = [[INF] * N for _ in range(N)]

    while pq:

        dist, i, j = heappop(pq)

        if dist > dists[i][j]:
            continue

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0<=ni<N and 0<=nj<N:
                fuel = 1 + max(graph[ni][nj] - graph[i][j], 0)
                new_dist = fuel + dist

                if dists[ni][nj] <= new_dist:  # 이미 그곳에 더 짧은 거리로 갔으면 그냥 지나가기
                    continue

                dists[ni][nj] = new_dist  # 그렇지 않다면 new_dist를 새롭게 등록해주기
                heappush(pq, (new_dist, ni, nj))

    return dists[N-1][N-1]

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]




    # 출력
    print(f"#{test_case} {dijkstra(0, 0)}")