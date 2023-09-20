import sys
input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
    return a


A, B = map(int, input().split())
print(A*B//gcd(A,B))
