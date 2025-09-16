import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x,y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    V, E = map(int, input().split())

    parents = [i for i in range(V+1)]

    edges = [list(map(int, input().split())) for _ in range(E)]

    edges.sort(key=lambda x: x[2])

    cnt = 0
    result = 0
    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            result += w
            if cnt == V:
                break


    # 출력
    print(f"#{test_case} {result}")