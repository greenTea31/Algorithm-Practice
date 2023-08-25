import sys
import collections
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
diction = collections.defaultdict(int)

for num in numbers:
    diction[num] += 1

ans = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if numbers[i] - numbers[j] == numbers[i]:
            if diction[numbers[i]] >= 3:
                ans += 1
                break
        elif numbers[i] - numbers[j] == numbers[j]:
            if diction[numbers[j]] >= 2:
                ans += 1
                break
        elif diction[numbers[i] - numbers[j]] >= 1:
            ans += 1
            break

print(ans)
