import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline


# DP, d[n] = d[n-1] + d[n-2]

def recur(cur): # 2 x cur크기의 직사각형을 채우는 방법의 수
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = recur(cur-1) + recur(cur-2)
    dp[cur] %= 10007
    return dp[cur]


n = int(input())
dp = [-1 for _ in range(n+1)]
dp[0], dp[1] = 1, 1
print(recur(n))