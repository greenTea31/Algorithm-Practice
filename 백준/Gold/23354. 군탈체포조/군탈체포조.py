import sys
import heapq
input = sys.stdin.readline


def dijkstra(st_i, st_j, t_board):
    pq = []
    heapq.heappush(pq, [0, st_i, st_j])
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    while pq:
        cur = heapq.heappop(pq)

        if cur[0] != t_board[cur[1]][cur[2]]:
            continue

        for i in range(4):
            ni, nj = cur[1] + di[i], cur[2] + dj[i]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if t_board[ni][nj] <= t_board[cur[1]][cur[2]] + board[ni][nj]:
                continue
            t_board[ni][nj] = t_board[cur[1]][cur[2]] + board[ni][nj]
            heapq.heappush(pq, [t_board[ni][nj], ni, nj])


def perm(index):
    if index == length:
        check()
        return

    for i in range(length):
        if visited[i]:
            continue
        visited[i] = True
        numbers[index] = i
        perm(index+1)
        visited[i] = False


def check():
    global answer
    temp_answer = 0
    temp_answer += initial_dist[soldier[numbers[0]][0]][soldier[numbers[0]][1]]

    for i in range(length-1):
        temp_answer += dist[numbers[i]][soldier[numbers[i+1]][0]][soldier[numbers[i+1]][1]]

    temp_answer += dist[numbers[length-1]][start_i][start_j]

    answer = min(answer, temp_answer)


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
start_i, start_j = 0, 0
soldier = []
answer = 1000001

for i in range(N):
    for j in range(N):
        if board[i][j] == -1:
            start_i = i
            start_j = j
        elif board[i][j] == 0:
            soldier.append([i, j])

board[start_i][start_j] = 0
length = len(soldier)

if not length:
    print(0)
    exit(0)

initial_dist = [[1000001 for _ in range(N)] for _ in range(N)]
dist = [[[1000001 for _ in range(N)] for _ in range(N)] for _ in range(length)]
visited = [False for _ in range(length)]
numbers = [0 for _ in range(length)]

initial_dist[start_i][start_j] = 0

for i in range(length):
    dist[i][soldier[i][0]][soldier[i][1]] = 0

dijkstra(start_i, start_j, initial_dist)

for i in range(length):
    dijkstra(soldier[i][0], soldier[i][1], dist[i])

perm(0)

print(answer)
