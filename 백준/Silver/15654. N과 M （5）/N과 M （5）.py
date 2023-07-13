import sys

a = [0 for _ in range(10)]
c = [0 for _ in range(10001)]


def go(index, n, m):
    if index == m:
        print(' '.join(a[:m]))
        return

    for i in s:
        if c[i] == 1:
            continue
        c[i] = 1
        a[index] = str(i)
        go(index + 1, n, m)
        c[i] = 0


N, M = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
s.sort()
go(0, N, M)