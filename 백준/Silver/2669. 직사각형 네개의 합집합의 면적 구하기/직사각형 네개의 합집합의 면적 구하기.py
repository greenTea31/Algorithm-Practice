import sys
input = sys.stdin.readline

board = [[False for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = True

ans = 0

for i in range(101):
    for j in range(101):
        if board[i][j]:
            ans += 1

print(ans)