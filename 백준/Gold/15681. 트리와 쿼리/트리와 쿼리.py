import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(123456)

# 트리 상단에서 dfs 진행하면서 서브쿼리 개수 갱신하고 출력하기


def dfs(cur, prev):
    for nxt in edges[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)
        subtree[cur] += subtree[nxt]

    return subtree[cur]


N, R, Q = map(int, input().split())
edges = collections.defaultdict(list)
subtree = [1 for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

dfs(R, 0)

for _ in range(Q):
    print(subtree[int(input())])
