import sys
input = sys.stdin.readline


def query(L, R, node_num, node_l, node_r):
    if R < node_l or node_r < L:
        return 1
    elif L <= node_l and node_r <= R:
        return seg_tree[node_num]
    else:
        mid = (node_l + node_r) // 2
        return query(L, R, node_num*2, node_l, mid) * query(L, R, node_num*2 + 1, mid + 1, node_r)


def update(i, val):
    i += nodeCounts // 2 - 1
    seg_tree[i] = val

    while i > 1:
        i >>= 1
        seg_tree[i] = seg_tree[2*i] * seg_tree[2*i + 1]


while True:
    try:
        N, K = map(int, input().split())
        numbers = list(map(int, input().split()))
        nodeCounts = 1

        while nodeCounts < 2 * N:
            nodeCounts <<= 1

        seg_tree = [1 for _ in range(nodeCounts)]

        for index, number in enumerate(numbers):
            if number > 0:
                number = 1
            elif number < 0:
                number = -1
            update(index + 1, number)

        for round in range(K):
            a, b, c = map(str, input().split())
            b, c = int(b), int(c)
            if a == "C":
                if c > 0:
                    c = 1
                elif c < 0:
                    c = -1
                update(b, c)
            else:
                ans = query(b, c, 1, 1, nodeCounts // 2)
                output = 0

                if ans > 0:
                    output = "+"
                elif ans < 0:
                    output = "-"

                print(output, end="")

        print()
    except Exception:
        break

