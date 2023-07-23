import sys
import collections
input = sys.stdin.readline

# 사방탐색 + BFS로 그냥 계산
def get_bingsan_count(start_r, start_c):
    q = collections.deque([])
    visited[start_r][start_c] = True
    q.append([start_r, start_c])

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            next_r, next_c = cur_r + dr[i], cur_c + dc[i]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M or visited[next_r][next_c] or board[next_r][next_c] == 0:
                continue
            visited[next_r][next_c] = True
            q.append([next_r, next_c])


def melting_bingsan(r, c):
    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
            continue
        if prev_board[next_r][next_c] == 0 and board[r][c] > 0:
            board[r][c] -= 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
prev_board = []

for i in range(N):
    prev_board.append(board[i][:])

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
day = 0

# 빙산이 방금 녹은건 옆에 빙산에 영향을 미치면 안됨

while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    b_count = 0
    day += 1

    for i in range(N):
        for j in range(M):
            melting_bingsan(i, j)

    for i in range(N):
        prev_board[i] = board[i][:]

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                b_count += 1
                get_bingsan_count(i, j)

    if b_count != 1:
        if b_count == 0:
            day = 0
        break

print(day)
