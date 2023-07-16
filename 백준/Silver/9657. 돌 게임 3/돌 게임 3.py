import sys
input = sys.stdin.readline

# 패배를 하나 이상 넘겨줄 수 있으면 내가 승리함

N = int(input())

dp = [0 for _ in range(1001)]
dp[1], dp[3], dp[4] = 1, 1, 1

for i in range(5, N+1):
    if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
        dp[i] = 1

print("SK" if dp[N] else "CY")
