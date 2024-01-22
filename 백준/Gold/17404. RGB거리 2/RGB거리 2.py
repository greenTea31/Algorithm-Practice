import sys

N = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

a1 = a2 = a3 = 0

d = [[p[0][0], 1000001, 1000001]]

for i in range(1, N):
    d.append([min(d[i-1][1], d[i-1][2]) + p[i][0],
              min(d[i-1][0], d[i-1][2]) + p[i][1],
              min(d[i-1][0], d[i-1][1]) + p[i][2]])

a1 = min(d[N-1][1], d[N-1][2])

d = [[1000001, p[0][1], 1000001]]

for i in range(1, N):
    d.append([min(d[i-1][1], d[i-1][2]) + p[i][0],
              min(d[i-1][0], d[i-1][2]) + p[i][1],
              min(d[i-1][0], d[i-1][1]) + p[i][2]])

a2 = min(d[N-1][0], d[N-1][2])

d = [[1000001, 1000001, p[0][2]]]

for i in range(1, N):
    d.append([min(d[i-1][1], d[i-1][2]) + p[i][0],
              min(d[i-1][0], d[i-1][2]) + p[i][1],
              min(d[i-1][0], d[i-1][1]) + p[i][2]])

a3 = min(d[N-1][0], d[N-1][1])

print(min(a1, a2, a3))