import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    그래프에는 방향성이 존재함
- 구하는 값
    특정한 두개의 노드에 경로가 존재하는지 확인하는 프로그램 -> V에서 E까지 갈 수 있는가
- 아이디어
"""

def solve(V,E,arr):


    return graph


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    graph = [[] for _ in range(V+1)]


    # for elem in arr:
    #     graph[elem[0]].append(elem[1])


    # 출력
    print(f"#{test_case} {solve(V,E,graph)}")