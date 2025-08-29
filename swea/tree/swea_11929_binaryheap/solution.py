import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    항산 완전 이진트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
    부모노드의 값 자식노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모노드와 값을 바꾼다.
    노드번호는 루트가 1번, 왼쪽에서 
- 구하는 값
    마지막 노드의 조상노드에 저장된 정수의 합을
    리프노드를 제외한 애들만 다 구하기
- 아이디어
"""


def solve(N, temp):
    answer = 0

    tree = [0] * (N + 1)
    for val in temp:
        enq(tree, val)

    idx = N // 2
    while idx > 0:
        answer += tree[idx]
        idx //= 2

    return answer


def enq(tree, val):
    global last
    last += 1
    tree[last] = val

    c = last
    p = c // 2

    while p > 0 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    temp = list(map(int, input().split()))
    last = 0

    # 출력
    print(f"#{test_case} {solve(N,temp)}")
