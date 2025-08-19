from collections import deque

def bfs(graph, start):
    visited  = [False for _ in range( N +1)] # visited배열 생성
    queue = deque([start]) # queue생성
    visited[start] = True

    while queue:
        v = queue.popleft()
        for adj_node in graph[v]:
            if not visited[adj_node]:
                visited[adj_node] = True
                queue.append(adj_node)

    return visited

def solve(graph):

    visited = bfs(graph, 1)

    linked_cnt = 0
    for v in visited:
        if v:
            linked_cnt += 1

    return linked_cnt - 1


# 입력
N = int(input())
M = int(input())

# 1번노드부터 시작하므로 +1해주기
graph = [[] for _ in range( N +1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 출력
print(solve(graph))