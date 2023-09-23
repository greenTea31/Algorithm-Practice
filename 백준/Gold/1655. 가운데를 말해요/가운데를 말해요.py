import heapq
import sys

max_pq = []
min_pq = []

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    min_size = len(min_pq)
    max_size = len(max_pq)
    if min_size == max_size:
        if min_size != 0 and min_pq[0] < num:
            heapq.heappush(max_pq, (-min_pq[0], min_pq[0]))
            heapq.heappop(min_pq)
            heapq.heappush(min_pq, num)
        else:
            heapq.heappush(max_pq, (-num, num))
    elif max_size > min_size:
        if max_pq[0][1] > num:
            heapq.heappush(min_pq, max_pq[0][1])
            heapq.heappop(max_pq)
            heapq.heappush(max_pq, (-num, num))
        else:
            heapq.heappush(min_pq, num)
    print(max_pq[0][1])