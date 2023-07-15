import sys
sys.setrecursionlimit(123123123)
input = sys.stdin.readline

# 백트래킹 + memoization
# cur일에서, 앞으로 최선 선택시 얻는 최대 이득


def recur(cur):
    if cur > N:
        return -10000000000
    if cur == N:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = max(recur(cur + sangdam[cur][0]) + sangdam[cur][1], recur(cur + 1))
    return dp[cur]


N = int(input())
sangdam = [list(map(int, input().split())) for _ in range(N)]
dp = [-1 for _ in range(N)]
print(recur(0))



