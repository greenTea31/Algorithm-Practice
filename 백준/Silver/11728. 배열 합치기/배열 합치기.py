import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s, e = 0, 0
sum_arr = []

while s < N or e < M:
    if s == N:
        sum_arr.append(B[e])
        e += 1
    elif e == M:
        sum_arr.append(A[s])
        s += 1
    else:
        if A[s] < B[e]:
            sum_arr.append(A[s])
            s += 1
        else:
            sum_arr.append(B[e])
            e += 1

print(' '.join(map(str, sum_arr)))
