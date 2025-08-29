import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    
- 변수
    N : 1부터 N까지 이진탐색트리에 저장해야 함
- 조건(제약사항)
    와전이진트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다
    
- 구하는 값
    완전 이진트리로 만든 이진 탐색트리의 루트에 저장된 값과 N/2번 노드에 저장된 값
- 아이디어
    중위순회하기
    1. 입력 받아서 1부터 N까지 넣기
    완전 이진트리이므로 일차원 배열로 하면 됨
"""


def solve(N, tree):
    in_order(1)
    return tree[1], tree[N // 2]


def in_order(node):
    global num
    if node <= N:
        in_order(2 * node)
        tree[node] = num
        num += 1
        in_order(2 * node + 1)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    tree = [0] * (N + 1)
    num = 1
    n, p = solve(N, tree)

    # 출력
    print(f"#{test_case} {n} {p}")
