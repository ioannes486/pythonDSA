import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N: 노드의 개수
    M: 리프노드의 개수
    L: 값을 출력할 노드번호
    
- 조건(제약사항)
    리프노드에 1000이하의 자연수가 저장되어 있음 최댓값은 2000* N
    
    
- 구하는 값
    지정한 노드 번호에 저장된 값
- 아이디어
"""


def solve(tree, L):
    post_order(1)
    return tree[L]


def post_order(node):
    if node <= N:
        post_order(2 * node)
        post_order(2 * node + 1)

        if 2 * node + 1 <= N:
            tree[node] = tree[2 * node] + tree[2 * node + 1]
        elif 2 * node == N:
            tree[node] = tree[2 * node]


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for i in range(M):
        idx, val = map(int, input().split())

        tree[idx] = val

    # 출력
    print(f"#{test_case} {solve(tree, L)}")
