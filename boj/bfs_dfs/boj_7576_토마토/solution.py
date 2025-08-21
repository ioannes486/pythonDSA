"""TODO:
- 상수
    1 익은 토마토
    0 익지 않는 토마토, -1은 토마토가 들어있지 않은 칸
- 변수
    N: 상자의 크기 : i인덱스
    M : 상자의 가로 크기 : j인덱스
    2 이상 1000이하

- 조건(제약사항)
    보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다
    인접토마토는 상하좌우 네 방향탐색을 해야 함
    토마토가 저절로 익는 경우는 없다

- 구하는 값
    며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.
    ->bfs로 여러 지점에서 가는 최단거리 중에서 가장 최대값을 구하면 모든 토마토가 익는다.
- 아이디어
    칸이 -1이 아니면 가기
"""
from collections import deque

di = [0,1,0,-1]
dj = [1,0,-1,0]

def solve(N, M, arr):
    q = deque()

    # 시작 점 찾아서 큐에 넣기
    distance = [[-1 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append([i,j])
                distance[i][j] = 0



    while q:
        i_idx, j_idx = q.popleft()

        for p in range(4):
            ni = i_idx + di[p]
            nj = j_idx + dj[p]
            if 0<=ni<N and 0<=nj<M:
                if distance[ni][nj] == -1 and arr[ni][nj] == 0:
                    distance[ni][nj] = distance[i_idx][j_idx] + 1
                    q.append([ni, nj])

    result = 0
    for i in range(N):
        for j in range(M):
            # 익지 않은 토마토 발견 > 실패
            if arr[i][j] != -1 and distance[i][j] == -1:
                return -1
            # 최대 날짜 구하기
            if distance[i][j] > result:
                result = distance[i][j]
    return result

# 입력
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


# 출력
print(solve(N, M, arr))