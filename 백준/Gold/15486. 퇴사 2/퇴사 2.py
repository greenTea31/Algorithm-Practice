import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+2)]
p = [[] for _ in range(N+1)]

for i in range(1, N+1):
    T, P = map(int, input().split())
    p[i] = [T, P]

for i in range(1, N+1):
    dp[i+1] = max(dp[i], dp[i+1])
    if i+p[i][0] > N+1:
        continue
    dp[i+p[i][0]] = max(dp[i+p[i][0]], dp[i] + p[i][1])

print(dp[N+1])