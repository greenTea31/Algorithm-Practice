N, M = map(int, input().split())
robot_r, robot_c, robot_d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    # 현재 칸이 청소되지 않은 경우 현재 칸을 청소한다
    if board[robot_r][robot_c] == 0:
        board[robot_r][robot_c] = 2
        answer += 1

    temp = board[robot_r][robot_c]
    board[robot_r][robot_c] = 3

    board[robot_r][robot_c] = temp
    clean_area = False

    for i in range(4):
        nd = robot_d - i
        if nd < 0:
            nd += 4
        nr = robot_r + dr[nd]
        nc = robot_c + dc[nd]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        # 청소되지 않은 빈 칸이 있는 경우
        if board[nr][nc] == 0:
            clean_area = True
            break

    # 청소하러 간다
    if clean_area:
        robot_d -= 1
        if robot_d < 0:
            robot_d += 4
        nr = robot_r + dr[robot_d]
        nc = robot_c + dc[robot_d]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if board[nr][nc] == 0:
            robot_r = nr
            robot_c = nc
        continue

    # 청소되지 않은 빈칸이 없는 경우
    hd = (robot_d + 2) % 4
    hr = robot_r + dr[hd]
    hc = robot_c + dc[hd]
    if hr < 0 or hr >= N or hc < 0 or hc >= M or board[hr][hc] == 1:
        print(answer)
        exit(0)
    robot_r = hr
    robot_c = hc
