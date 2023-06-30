import sys
input = sys.stdin.readline
parent = [i for i in range(1001)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    aRoot, bRoot = find(a), find(b)

    if aRoot == bRoot:
        return

    parent[bRoot] = aRoot


N = int(input())
E = []

for _ in range(N):
    E.append(list(map(int, input().split())))

edges = []

for i in range(N):
    for j in range(i+1, N):
        edges.append([E[i][j], i, j])

edges.sort()

connected = 0
answer = 0

for edge in edges:
    cost, a, b = edge

    if find(a) == find(b):
        continue
    union(a, b)
    answer += cost
    connected += 1
    if connected == N-1:
        break

print(answer)