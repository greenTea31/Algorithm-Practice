import sys
import collections
input = sys.stdin.readline

N = int(input())
number_cards = list(map(int, input().split()))
hash_map = collections.defaultdict(int)

for number in number_cards:
    hash_map[number] += 1

M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    print(hash_map[number], end=" ")