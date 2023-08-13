import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(123456)

# SCC별로 쪼개고 inDegree 0인 개수 세면 다 넘어갈듯


def dfs(cur):
    global cnt, SN
    cnt += 1
    visited[cur] = cnt
    stack.append(cur)

    result = visited[cur]

    for nxt in edges[cur]:
        if visited[nxt] == 0:
            result = min(result, dfs(nxt))
        elif not finished[nxt]:
            result = min(result, visited[nxt])

    if result == visited[cur]:
        curScc = []

        while True:
            t = stack.pop()
            curScc.append(t)
            finished[t] = True
            sn[t] = SN
            if t == cur:
                break

        SCC.append(curScc)
        SN += 1

    return result


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    edges = collections.defaultdict(list)
    cnt = 0
    SN = 0
    visited = [0 for _ in range(N+1)]
    finished = [0 for _ in range(N+1)]
    sn = [0 for _ in range(N+1)]
    stack = []
    SCC = []

    for _ in range(M):
        x, y = map(int, input().split())
        edges[x].append(y)

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)

    indegree = [0 for _ in range(SN)]

    # 간선 i, j에 대해 i와 j가 서로 다른 SCC에 속하면 j가 속한 SCC의 inDegree 상승시키고 0인거 개수 찾기
    for i in range(1, N+1):
        for nxt in edges[i]:
            if sn[i] != sn[nxt]:
                indegree[sn[nxt]] += 1

    answer = 0

    for num in indegree:
        if num == 0:
            answer += 1

    print(answer)
