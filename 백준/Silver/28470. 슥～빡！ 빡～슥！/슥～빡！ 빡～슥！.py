import sys
import math
input = sys.stdin.readline

N = int(input())

attacks = list(map(int, input().split()))
evades = list(map(int, input().split()))
delta = list(map(float, input().split()))
ans = 0

for i in range(N):
    cal_delta = delta[i] * 10
    if cal_delta <= 10:
        ans -= (cal_delta * evades[i] // 10)
        ans += attacks[i]
    else:
        ans += (cal_delta * attacks[i] // 10)
        ans -= evades[i]
    ans = math.floor(ans)

print(ans)