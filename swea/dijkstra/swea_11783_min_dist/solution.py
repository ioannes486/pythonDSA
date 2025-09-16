import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    
- 변수
    E 개의 일방통행구간 : 간선의 개수
    N : 정점의 개수
    
- 조건(제약사항)

- 구하는 값

- 아이디어
"""
from heapq import heappop, heappush

INF = int(21e8)

def dijkstra(start_node):
    dists = [INF] * (N+1)

    pq = [(0, start_node)]

    while pq:
        dist, node = heappop(pq)

        if dist > dists[node]:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if new_dist >= dists[next_node]:
                continue
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))




    return dists[N]


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, E = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))


    # 출력
    print(f"#{test_case} {dijkstra(0)}")