
import sys
sys.stdin = open("input.txt")


def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x ==rep_y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())

edges = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))


edges.sort(key=lambda x : x[2])
# 가중치가 작은 간선부터 순서대로 고르지
# 사이클이 발생하면 고르지 말자
# 언제까지?
# mst가 완성이 죌 때까지
# v-1개를 선택할 때 까지
# 왜 v개가 아니지?
# 아 간선을 선택하는구나

cnt = 0
result = 0

parents = [i for i in range(V)]

for u, v, w in edges:
    # 사이클이 아니라면
    # 같은 집합으로 만들기
    # cnt += 1
    # cnt == 1이면 종료

    if find_set(u) != find_set(v):
        parents[u] = v

    if cnt == V - 1:
        break


print(parents)

for i in range(V):
    print(find_set(i))