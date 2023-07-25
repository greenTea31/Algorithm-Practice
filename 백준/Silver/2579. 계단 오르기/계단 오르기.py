import sys
input = sys.stdin.readline

# Bottom-up dp

count = int(input())
chairs = [0, 0]

for _ in range(count):
    chairs.append(int(input()))

dp = [[0, 0] for _ in range(count+2)]

for i in range(2, count+2):
    dp[count][1] = 0
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + chairs[i]
    dp[i][1] = dp[i-1][0] + chairs[i]

print(max(dp[count][0], dp[count][1], dp[count+1][0], dp[count+1][1]))

