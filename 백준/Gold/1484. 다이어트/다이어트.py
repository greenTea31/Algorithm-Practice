import sys
input = sys.stdin.readline

G = int(input())
weights = []

for i in range(1, 50002):
    weights.append(i)

answer = []
s, e = 0, 0

while True:
    temp_diff = weights[e] ** 2 - weights[s] ** 2

    if temp_diff < G:
        e += 1
    elif temp_diff > G:
        if e-s == 1:
            break
        s += 1
    else:
        answer.append(weights[e])
        s += 1
        e += 1

if answer:
    for ans in answer:
        print(ans)
else:
    print(-1)
