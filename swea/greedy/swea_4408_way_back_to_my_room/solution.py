from collections import deque


import sys
sys.stdin = open("input.txt", "r")



"""TODO:
- 상수
    400 : 방의 총 개수
- 변수

- 조건(제약사항)
    
- 구하는 값
    최소 몇시간만에 모든 학생이 이동할 수 있는지를 구하라
- 아이디어
    화물 문제랑 비슷 한듯
"""


# 1. 각 번호의 인덱스 계산하기
# 2. 안겹치는 애들끼리 집어넣기 -> 스택을 활용할 수 있을듯?+

def convert_room_number_into_index(room_number):
    room_number = int(room_number)
    if room_number % 2 == 1:
        result = room_number // 2
    else:
        result = room_number // 2 - 1
    return result

def solve():
    visited = [0] * 200
    for start, end in arr:
        if start > end:
            start , end = end, start

        for i in range(start, end+1):
            visited[i] += 1
    return max(visited)


T = int(input())
for test_case in range(1, T + 1):
    # 입력

    N = int(input())

    arr = [list(map(convert_room_number_into_index, input().split())) for _ in range(N)]
    # 출력
    print(f"#{test_case} {solve()}")