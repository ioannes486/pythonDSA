"""TODO:
- 상수
    L : 육지
    W : 바다

    보물지도의 가로, 세로 크기는 각각 50 이하이다
- 변수

- 조건(제약사항)
    이동은 상하좌우로 이웃한 육지로만 이동가능하다
    -> di, dj쓰자

    한칸 이동하는데 한 시간이 걸린다.
    -> 최소 시간 혹은 최대시간 구하라고 할듯

    보물은 서로간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
    -> 바다에는 없다.

    같은 곳을 두 번 이상 지나가거나 멀리 돌아가서는 안된다.
    -> 방향이 있는 그래프, dfs써야 할듯?


- 구하는 값
    보물이 묻혀있는 두 곳 간의 최단거리로 이동하는 시간을 구하라

- 아이디어
    bfs :
    모든 점에 대해
    점이 육지면
    visited 배열과
    거리합을 저장할 배열 만들기
    bfs 진행하기
    방문을 하면 현재 거리합의 + 1 된 결과를 거리합 배열에 넣어주기
    더 큰값이 나오면 그 값으로 해주셈
    지금 방문한 곳을 큐스택에 넣기
"""
from collections import deque


di = [0,1,0,-1]
dj = [1,0,-1,0]
def solve(N, M, treasure_map):
    maximum_duration = 0
    for i in range(N):
        for j in range(M):
            if treasure_map[i][j] == 'L':
                visited = [[0 for _ in range(M)] for _ in range(N)]
                visited[i][j] = 1;
                distances = [[0 for _ in range(M)] for _ in range(N)]
                start = [i, j]
                q = deque([start])

                while q:
                    i_idx, j_idx = q.popleft()
                    for idx in range(4):
                        ni = i_idx + di[idx]
                        nj = j_idx + dj[idx]
                        if 0<=ni<N and 0<=nj<M:
                            if treasure_map[ni][nj] == 'L':
                                if visited[ni][nj] != 1:
                                    visited[ni][nj] = 1
                                    distances[ni][nj] = distances[i_idx][j_idx] + 1
                                    q.append([ni,nj])
                                    maximum_duration = max(maximum_duration, distances[ni][nj])



    return maximum_duration

# 입력
N, M = map(int, input().split()) # 지도 세로, 가로
treasure_map = [list(input()) for _ in range(N)]

# 출력
print(solve(N, M, treasure_map))