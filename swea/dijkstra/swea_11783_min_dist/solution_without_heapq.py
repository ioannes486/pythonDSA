import sys
sys.stdin = open("input.txt", "r")

INF = float('inf')


def dijkstra(v):
    # 1. 출발점 설정
    dists[v] = 0

    # 2. 반복(정점 수)
    for _ in range(N):
    #   최소값 (가중치) + 미방문
        min_v = INF
        for i in range(V):
            if min_v > dists[i] and not visited[i]:
                min_v = dists[i]
                v = i  # 시작정점

    #   방문체크

    visited[v] = 1
    #   인접한 정점 가중치 갱신
    for w in range(V):
        if adj_mat[v][w] and not visited[w]:
            if dists[w] > dists[v] + adj_mat[v][w]:
                dists[w] = dists[v] + adj_mat[v][w]
    # 우선순위 큐를 쓸 때는 정점수보다 더 들어가며 이때 현재 가중치보다 큰 놈들은 전부 아웃시킨다
    # 우선순위 큐를 쓰지 않을 때는 정점수만큼 반복을 해준다.

    return


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, E = map(int, input().split())

    V = N + 1

    adj_mat = [[0] * V for _ in range(V)]
    adj_list = [[] for _ in range(V)]
    dists = [INF] * V
    visited = [0] * V

    for i in range(E):
        s,e,w = map(int, input().split())
        adj_mat[s][e] = w

    dijkstra(0)
    # 출력
    print(f"#{test_case} {solve()}")