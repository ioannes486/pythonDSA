import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    s g

- 변수

- 조건(제약사항)
    깊이 1이라면 복구에 드는 시간이 1이다
    파여진 깊이에 비례해서 복구 시간은 증가한다.

- 구하는 값
    출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간
- 아이디어
"""

from heapq import heappop, heappush

INF = int(21e8)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dijkstra(start_i, start_j):
    pq = [(0, start_i, start_j)]
    dists = [[INF] * N for _ in range(N)]
    while pq:

        dist, i, j = heappop(pq)
        if dist > dists[i][j]:
            continue

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < N and 0 <= nj < N:
                next_dist = dist + graph[ni][nj]

                if next_dist >= dists[ni][nj]:
                    continue

                dists[ni][nj] = next_dist
                heappush(pq, (next_dist, ni, nj))

    return dists[N-1][N-1]


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    graph = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            graph[i][j] = int(graph[i][j])

    min_time = dijkstra(0,0)
    # 출력
    print(f"#{test_case} {min_time}")

