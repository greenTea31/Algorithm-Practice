import sys
import math
input = sys.stdin.readline

N, X = map(int, input().split())
essence = list(map(int, input().split()))
length = len(essence)
essence.sort()
s, e = 0, length - 1
answer = 0
remain = length

while s <= e:
    if essence[e] >= X:
        answer += 1
        remain -= 1
        e -= 1
        continue
    
    if s == e:
        break

    temp_sum = essence[s] + essence[e]
    if temp_sum >= math.ceil(X / 2):
        answer += 1
        remain -= 2
        s += 1
        e -= 1
    else:
        s += 1

answer += remain // 3
print(answer)