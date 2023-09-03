import sys
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

distance = []

for i in range(N-1):
    distance.append(abs(numbers[i] - numbers[i+1]))

temp = gcd(distance[0], distance[1])

if len(distance) >= 3:
    for i in range(2, N-1):
        temp = gcd(temp, distance[i])

ans = 0

for i in range(N-1):
    cur = numbers[i]
    while cur + temp < numbers[i+1]:
        cur += temp
        ans += 1

print(ans)
