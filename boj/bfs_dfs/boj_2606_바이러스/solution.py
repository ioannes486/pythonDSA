

"""TODO:
- 상수
    
- 변수
    컴퓨터의 수 : 100이하의 양의 정수 -> 노드의 수
    서로 연결되어 있는 컴퓨터의 쌍의 수 -> 간선의 수
- 조건(제약사항)
    한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜바이러스에 걸린다
    여러 개의 노드를 통해 1번 컴과 연결되어 있는 컴들은 전부 웜 바이러스에 걸린다
    
- 구하는 값
    1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
- 아이디어
    그냥 일단 dfs제끼라웃!
"""
def dfs(graph, v, visited):
    visited[v] = True

    for node_idx in graph[v]:
        if not visited[node_idx]:
            dfs(graph, node_idx, visited)

def solve(N, graph):
    visited  = [False for _ in range(N+1)]

    dfs(graph, 1, visited)

    linked_cnt = 0
    for v in visited:
        if v:
            linked_cnt += 1

    return linked_cnt - 1


# 입력
N = int(input())
M = int(input())

# 1번노드부터 시작하므로 +1해주기
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 출력
print(solve(N,graph))