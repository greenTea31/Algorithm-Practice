import sys
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


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
    cur = numbers[i+1] - numbers[i]
    cur //= temp
    ans += (cur-1)

print(ans)
