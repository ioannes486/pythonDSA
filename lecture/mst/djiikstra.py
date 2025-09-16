import sys
sys.stdin = open("input.txt")


from heapq import heappush, heappop
INF = int(21e8)

V, E = map(int, input().split())

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF]* V
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            # 누적거리 = 현재 거리 + 다음 거리

            #이미 크거나 같은 가중치로 온 적이 있다면 continue

            if dists[next_node] <= new_dist:
                continue

            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))


    return dists


start_node = 0

graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight, = map(int, input().split())
    graph[start].append((weight, end))

result = dijkstra(0)
print(result)