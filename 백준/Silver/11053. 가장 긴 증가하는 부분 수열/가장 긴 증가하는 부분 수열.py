import sys
input = sys.stdin.readline

# LIS

N = int(input())
numbers = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1, N):
    max_value = 0
    for j in range(i):
        if numbers[j] < numbers[i]:
            max_value = max(max_value, dp[j])
    dp[i] = max_value + 1

print(max(dp))
