import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""


from collections import deque


def is_condition_satisfied(number):
    if number > 0 and number <= 1000000:
        if visited[number] == -1:
            return True
    return False


def bfs(start):
    q = deque([start])

    visited[start] = 0

    while q:
        v = q.popleft()

        plus = v + 1
        minus = v - 1
        twice = v * 2
        ten = v - 10

        if plus == M or minus == M or twice == M or ten == M:
            visited[M] = visited[v] + 1
            break

        if is_condition_satisfied(plus):
            visited[plus] = visited[v] + 1
            q.append(plus)

        if is_condition_satisfied(minus):
            visited[minus] = visited[v] + 1
            q.append(minus)

        if is_condition_satisfied(twice):
            visited[twice] = visited[v] + 1
            q.append(twice)

        if is_condition_satisfied(ten):
            visited[ten] = visited[v] + 1
            q.append(ten)



    return visited[M]


T = int(input())
for test_case in range(1, T + 1):
    # 입력

    N, M = map(int, input().split())

    result = float('inf')

    visited = [-1] * 1000001


    # 출력
    print(f"#{test_case} {bfs(N)}")