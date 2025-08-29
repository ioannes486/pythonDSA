import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    출발점은 0, 도착점은 99
- 변수
    길의 총 개수
- 조건(제약사항)
    출발은 0 도착은 99
    정점의 개수는 98개를 출발점과 도착점 포함하면 100개를 넘어가지 않는다
    -> 모든 노드를 표현하기 위해서는 100개의 그래프 노드가 필요하다
- 구하는 값
    0에서 99까지 가는 길이 존재하는지 여부를 각각 1과 0으로 반환
- 아이디어
    길의 총 개수 = 어디부터 어디까지 갈 수 있다를 표현한 1차원 배열 or 튜플 or 표현의 개수
    N을 받아서 2N까지 돌려야 할듯?
"""


def dfs(graph, node_idx, visited):
    visited[node_idx] = True

    for i in graph[node_idx]:
        if not visited[i]:
            dfs(graph, i, visited)


def solve(graph):
    visited = [False for _ in range(100)]

    dfs(graph, 0, visited)

    if visited[99]:
        return 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    source = list(map(int, input().split()))
    graph = [[] for _ in range(100)]  # 0번부터 99번까지 노드 필요함
    for i in range(N):
        graph[source[2 * i]].append(source[2 * i + 1])

    print(f"#{test_case} {solve(graph)}")
