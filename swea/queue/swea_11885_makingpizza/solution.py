

"""TODO:
- 상수

- 변수
    N: 피자를 동시에 구울 수 있는 화덕의 수 3 이상 20이하
    M : 구울 피자의 총 개수 N이상 100이하
    ci : 각 피자

- 조건(제약사항)
    치즈가 모두 녹으면 화덕에서 꺼낸다. 치즈의 양은 피자마다 다르다
    피자는 1번 위치에서 넣거나 뺄 수 있다. -> front의 위치
    front의 위치에서 치즈를 확인하고 다시 같은 자리에 넣을 수 있다. -> 치즈가 다 안됐으면 빼지 않는다.
    화덕을 한 바퀴 돌 때 녹지 않은 치즈의 양은 반으로 줄어든다. -> 한바퀴를 돌아야 한다.
    치즈가 모두 녹아 0이 되면 화덕에서 꺼내고 바로 그 자리에 남은 피자를 순서대로 넣는다
- 구하는 값
    가장 마지말까지 남아있는 피자 번호
- 아이디어
"""


import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def solve( N, M, pizzas ):

    q = deque(list(range(N)))
    rotation_number = 0

    idx = N
    # 마지막 피자가 남을 때까지 피자 굽기
    while len(q) > 1:
        if pizzas[q[0]] > 0:
            q.append(q.popleft())
        elif pizzas[q[0]] == 0:
            q.popleft()
            if idx < M:
                q.append(idx)
                for _ in range(N-1):
                    q.append(q.popleft())
                idx += 1
        rotation_number += 1

        if rotation_number == N:
            for i in range(len(q)):
                pizzas[q[i]] = pizzas[q[i]] // 2

            rotation_number = 0

    return q[0] + 1


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())

    pizzas = list(map(int, input().split()))
    # 출력
    print(f"#{test_case} {solve(N, M, pizzas)}")
