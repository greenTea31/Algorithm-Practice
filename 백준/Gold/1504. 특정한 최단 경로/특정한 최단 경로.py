import heapq

cantFlag = False


def dijkstra(start, end):
    global cantFlag
    dist = [800001 for _ in range(N + 1)]
    dist[start] = 0
    pq = [[dist[start], start]]

    while pq:
        cur_d, cur = heapq.heappop(pq)
        if dist[cur] != cur_d:
            continue
        if cur == end:
            return dist[cur]
        for nxt_w, nxt in edge[cur]:
            if dist[nxt] <= dist[cur] + nxt_w:
                continue
            dist[nxt] = dist[cur] + nxt_w
            heapq.heappush(pq, [dist[nxt], nxt])

    if dist[end] == 800001:
        cantFlag = True
        return -1
    return dist[end]


N, E = map(int, input().split())
edge = [[] for _ in range(N+1)]


for _ in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

v1, v2 = map(int, input().split())

answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) +
             dijkstra(v1, N))

print(-1 if cantFlag else answer)
