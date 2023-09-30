import sys
input = sys.stdin.readline

N, M = map(int, input().split())
people = list(map(int, input().split()))
friends = set(map(int, input().split()))
ans = 0

for i in range(M):
    if people[i] not in friends:
        ans += 1

print(ans)
