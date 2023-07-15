import sys

N = int(sys.stdin.readline())
d = [[0 for _ in range(4)] for __ in range(N+1)]
p = [[0, 0, 0]]

for i in range(1, N+1):
    p.append(list(map(int, sys.stdin.readline().split())))
    d[i] = p[i]
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + p[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + p[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + p[i][2]

print(min(d[N]))