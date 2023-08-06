import sys
import collections

N = int(sys.stdin.readline())
graph = collections.defaultdict(list)
parent = collections.defaultdict(int)
Q = collections.deque([])
discovered = [False for _ in range(N+1)]

for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

Q.append(1)

while Q:
    cur = Q.popleft()
    for i in graph[cur]:
        if discovered[i]:
            continue
        parent[i] = cur
        discovered[i] = True
        Q.append(i)

for i in range(2, N+1):
    print(parent[i])
