'''TODO
우선순위큐 복습
힙큐 사용법
힙의 시간 복잡도
'''


import sys
sys.stdin = open("input.txt")

from heapq import heappop, heappush


V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]

# 특정 정점 기주으로 시작
# 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다.
# 작은 노드를 먼저 꺼내기 위해 우선순위큐를 활용한다.


def prim(start_node):
    pq = [(0, start_node)] # 가중치, 노드 형태
    # 여기 가중치는 무슨의미? 그래프에 가중치가 있는데 얘는 어디서 튀어나온거지?
    MST = [0] * V # 방문체크하기
    min_weight = 0
    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight
        for next_node in range(V):
            if graph[node][next_node] ==  0:
                continue

            if MST[next_node]:
                continue
            # 힙큐에 넣기 전에 방문처리 해버리면 최소비용이 유지가 안됨
            heappush(pq, (graph[node][next_node], next_node))

    return min_weight

for _ in range(E):
    start, end , weight = map(int, input().split())
    # 가중치 그래프는 무방향인 경우가 많다
    # 출발정점을 바꾸어도 최소비용은 같다
    # 하지만 그래프는 다를 수 있다.

    graph[start][end] = weight
    graph[end][start] = weight

result = prim(start) # 출발 정접과 함께 시작
print(f"최소 비용 = {result}")