import sys
import collections
input = sys.stdin.readline

# 입력과 동시에 전파 x, 출력 직전에 전파


def bfs(cur):
    q = collections.deque([])
    q.append([cur, 0])

    while q:
        cur, prev = q.popleft()

        for nxt in edges[cur]:
            if nxt == prev:
                continue
            score[nxt] += score[cur]
            q.append([nxt, cur])


n, m = map(int, input().split())
edges = collections.defaultdict(list)
score = [0 for _ in range(n+1)]
parent_node = list(map(int, input().split()))

for i in range(1, n):
    edges[i+1].append(parent_node[i])
    edges[parent_node[i]].append(i+1)

for _ in range(m):
    i, w = map(int, input().split())
    score[i] += w

bfs(1)

for i in range(1, n+1):
    print(score[i], end=' ')

