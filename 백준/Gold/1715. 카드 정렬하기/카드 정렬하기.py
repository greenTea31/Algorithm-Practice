import sys
import heapq
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    heapq.heappush(pq, int(input()))

ans = 0

for _ in range(N-1):
    a, b = heapq.heappop(pq), heapq.heappop(pq)
    ans += (a+b)
    heapq.heappush(pq, (a+b))

print(ans)