import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    V: 노드 개수
    E :간선개수
- 조건(제약사항)
    방향성 X : 그래프 만들 때 양쪽 추가 해야함
    
- 구하는 값
    주어진 출발 노드에서 최소 몇개의 간선을 지나면 도착노드에 갈 수 있는지
- 아이디어
"""

from collections import deque


def bfs(start, graph, G):
    visited = [-1 for _ in range(V + 1)]
    q = deque([start])
    visited[start] = 0

    while q:
        v = q.popleft()

        for nxt in graph[v]:
            if visited[nxt] == -1:
                visited[nxt] = visited[v] + 1
                q.append(nxt)

    return visited[G]


def solve(graph, S, G):
    result = bfs(S, graph, G)
    return result if result > 0 else 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    V, E = map(int, input().split())  # 노드 수, 간선 수

    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())

    # 출력
    print(f"#{test_case} {solve(graph, S, G)}")
