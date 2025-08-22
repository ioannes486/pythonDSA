'''
1 3
1 2 1 3 2 4 3 5 3 6 4 7
'''
"""TODO:
- 상수

- 변수
    N : N이하의 노드 수를 구하라
    
- 조건(제약사항)
    부모와 자식 노드 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트노드가 된다
    
- 구하는 값

- 아이디어
"""

import sys
sys.stdin = open("input.txt", "r")

def preorder(node):
    global result
    if node != 0:  # 0이 들어가면 튕겨져 나옴
        result += 1
        preorder(tree[node][0])  # 12번의 자식은 0
        preorder(tree[node][1])




T = int(input())
for test_case in range(1, T + 1):
    # 입력
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(E + 2)]  # 인접리스트 14*3

    for i in range(E):
        p, c = temp[i * 2], temp[i * 2 + 1]

        if tree[p][0] == 0:  # 왼쪽자식 없으면
            tree[p][0] = c
        else:  # 왼쪽자식 있으면
            tree[p][1] = c
    result = 0
    preorder(N)
    # 출력
    print(f"#{test_case} {result}")
