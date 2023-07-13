import sys

a = [0 for _ in range(10)]


def go(index, up, n, m):
    if index == m:
        print(' '.join(a[:m]))
        return

    for i in range(up, n):
        a[index] = str(s[i])
        go(index + 1, i, n, m)


N, M = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
s.sort()
go(0, 0, N, M)