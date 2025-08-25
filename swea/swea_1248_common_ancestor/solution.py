import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def search_ancestor(node):
    s = tree[node][2]
    p = []

    while s != 0:
        p.append(s)
        s = tree[s][2]
    return p

def common_ancestor(p1, p2):


def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    V,E, n1, n2 = map(int, input().split())
    temp = list(map(int, input().split()))

    tree = [[0]*3 for _ in range(V+1)]

    for i in range(E):
        p, c = temp[i*2], temp[i*2+1]
        if tree[p][0] == 0:
            temp[p][0] = c
        else:
            tree[p][1] = c

        tree[c][2] = p

    p1 = search_ancestor(n1)
    p2 = search_ancestor(n2)
    CA = common_ancestor(p1, p2)
    cnt = 0
    preorder(CA)
    # 출력
    print(f"#{test_case} {cnt}")