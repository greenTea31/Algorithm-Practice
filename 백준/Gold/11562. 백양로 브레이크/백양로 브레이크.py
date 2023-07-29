import sys
input = sys.stdin.readline

# 일방통행이라 바꿔야 하면 가중치 1, 플로이드 워셜

n, m = map(int, input().split())
road = [[250 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u, v, b = map(int, input().split())
    road[u][u], road[v][v] = 0, 0
    road[u][v], road[v][u] = 0, 1

    if b == 1:
        road[v][u] = 0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if road[i][k] + road[k][j] <= road[i][j]:
                road[i][j] = road[i][k] + road[k][j]

k = int(input())

for _ in range(k):
    s, e = map(int, input().split())
    print(road[s][e])


