import sys

N = int(sys.stdin.readline())
d = [i for i in range(100001)]
d[0] = 0

for i in range(2, N+1):
    j = 1
    while j*j <= i:
        if d[i] > d[i-j*j] + 1:
            d[i] = d[i-j*j] + 1
        j += 1

print(d[N])