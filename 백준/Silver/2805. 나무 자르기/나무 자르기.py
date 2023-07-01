import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))
max_height = 0

for height in heights:
    max_height = max(max_height, height)

s, e = 0, max_height
answer = 0

while s <= e:
    mid = (s + e) // 2
    height_sum = 0

    for height in heights:
        if height > mid:
            height_sum += height - mid

    if height_sum == M:
        answer = mid
        break
    elif height_sum < M:
        e = mid - 1
    else:
        s = mid + 1
        answer = mid

print(answer)
