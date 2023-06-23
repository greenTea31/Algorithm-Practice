import sys
input = sys.stdin.readline

N = int(input())
primes = [0]
visited = set()
bound = min(N+1, 4000001)

for i in range(2, bound):
    if i not in visited:
        primes.append(i)
        visited.add(i)
        for j in range(i*2, bound, i):
            visited.add(j)

length = len(primes)
p_sum = [0 for _ in range(length)]

for i in range(1, length):
    p_sum[i] = p_sum[i-1] + primes[i]

answer, s, e = 0, 0, 1

while e < length:
    temp_sum = p_sum[e] - p_sum[s]
    if temp_sum == N:
        answer += 1
        s, e = s+1, e+1
    elif temp_sum < N:
        e += 1
    else:
        if e - s == 1:
            s, e = s+1, e+1
        else:
            s += 1

print(answer)