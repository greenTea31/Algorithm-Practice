import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(2000)

N, M = map(int, input().split())
edges = collections.defaultdict(list)

for _ in range(N-1):
    A, B, C = map(int, input().split())
    edges[A].append([C, B])
    edges[B].append([C, A])

for _ in range(M):
    A, B = map(int, input().split())
    Q = collections.deque()
    Q.append([A, 0, 0]) # 정점, 거리, 이전점

    while Q:
        cur = Q.popleft()

        if cur[0] == B:
            print(cur[1])
            break

        for nxt in edges[cur[0]]:
            if nxt[1] == cur[2]:
                continue
            Q.append([nxt[1], cur[1] + nxt[0], cur[0]])
