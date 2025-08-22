import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    in order 형식으로 순회할것
    트리는 완전 이진트리형식으로 주어지며 노드당 하나의 문자만 저장할 수 있다.
    
- 구하는 값

- 아이디어
"""

def inorder(node):
    global result
    if node <= last:
        inorder(2 * node)
        result += tree[node]
        inorder(2 * node + 1)


T = 10
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    tree = ["0"] * (N+1)
    for i in range(N):
        temp = list(input().split())
        tree[int(temp[0])] = temp[1]
    last = len(tree) - 1

    result = ""
    inorder(1)
    # 출력
    print(f"#{test_case} {result}")