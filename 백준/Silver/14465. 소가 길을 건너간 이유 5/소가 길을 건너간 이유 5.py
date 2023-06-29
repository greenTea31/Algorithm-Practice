import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
broken = set()

for _ in range(B):
    broken.add(int(input()))

s, e = 1, K
repair = 0
answer = 100001

for i in range(1, K+1):
    if i in broken:
        repair += 1

answer = min(answer, repair)

while e < N:
    if s in broken:
        repair -= 1
    s += 1
    e += 1
    if e in broken:
        repair += 1
    answer = min(answer, repair)

print(answer)

