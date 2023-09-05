import sys
input = sys.stdin.readline


def dfs(cur):
    global ans
    lst = [cur]

    while lst:
        visited[lst[-1]] = True
        nxt = edges[lst[-1]]

        if visited[nxt]:
            if not finished[nxt]:
                ans += 1
                finished[nxt] = True
                while lst[-1] != nxt:
                    finished[lst[-1]] = True
                    lst.pop()
                    ans += 1
        else:
            visited[nxt] = True
            lst.append(nxt)
            continue

        finished[lst[-1]] = True
        lst.pop()

    return ans


T = int(input())

for _ in range(T):
    n = int(input())
    students = list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    finished = [False for _ in range(n+1)]
    edges = [0 for _ in range(n+1)]

    for i in range(n):
        edges[i+1] = students[i]

    answer = n

    for i in range(1, n+1):
        if visited[i]:
            continue
        ans = 0
        answer -= dfs(i)

    print(answer)
