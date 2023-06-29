import sys
input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []
E = []
F = []

for _ in range(N):
    q, w, e, r = map(int, input().split())
    A.append(q)
    B.append(w)
    C.append(e)
    D.append(r)

for i in range(N):
    for j in range(N):
        E.append(A[i] + B[j])
        F.append(C[i] + D[j])

E.sort()
F.sort()
real_length = len(E)
s, e = 0, real_length - 1
answer = 0
s_count, e_count = 1, 1

while s < real_length and e >= 0:
    temp_sum = E[s] + F[e]

    while s+1 < real_length and E[s] == E[s+1]:
        s += 1
        s_count += 1

    while e-1 >= 0 and F[e] == F[e-1]:
        e -= 1
        e_count += 1

    if temp_sum == 0:
        answer += s_count * e_count
        if s+1 < real_length:
            s += 1
            s_count = 1
        else:
            e -= 1
            e_count = 1
    elif temp_sum < 0:
        s += 1
        s_count = 1
    else:
        e -= 1
        e_count = 1

print(answer)

