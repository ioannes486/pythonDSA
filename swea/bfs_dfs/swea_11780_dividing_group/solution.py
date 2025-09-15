import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N: 정점의 개수 M:간선의 개수
- 조건(제약사항)
    한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.
    번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.
- 구하는 값
    전체 몇개의 조가 만들어지는가?
- 아이디어
    그냥 bfs돌리면 될듯
    그래프 방향은 무방향, 그래프를 만들 때는 양쪽 방향을 전부 고려해야 한다.
- 시간복잡도
    N은 최대 100
    bfs는 엔제곱이므로 10000번의 연산을 3초 안에 해야 함
    쌉가능    
"""

from collections import deque


def bfs(start, cnt):
    global visited
    q = deque([start])
    visited[start] = True
    while q:

        v = q.popleft()

        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())

    temp = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]

    for i in range(0, 2 * M, 2):
        graph[temp[i]].append(temp[i + 1])
        graph[temp[i + 1]].append(temp[i])

    visited = [False] * (N + 1)

    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            cnt = bfs(i, cnt)

    # 출력
    print(f"#{test_case} {cnt}")
