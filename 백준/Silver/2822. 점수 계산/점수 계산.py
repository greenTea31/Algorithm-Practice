import sys
input = sys.stdin.readline

numbers = []

for i in range(8):
    numbers.append([int(input()), i+1])

numbers.sort(key=lambda x: x[0])
ans = 0

for i in range(3, 8):
    ans += numbers[i][0]

print(ans)

index = []

for i in range(3, 8):
    index.append(numbers[i][1])

index.sort()

for num in index:
    print(num, end=' ')
