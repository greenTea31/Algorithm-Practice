import sys
input = sys.stdin.readline

N = int(input())
numbers = set(map(int, input().split()))
numbers = list(numbers)
numbers.sort()

for num in numbers:
    print(num, end=' ')
