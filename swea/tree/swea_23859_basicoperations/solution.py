import sys
sys.stdin = open("input.txt", "r")

def solve():
    post_order(1)
    return tree_values[1].split('.')[0]


def post_order(node):
    if node != 0:
        post_order(tree_children[node][0])
        post_order(tree_children[node][1])
        calculate(node)


def calculate(node):
    operator = tree_values[node]
    if operator in "+-*/":
        l = tree_children[node][0]
        r = tree_children[node][1]
        operand1 = float(tree_values[l])
        operand2 = float(tree_values[r])
        if operator == "+":
            tree_values[node] = str(operand1 + operand2)
        elif operator == "-":
            tree_values[node] = str(operand1 - operand2)
        elif operator == "*":
            tree_values[node] = str(operand1 * operand2)
        elif operator == "/":
            tree_values[node] = str(operand1 / operand2)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    tree_values = ['0' for _ in range(N+1)]
    tree_children = [[0] * 2 for _ in range(N+1)]
    for _ in range(N):
        line = list(input().split())
        idx = int(line[0])
        tree_values[idx] = line[1]
        if len(line) == 4:
            tree_children[idx][0] = int(line[2])
            tree_children[idx][1] = int(line[3])




    # 출력
    print(f"#{test_case} {solve()}")
