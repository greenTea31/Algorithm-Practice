import sys

a = [0 for _ in range(10)]
c = [0 for _ in range(10)]


def go(index, up, n, m):
    if index == m:
        print(' '.join(a[:m]))
        return

    for i in range(up, n+1):
        if c[i] == 1:
            continue
        c[i] = 1
        a[index] = str(i)
        go(index + 1, i + 1, n, m)
        c[i] = 0


N, M = map(int, sys.stdin.readline().split())
go(0, 1, N, M)