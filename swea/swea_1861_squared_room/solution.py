import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N : 방의 크기, 1dltkd 1000이하 
    방안의 숫자 : 1이상 N^2이하의 수, 
    모든 방에 대해 서로 다르다
- 조건(제약사항)
    상하좌우이다 -> 델타를 이용한다.
    처음에 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는가?  

- 구하는 값
    처음에 출발해야 하는 방 번호와 최대 몇개의 방을 이동할 수 있는지 공백으로 구분하여 출력
    이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 선택한다.
- 아이디어
"""


from collections import deque


di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(start):

    q = deque([start])

    while q:
        v = q.popleft()
        ci = v[0]
        cj = v[1]

        for dir in range(4):
            ni = ci + di[dir]
            nj = cj + dj[dir]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == arr[ci][cj] + 1:
                    q.append([ni, nj])



    return


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    # 1. 입력 받기
    N = int(input())

    arr = list(map(int, input().split()))
    # 출력
    print(f"#{test_case} {solve()}")