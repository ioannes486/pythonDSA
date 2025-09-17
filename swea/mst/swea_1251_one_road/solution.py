import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N : 바다의 크기
    
- 조건(제약사항)
    환경부담 세율 = E * 간선의 길이**2
- 구하는 값
    모든 섬들을 잇는 최소 환경 부담금을 소수 첫째 자리에서 반올림하기
    
- 아이디어
    프림의 알고리즘 으로 풀기
    
- 시간복잡도
    VlogV + ElogE
    
"""
from heapq import heappush, heappop
import math

def make_graph(start_node):

    min_weight = 0
    pq = [(0, start_node)]
    visited = [-1] * N
    while pq:
        dist, node = heappop(pq)

        if visited[node] != -1:
            continue
        visited[node] = 1
        min_weight += dist

        for nxt_node in range(N):
        # 한 정점에서 모든 정점을 다 갈 수 있음, 고로 완전그래프임
            if visited[nxt_node] != -1:
                continue
            route_cost = ((x_list[node] - x_list[nxt_node]) ** 2 + (y_list[node] - y_list[nxt_node]) ** 2) * E
            heappush(pq, (route_cost, nxt_node))

    return min_weight


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    min_weight = make_graph(0)

    # 출력
    print(f"#{test_case} {min_weight:.0f}")