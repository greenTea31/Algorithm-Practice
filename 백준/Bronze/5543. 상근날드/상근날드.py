import sys
input = sys.stdin.readline

hamburger = []
soda = []

for _ in range(3):
    hamburger.append(int(input()))

for _ in range(2):
    soda.append(int(input()))

hamburger.sort()
soda.sort()

print(hamburger[0] + soda[0] - 50)
