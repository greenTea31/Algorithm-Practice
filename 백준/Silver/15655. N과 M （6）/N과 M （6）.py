import sys
input = sys.stdin.readline


# 숫자 중에서 조합 구하기 (선택으로 구하기)
def recur(cur, picked):
    if picked == M:
        for num in selected:
            print(num, end=' ')
        print()
        return
    if cur == N:
        return

    selected[picked] = numbers[cur]
    recur(cur+1, picked+1)
    selected[picked] = 0
    recur(cur+1, picked)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
selected = [0 for _ in range(M)]
recur(0, 0)