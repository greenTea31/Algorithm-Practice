import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(123456)

# 다른 모든 구역에 도달할 수 있는 시작지점을 찾아라
# SCC 돌리고 indegree == 0인 scc가 하나만 존재해야 함
# SCC 구하는게 O(V+E), 정점과 간선은 10만까지


def dfs(cur):
    global cnt, scc
    cnt += 1
    dfsn[cur] = cnt
    stack.append(cur)
    result = dfsn[cur]

    for nxt in edges[cur]:
        if dfsn[nxt] == 0:
            result = min(result, dfs(nxt))
        elif not finished[nxt]:
            result = min(result, dfsn[nxt])

    if result == dfsn[cur]:
        cur_scc = []

        while True:
            t = stack.pop()
            cur_scc.append(t)
            finished[t] = True
            scc_parent[t] = scc
            if t == cur:
                break

        SCC.append(cur_scc)
        scc += 1

    return result


T = int(input())

for k in range(T):
    N, M = map(int, input().split())
    edges = collections.defaultdict(list)
    dfsn = [0 for _ in range(N)]
    scc_parent = [0 for _ in range(N)]
    finished = [False for _ in range(N)]
    stack = []
    SCC = []
    scc = 0
    cnt = 0

    for _ in range(M):
        A, B = map(int, input().split())
        edges[A].append(B)

    for i in range(N):
        if dfsn[i] == 0:
            dfs(i)

    indegree = [0 for _ in range(scc)]

    for i in range(N):
        for nxt in edges[i]:
            if scc_parent[i] != scc_parent[nxt]:
                indegree[scc_parent[nxt]] += 1

    ans = []
    confuse = 0

    for i in range(scc):
        if indegree[i] == 0:
            confuse += 1
            if confuse >= 2:
                print("Confused")
                break
            for j in range(N):
                if scc_parent[j] == i:
                    ans.append(j)

    if confuse == 1:
        for num in ans:
            print(num)

    print()

    if k < T-1:
        input()







