import sys
input = sys.stdin.readline

N = int(input())
A, Pa, B, Pb = map(int, input().split())
dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    if i-Pa >= 0 and dp[i][0] < dp[i-Pa][0] + A:
        dp[i][0], dp[i][1], dp[i][2] = dp[i-Pa][0] + A, dp[i-Pa][1] + 1, dp[i-Pa][2]
    if i-Pb >= 0 and dp[i][0] < dp[i-Pb][0] + B:
        dp[i][0], dp[i][1], dp[i][2] = dp[i-Pb][0] + B, dp[i-Pb][1], dp[i-Pb][2] + 1

max_value = 0
max_index = 0

for i in range(N+1):
    if dp[i][0] > max_value:
        max_index = i
        max_value = dp[i][0]

print(dp[max_index][1], dp[max_index][2])

