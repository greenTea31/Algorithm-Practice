import sys
import collections
input = sys.stdin.readline

N, K = map(int, input().split())
if N == K:
    print(0)
    print(1)
    exit(0)
answer = abs(K-N)
count = 0
Q = collections.deque()
Q.append([N, 0])
visited = [100001 for _ in range(200001)]
visited[N] = 0

while Q:
    cur = Q.popleft()

    if answer < cur[1]:
        break

    if cur[0]+1 == K and cur[1]+1 <= answer:
        answer = cur[1]+1
        count += 1
        continue
    if cur[0]-1 == K and cur[1]+1 <= answer:
        answer = cur[1]+1
        count += 1
        continue
    if cur[0]*2 == K and cur[1]+1 <= answer:
        answer = cur[1]+1
        count += 1
        continue

    if cur[0]+1 <= 200000 and visited[cur[0]+1] >= cur[1]+1:
        visited[cur[0]+1] = cur[1]+1
        Q.append([cur[0]+1, cur[1]+1])
    if cur[0]-1 >= 0 and visited[cur[0]-1] >= cur[1]+1:
        visited[cur[0]-1] = cur[1]+1
        Q.append([cur[0]-1, cur[1]+1])
    if 2*cur[0] <= 200000 and visited[2*cur[0]] >= cur[1]+1:
        visited[2*cur[0]] = cur[1]+1
        Q.append([2*cur[0], cur[1]+1])

print(answer)
print(count)
