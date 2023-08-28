import sys
input = sys.stdin.readline


def hanoi(num, start, via, end):
    if num == 0:
        return
    hanoi(num-1, start, end, via)
    print(f'{start} {end}')
    hanoi(num-1, via, start, end)


N = int(input())
print(2**N-1)
hanoi(N, 1, 2, 3)