import copy

"""TODO:
- 상수
    16바이 16미로
    1 : 벽, 0 : 길
    시작점은 1,1 도착점은 3 2는 출발점
    테스트 케이스의 수
- 변수
    maze
- 조건(제약사항)

- 구하는 값
    출발점으로부터 도착지점까지 갈 수 잇는 길이 있는지 판단

- 아이디어
    di,dj활용, dfs, visited
"""


def solve(N, maze):
    visited = copy.deepcoc
    return


T = 10
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    maze = [list(input()) for _ in range(16)]
    # 출력
    print(f"#{N} {solve(N, maze)}")
