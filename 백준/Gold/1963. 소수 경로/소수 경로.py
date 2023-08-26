import sys
import collections
input = sys.stdin.readline

visited = set()
primes = set()

for i in range(2, 10001):
    if i in visited:
        continue
    visited.add(i)
    primes.add(i)

    for j in range(2*i, 10001, i):
        visited.add(j)

edges = collections.defaultdict(list)

for num1 in primes:
    for num2 in primes:
        if 1000 <= num1 <= 9999 and 1000 <= num2 <= 9999:
            str_num1, str_num2 = str(num1), str(num2)
            diff_count = 0
            for i in range(4):
                if str_num1[i] != str_num2[i]:
                    diff_count += 1
            if diff_count == 1:
                edges[num1].append(num2)

T = int(input())

for _ in range(T):
    bfs_visited = set()
    A, B = map(int, input().split())
    q = collections.deque([])
    q.append([A, 0])
    flag = False
    bfs_visited.add(A)

    while q:
        cur_number, cur_dist = q.popleft()

        if cur_number == B:
            print(cur_dist)
            flag = True
            break

        for nxt_number in edges[cur_number]:
            if nxt_number in bfs_visited:
                continue
            bfs_visited.add(nxt_number)
            q.append([nxt_number, cur_dist+1])

    if not flag:
        print("Impossible")
