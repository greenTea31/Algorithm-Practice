import sys
input = sys.stdin.readline


def recur(cur, p, f, s, v, cost):
    global minimum_cost, ans

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if minimum_cost > cost:
            minimum_cost = cost
            ans = selected[:]
        return

    if cur == N:
        return

    selected.append(cur+1)
    recur(cur+1, p+foods[cur][0], f+foods[cur][1], s+foods[cur][2], v+foods[cur][3], cost+foods[cur][4])
    selected.pop()
    recur(cur+1, p, f, s, v, cost)


N = int(input())
mp, mf, ms, mv = map(int, input().split())
foods = []
selected = []
ans = []
minimum_cost = 7501

for _ in range(N):
    foods.append(list(map(int, input().split())))

recur(0, 0, 0, 0, 0, 0)

if minimum_cost == 7501:
    print(-1)
else:
    print(minimum_cost)
    print(*ans)


