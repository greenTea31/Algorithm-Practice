import sys
input = sys.stdin.readline

# 조건 따라 완탐

N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
answer = 0

# 가로 판별
for i in range(N):
    flag = True

    for j in range(N-1):
        if abs(road[i][j] - road[i][j+1]) > 1:
            flag = False
            break
        if road[i][j] + 1 == road[i][j+1]:
            if j - (L-1) < 0:
                flag = False
                break
            for k in range(j - (L-1), j+1):
                if road[i][k] != road[i][j] or visited[i][k]:
                    flag = False
                    break
            if not flag:
                break
            for k in range(j - (L-1), j+1):
                visited[i][k] = True
        if road[i][j] == road[i][j+1] + 1:
            if j + L >= N:
                flag = False
                break
            for k in range(j+1, j+L+1):
                if road[i][j+1] != road[i][k] or visited[i][k]:
                    flag = False
                    break
            if not flag:
                break
            for k in range(j+1, j+L+1):
                visited[i][k] = True

    if flag:
        answer += 1

visited = [[False for _ in range(N)] for _ in range(N)]

# 세로 판별
for j in range(N):
    flag = True

    for i in range(N-1):
        if abs(road[i][j] - road[i+1][j]) > 1:
            flag = False
            break
        if road[i][j] + 1 == road[i+1][j]:
            if i - (L - 1) < 0:
                flag = False
                break
            for k in range(i - (L - 1), i+1):
                if road[k][j] != road[i][j] or visited[k][j]:
                    flag = False
                    break
            if not flag:
                break
            for k in range(i - (L-1), i+1):
                visited[k][j] = True
        if road[i][j] == road[i+1][j] + 1:
            if i + L >= N:
                flag = False
                break
            for k in range(i + 1, i + L + 1):
                if road[i + 1][j] != road[k][j] or visited[k][j]:
                    flag = False
                    break
            if not flag:
                break
            for k in range(i+1, i+L+1):
                visited[k][j] = True

    if flag:
        answer += 1

print(answer)