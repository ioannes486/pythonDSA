import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    1 : 벽
    0 : 통로
    3 : 도착
    2 : 출발

- 변수
    N = 미로의 한 변의 크기
    5 이상 100 이하
- 조건(제약사항)

- 구하는 값
    경로가 있는 경우 출발지에서 도착지까지 가는 최소 칸의 수
    경로가 없는 경우 0

- 아이디어
    bfs 돌리기 :
    도착점에서 거리를 계산해야되니깐 그냥 배열에 visited체크를 해버리면 헷갈릴 수 있음
    -> visited배열을 하나 만들자
"""


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs(graph, start, goal, N):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    q = [start]
    visited[start[0]][start[1]] = 0
    while q:
        i_idx, j_idx = q.pop(0)

        for nxt in range(4):
            ni = i_idx + di[nxt]
            nj = j_idx + dj[nxt]

            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] != 1 and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i_idx][j_idx] + 1
                    q.append([ni, nj])
    result = visited[goal[0]][goal[1]]

    return 1 if result > 0 else 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    tc = int(input())
    N = 100
    graph = [[0 for _ in range(N)] for _ in range(N)]

    start = goal = [0, 0]
    for i in range(N):
        line = list(input())
        for j in range(N):
            val = int(line[j])
            graph[i][j] = val

            if val == 2:
                start = [i, j]
                continue

            if val == 3:
                goal = [i, j]
                continue

    # 출력
    print(f"#{test_case} {dfs(graph, start, goal, N)}")
