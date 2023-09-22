import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    for number in numbers:
        for i in range(1, M+1):
            if i - number < 0:
                continue
            dp[i] += dp[i - number]

    print(dp[M])
