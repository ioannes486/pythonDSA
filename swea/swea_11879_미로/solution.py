import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""
di = [1,0,-1,0]
dj = [0,1,0,-1]
def dfs(i_index, j_index, maze):
    maze[i_index][j_index] = 1

    for direction_index in range(4):
        ni = i_index + di[direction_index]
        nj = j_index + dj[direction_index]
        if 0 <= ni < N and 0<= nj < N:
            if maze[ni][nj] != 1:
                dfs(ni, nj, maze)



T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    start_i = -1
    start_j = -1
    goal_i = -1
    goal_j = -1

    maze = [[0] * N for _ in range(N)]
    for i in range(N):
        text = input()
        for j in range(N):
            elem = int(text[j])
            if elem == 2:
                start_i = i
                start_j = j
            elif elem == 3:
                goal_i = i
                goal_j = j
            maze[i][j] = elem

    dfs(start_i, start_j, maze)

    result = 0
    if maze[goal_i][goal_j] == 1:
        result = 1


    # 출력
    print(f"#{test_case} {result}")