import sys

a = [0 for _ in range(10)]


def go(index, n, m):
    if index == m:
        print(' '.join(a[:m]))
        return

    for i in range(1, n+1):
        a[index] = str(i)
        go(index + 1, n, m)


N, M = map(int, sys.stdin.readline().split())
go(0, N, M)