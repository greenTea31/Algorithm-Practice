import sys
input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
    temp = list(map(int, input().split()))
    numbers.append(sum(temp[1:]))

numbers.sort()

for i in range(1, N):
    numbers[i] += numbers[i-1]

print(sum(numbers))
