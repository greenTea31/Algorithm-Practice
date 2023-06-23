import sys
input = sys.stdin.readline

n = int(input())

px, py = map(int, input().split())
px += 500000
py += 500000
start_x, start_y = px, py
h = [0 for _ in range(1000001)]
v = [0 for _ in range(1000001)]

for i in range(1, n):
    xi, yi = map(int, input().split())
    xi += 500000
    yi += 500000

    if px == xi:
        h[min(py, yi)] += 1
        h[max(py, yi)] -= 1
    if py == yi:
        v[min(px, xi)] += 1
        v[max(px, xi)] -= 1

    px, py = xi, yi

if start_x == px:
    h[min(start_y, py)] += 1
    h[max(start_y, py)] -= 1
if start_y == py:
    v[min(start_x, px)] += 1
    v[max(start_x, px)] -= 1

for j in range(1, 1000001):
    h[j] += h[j-1]
    v[j] += v[j-1]

print(max(max(h), max(v)))