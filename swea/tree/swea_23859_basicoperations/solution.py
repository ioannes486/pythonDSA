import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값
    계산한 결과
- 아이디어
    계산이 안맏으면 부동소수점 연산도 고려해봐야할 듯?
"""


def solve(tree_values, tree_children):
    post_order(1, tree_values, tree_children)
    return tree_values, tree_children


def post_order(node, tree_values, tree_children):
    if node != 0:
        post_order(tree_children[node][0],tree_values, tree_children)
        post_order(tree_children[node][1], tree_values, tree_children)
        calculate(node, tree_values)


def calculate(node, tree):
    operator = tree[tree_values]
    if operator in "+-*/":
        operand1 = tree_values[tree_children[node][0]]
        operand2 = tree_values[tree_children[node][1]]
        if operator == "+":
            tree[node] = str(operand1 + operand2)
        elif operator == "-":
            tree[node] = str(operand1 - operand2)
        elif operator == "*":
            tree[node] = str(operand1 * operand2)
        elif operator == "/":
            tree[node] = str(operand1 / operand2)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    tree_values = [[0] for _ in range(N+1)]
    tree_children = [[0] * 2 for _ in range(N+1)]
    for _ in range(N):
        line = list(input().split())
        idx = int(line[0])
        tree_values[idx] = line[1]
        if len(line) == 4:
            tree_children[idx][0] = int(line[2])
            tree_children[idx][1] = int(line[3])




    # 출력
    print(f"#{test_case} {solve(tree_values, tree_children)}")
