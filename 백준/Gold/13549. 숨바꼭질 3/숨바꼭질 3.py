import sys
import collections
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False for _ in range(200001)]

if N == K:
    print(0)
    exit(0)

answer = abs(K-N)
Q = collections.deque()
Q.append([N, 0])

while Q:
    cur = Q.popleft()
    if cur[0] * 2 <= 200000 and not visited[cur[0]*2]:
        if cur[0] * 2 == K:
            answer = cur[1]
            break
        visited[cur[0]*2] = True
        Q.append([cur[0]*2, cur[1]])
    if cur[0]-1 >= 0 and not visited[cur[0]-1]:
        if cur[0]-1 == K:
            answer = cur[1]+1
            break
        visited[cur[0]-1] = True
        Q.append([cur[0]-1, cur[1]+1])
    if cur[0]+1 <= 200000 and not visited[cur[0]+1]:
        if cur[0]+1 == K:
            answer = cur[1]+1
            break
        visited[cur[0]+1] = True
        Q.append([cur[0]+1, cur[1]+1])

print(answer)
