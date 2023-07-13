import sys
a = [0 for _ in range(10)]


def go(index, up, n, m):
    if index == m:
        print(' '.join(a[:m]))
        return

    for i in range(up, n+1):
        a[index] = str(i)
        go(index + 1, i, n, m)


N, M = map(int, sys.stdin.readline().split())
go(0, 1, N, M)