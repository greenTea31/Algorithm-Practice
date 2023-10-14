import sys
import collections
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
times = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
endtime = [0 for _ in range(N+1)]

for i in range(1, N+1):
    time, count, *numbers = map(int, input().split())
    times[i] = time
    indegree[i] = count

    for num in numbers:
        edges[num].append(i)

zero_degree = collections.deque([])

for i in range(1, N+1):
    if indegree[i] == 0:
        endtime[i] = times[i]
        zero_degree.append(i)

while zero_degree:
    cur = zero_degree.popleft()
    for nxt in edges[cur]:
        indegree[nxt] -= 1
        endtime[nxt] = max(endtime[nxt], endtime[cur] + times[nxt])
        if indegree[nxt] == 0:
            zero_degree.append(nxt)

print(max(endtime))
