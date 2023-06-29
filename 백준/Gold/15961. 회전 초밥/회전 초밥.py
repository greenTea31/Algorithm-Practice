import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []

for _ in range(N):
    sushi.append(int(input()))

window = {}
answer = 1

for i in range(k):
    if sushi[i] not in window:
        window[sushi[i]] = 1
    else:
        window[sushi[i]] += 1

temp_answer = len(window) if c in window else len(window)+1
answer = max(answer, temp_answer)
s, e = 0, k-1

while s < N-1:
    window[sushi[s]] -= 1

    if window[sushi[s]] == 0:
        del window[sushi[s]]

    s += 1
    e += 1

    if e == N:
        e = 0

    if sushi[e] not in window:
        window[sushi[e]] = 1
    else:
        window[sushi[e]] += 1

    temp_answer = len(window) if c in window else len(window) + 1
    answer = max(answer, temp_answer)

print(answer)
