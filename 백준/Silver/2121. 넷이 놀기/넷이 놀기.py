import sys
import collections
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
hash_map = collections.defaultdict(set)
dots = []

for _ in range(N):
    x, y = map(int, input().split())
    hash_map[x].add(y)
    dots.append([x, y])

answer = 0

for x, y in dots:
    if y + B in hash_map[x] and y + B in hash_map[x+A] and y in hash_map[x+A]:
        answer += 1

print(answer)