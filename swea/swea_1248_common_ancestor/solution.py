import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    V: 정점의 개수
    E : 간손의 개수
    node1 
    node2
    : 공통조상을 찾아야 하는 두개의 정점
- 조건(제약사항)
    완전 이진트리 아님
- 구하는 값
    임의의 두 정점의 가장 가까운 공통조상을 찾고, 그 정점을 루트로 하는 서브트리의 크기
- 아이디어
    가장 가까운 정점 : 레벨이 가장 가까운 것 해당 부모노드를 타고 올라가서 조상노드의 인덱스 값이 같으면 
    서브트리 영역 감소
"""

def postorder(node):
    global result
    global answer_cnt
    global common_node

    if node == node1 or node == node2:
        answer_cnt += 1

    if answer_cnt == 2:
        return


    if node != 0:
        if answer_cnt == 1:
            result += 1
        postorder(tree[node][0])

        postorder(tree[node][1])

def solve():
    result = 0
    answer_cnt = 0
    common_node = 1

    postorder(1)
    return result





T = int(input())
for test_case in range(1, T + 1):
    # 입력
    V,E,node1, node2 = map(int, input().split())

    temp = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(V + 1)]


    for i in range(E):
        p, c = temp[2 * i], temp[2 * i + 1]

        if tree[p][0]:
            tree[p][1] = c
        else:
            tree[p][0] = c



    # 순회순서를 바꿔서 두개를 찾으면 계산값을 반환하도록 할 수 있는 방법이 있지 않을까?
    # 출력
    print(f"#{test_case} {result}")