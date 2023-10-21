import sys
import heapq
input = sys.stdin.readline

"""
트리셋? 파이썬엔 없는데
우선순위큐 2개 쓰고 delete 체크 하던가...
"""

N = int(input())
min_heap = []
max_heap = []
num_to_difficult = {}

for _ in range(N):
    P, L = map(int, input().split())
    num_to_difficult[P] = L
    heapq.heappush(min_heap, [L, P])
    heapq.heappush(max_heap, [-L, -P])

M = int(input())

for _ in range(M):
    command, *number = input().split()
    length = len(number)

    for i in range(length):
        number[i] = int(number[i])

    if command == "add":
        P, L = number[0], number[1]
        num_to_difficult[P] = L
        heapq.heappush(min_heap, [L, P])
        heapq.heappush(max_heap, [-L, -P])
    elif command == "recommend":
        if number[0] == 1:
            while True:
                L, P = heapq.heappop(max_heap)
                if num_to_difficult[-P] == -L:
                    heapq.heappush(max_heap, [L, P])
                    print(-P)
                    break
        else:
            while True:
                L, P = heapq.heappop(min_heap)
                if num_to_difficult[P] == L:
                    heapq.heappush(min_heap, [L, P])
                    print(P)
                    break
    elif command == "solved":
        P = number[0]
        num_to_difficult[P] = -1
