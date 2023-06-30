import sys
input = sys.stdin.readline

N = int(input())
number_card = list(map(int, input().split()))
hash_map = set()

for card in number_card:
    hash_map.add(card)

M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in hash_map:
        print(1, end=' ')
    else:
        print(0, end=' ')