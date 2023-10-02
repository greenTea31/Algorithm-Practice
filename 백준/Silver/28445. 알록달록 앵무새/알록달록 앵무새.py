import sys
input = sys.stdin.readline

father = set(input().split())
mother = set(input().split())
parent = list(father.union(mother))
parent.sort()

for i in parent:
    for j in parent:
        print(i, j)
