

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

    q = deque(list(range(N))) # 피자의 인덱스로 이루어진 큐 만들기
    # N 이 3일 때 0,1,2피자가 들어가 있으니까
    # 다음에 3
    rotation_number = 0 # 한 번 피자를 확인 할때마다 1증가
    # rotation_number = N 오븐크기랑 같으면
    # 피자 배열에 있는 애들 중에 큐 안에 있는 피자의 치즈를 녹일거임

    idx = N # 다음에 피자를 추가할때 다음에 어떤 피자를 추가할지

    # 마지막 피자가 남을 때까지 피자 굽기
    while len(q) > 1:
        if pizzas[q[0]] > 0: # 큐 첫번째에 해당하는 피자의 치즈가 남아있으면
            q.append(q.popleft()) #

        # 치즈가 0이라고 해봐바
        #
        elif pizzas[q[0]] == 0:
            q.popleft()
            if idx < M: # 아직 피자 리스트에서 피자가 남아있으면
                q.append(idx) # 일단은 큐에 추가해줄거야
                for _ in range(N-1): # 큐에 추가해준 애를 맨 앞으로 옮겨야 되니까
                    q.append(q.popleft()) # N-1 1번만큼 원래 있던 애를 맨 오른쪽으로 옮기면
                    # 새로 추가하는애가 맨 왼쪽으로 오겠지
        #
                idx +=  1# 다음 피자의 인덱스

        rotation_number += 1

        # 로테이션을 N번 돌면
        # 치즈를 녹여주는거야
        if rotation_number == N:
            for i in range(len(q)):
                pizzas[q[i]] = pizzas[q[i]] // 2
             # 다시 로테이션 초기화
            rotation_number = 0

    return q[0] + 1 # 맨 마지막 인덱스에다 + 1 하면 구해지는거임


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())

    pizzas = list(map(int, input().split()))
    # 출력
    print(f"#{test_case} {solve(N, M, pizzas)}")
