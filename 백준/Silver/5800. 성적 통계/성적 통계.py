import sys
input = sys.stdin.readline

K = int(input())
classes = []

for _ in range(K):
    classes.append(list(map(int, input().split()))[1:])
    classes[-1].sort(reverse=True)

for i in range(1, K+1):
    print(f"Class {i}")
    max_value = max(classes[i-1])
    min_value = min(classes[i-1])
    largest_gap = 0
    length = len(classes[i-1])

    for j in range(length-1):
        largest_gap = max(largest_gap, classes[i-1][j] - classes[i-1][j+1])

    print(f"Max {max_value}, Min {min_value}, Largest gap {largest_gap}")
