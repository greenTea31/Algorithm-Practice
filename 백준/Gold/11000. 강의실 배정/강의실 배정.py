import sys
import heapq
input = sys.stdin.readline

N = int(input())
studys = []
studyrooms = [0]

for _ in range(N):
    start, end = map(int, input().split())
    studys.append([start, end])

studys.sort(key=lambda x: (x[0], x[1]))
ans = 1

for study in studys:
    if studyrooms[0] <= study[0]:
        heapq.heappop(studyrooms)
        heapq.heappush(studyrooms, study[1])
    else:
        ans += 1
        heapq.heappush(studyrooms, study[1])

print(ans)