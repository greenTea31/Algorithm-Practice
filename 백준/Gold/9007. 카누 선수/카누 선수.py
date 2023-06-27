import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k, n = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    arr4 = list(map(int, input().split()))
    sum_arr1 = []
    sum_arr2 = []

    for i in range(n):
        for j in range(n):
            sum_arr1.append(arr1[i] + arr2[j])
            sum_arr2.append(arr3[i] + arr4[j])

    sum_arr1.sort()
    sum_arr2.sort()
    s, e = 0, n**2 - 1
    answer = 0
    min_diff = 1010101010
    min_sum = 1010101010

    while s < n**2 and e >= 0:
        temp_sum = sum_arr1[s] + sum_arr2[e]
        now_diff = abs(temp_sum - k)

        if now_diff < min_diff:
            answer = temp_sum
            min_sum = temp_sum
            min_diff = now_diff
        elif now_diff == min_diff and temp_sum < min_sum:
            answer = temp_sum
            min_sum = temp_sum

        if temp_sum < k:
            s += 1
        elif temp_sum > k:
            e -= 1
        else:
            answer = k
            break

    print(answer)