import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
ans = 0
idx = 0

while K > 0:
    while K >= coins[idx]:
        K -= coins[idx]
        ans += 1
    idx += 1

print(ans)