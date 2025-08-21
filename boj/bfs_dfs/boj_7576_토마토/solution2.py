from collections import deque

di = [0,1,0,-1]
dj = [1,0,-1,0]

def solve(N, M, arr):
    q = deque()

    # 시작 점 찾아서 큐에 넣기
    distance = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append([i,j])
                distance[i][j] = 1


    while q:
        i_idx, j_idx = q.popleft()

        for p in range(4):
            ni = i_idx + di[p]
            nj = j_idx + dj[p]
            if 0<=ni<N and 0<=nj<M:
                if distance[ni][nj] == 0:
                    if arr[ni][nj] == 0:
                        distance[ni][nj] = distance[i_idx][j_idx] + 1
                        q.append([ni, nj])
                    else:
                        distance[ni][nj] = -1

    # -1안에 -1이 있는 경우 검사
    for k in range(N):
        for l in range(M):
            minus_cnt = 0
            if distance[k][l] == -1:
                for p in range(4):
                    ni = k + di[p]
                    nj = l + dj[p]
                    if 0 <= ni < N and 0 <= nj < M:
                        if distance[ni][nj] == -1:
                            minus_cnt -= 1
                if minus_cnt == -4:
                    distance[k][l] = -1

    # 모든 경우가 -1인 반례검사
    cnt = 0
    for k in range(N):
        for l in range(M):
            if arr[k][l] == -1:
                cnt += 1
    if cnt == M * N:
        return 0

    # 안 익은 토마토 전수조사
    for k in range(N):
        for l in range(M):
            if distance[k][l] == 0:
                return -1




    result = -2
    for idx in range(N):
        result = max(result, max(distance[idx]))


    return result -1

# 입력
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


# 출력
print(solve(N, M, arr))