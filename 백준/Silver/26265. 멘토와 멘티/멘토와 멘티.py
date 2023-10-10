import sys
input = sys.stdin.readline

N = int(input())

people = []

for _ in range(N):
    people.append(list(input().split()))

people.sort(key=lambda x: x[1], reverse=True)
people.sort(key=lambda x: x[0])

for person in people:
    print(person[0], person[1])
