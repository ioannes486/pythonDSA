import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N: 등산로를 만들기 위한 부지의 크기
- 조건(제약사항)
    등산로는 가장 높은 봉우리에서 시작해야 한다
    높은 지형에서 낮은 지형으로 가야 한다.
    딱 한곳을 정해서 K깊이만큼 지형을 깎을 수 있다.
- 구하는 값
    만들 수 있는 가장 긴 등산로를 찾아 길이를 출력하기
- 아이디어
"""

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(start_i, start_j, arr):
    q = deque([[start_i, start_j]])
    visited = [[-1] * N for _ in range(N)]
    visited[start_i][start_j] = 1

    max_length = 0
    while q:

        i, j = q.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0<= ni <N and 0<= nj <N:
                if visited[ni][nj] == -1 and arr[i][j] > arr[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    max_length = visited[ni][nj]
                    q.append([ni, nj])

    return max_length




def calculate_longest_trail(cur_graph):

    # 현재의 그래프에서 모든 영역을 순회하고 거리의 최댓값 구하기
    max_length = 0
    # 2. 모든 점에 대해서 구해보기
    for i in range(N):
        for j in range(N):
            if cur_graph[i][j] == max_height:
                max_length = max(max_length, bfs(i, j, cur_graph))

    return max_length

def process_graph(graph1):
    # 모든 상태의 그래프에서 거리의 최댓값 구하기

    result = -1
    for k in range(K+1):
        for i in range(N):
            for j in range(N):
                graph1[i][j] = graph1[i][j] - k
                result = max(calculate_longest_trail(graph), result)
                graph1[i][j] = graph1[i][j] + k

    return result

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, K = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0
    for i in range(N):
        max_height = max(max(graph[i]), max_height)



    # 출력
    print(f"#{test_case} {max_height}")
