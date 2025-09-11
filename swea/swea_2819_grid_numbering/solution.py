import sys
sys.stdin = open("input.txt", "r")


from collections import deque


"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""


di = [0,1,0,-1]
dj = [1,0,-1,0]
def dfs(i_idx, j_idx):


    for dir in range(4):
        ni = i_idx + di[dir]
        nj = j_idx + dj[dir]
        if 0<=ni<4 and 0<=nj<4:
            dfs(ni,nj)


T = int(input())
for test_case in range(1, T + 1):
    # 입력

    arr = [list(map(int, input().split())) for _ in range(4)]



    # 출력
    print(f"#{test_case} {solve()}")