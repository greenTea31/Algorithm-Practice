import sys
import collections
input = sys.stdin.readline

# 특정 정점에서 가장 먼 곳 구하고 거기서 한번 더 가장 먼 곳 구하기


def bfs(start):
    q = collections.deque([])
    q.append([start, 0])

    while q:
        cur, prev = q.popleft()

        for nxt, weight in edges[cur]:
            if nxt == prev:
                continue
            distance[nxt] = distance[cur] + weight
            q.append([nxt, cur])


n = int(input())
edges = collections.defaultdict(list)

for _ in range(n-1):
    start, end, weight = map(int, input().split())
    edges[start].append([end, weight])
    edges[end].append([start, weight])

distance = [0 for _ in range(n+1)]
bfs(1)
max_index, max_weight = 0, 0

for i in range(n+1):
    if max_weight < distance[i]:
        max_index, max_weight = i, distance[i]

distance = [0 for _ in range(n+1)]
bfs(max_index)

max_index, max_weight = 0, 0

for i in range(n+1):
    if max_weight < distance[i]:
        max_index, max_weight = i, distance[i]

print(max(distance))
