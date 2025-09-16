import sys
sys.stdin = open("input.txt")


from heapq import heappush, heappop
INF = int(21e8)

V, E = map(int, input().split())

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * V  # 시작 정점에서 모든 와의 거리를 무한대로 초기화
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq) # 가장 최소 거리의 노드부터 뽑기
        if dists[node] < dist: # 이미 더 짧은 거리로 갔으면 그냥 지나가기
            continue

        for next_dist, next_node in graph[node]:  # 그래프에서 더 갈 수 있는 점들에 대하여
            new_dist = dist + next_dist # 각 지점까지 누적 거리 구하기

            # 누적거리 = 현재 거리 + 다음 거리

            #이미 크거나 같은 가중치로 온 적이 있다면 continue

            if dists[next_node] <= new_dist: # 이미 그곳에 더 짧은 거리로 갔으면 그냥 지나가기
                continue

            dist[next_node] = new_dist # 그렇지 않다면 new_dist를 새롭게 등록해주기
            heappush(pq, (new_dist, next_node))


    return dists


start_node = 0

graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight, = map(int, input().split())
    graph[start].append((weight, end))

result = dijkstra(0)
print(result)