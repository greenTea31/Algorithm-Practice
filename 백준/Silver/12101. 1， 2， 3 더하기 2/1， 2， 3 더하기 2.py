import sys
input = sys.stdin.readline


def recur(hap, sum_hap):
    if sum_hap > n:
        return
    if sum_hap == n:
        hap_list.append(hap)
        return
    recur(hap+"+1", sum_hap+1)
    recur(hap + "+2", sum_hap + 2)
    recur(hap + "+3", sum_hap + 3)


n, k = map(int, input().split())
hap_list = []
recur("1", 1)
recur("2", 2)
recur("3", 3)

if len(hap_list) > k-1:
    print(hap_list[k-1])
else:
    print(-1)