import sys
import heapq
input = sys.stdin.readline


pq = []
N = int(input())
dasom = 0
answer = 0

for i in range(N):
    if i == 0:
        dasom = -int(input())
    else:
        heapq.heappush(pq, -int(input()))

while pq and dasom >= pq[0]:
    temp = heapq.heappop(pq)
    temp += 1
    dasom -= 1
    answer += 1
    heapq.heappush(pq, temp)

print(answer)
