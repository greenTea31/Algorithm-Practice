import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
s, e = 0, 0
temp_sum = numbers[0]
now_length = 1
answer = 100001

while e < N:
    if temp_sum < S:
        e += 1

        if e == N:
            break

        now_length += 1
        temp_sum += numbers[e]
    else:
        answer = min(answer, now_length)

        if now_length == 1:
            break

        temp_sum -= numbers[s]
        s += 1
        now_length -= 1

print(answer if answer != 100001 else 0)
