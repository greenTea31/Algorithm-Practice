import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
s, e = 0, N-1
min_diff = 2000000005
ans_s, ans_e = 0, 0

while s < e:
    temp_sum = weights[s] + weights[e]

    if temp_sum == 0:
        ans_s, ans_e = weights[s], weights[e]
        break

    cur_diff = abs(temp_sum)

    if cur_diff < min_diff:
        min_diff = cur_diff
        ans_s, ans_e = weights[s], weights[e]

    if temp_sum > 0:
        e -= 1
    else:
        s += 1

print(f"{ans_s} {ans_e}")
