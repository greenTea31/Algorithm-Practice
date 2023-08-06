import sys
input = sys.stdin.readline

# 전위, 중위, 후위순회 구현


def preorder(cur):
    print(diction[cur], end='')
    if cur*2 in diction:
        preorder(cur*2)
    if cur*2+1 in diction:
        preorder(cur*2+1)


def inorder(cur):
    if cur*2 in diction:
        inorder(cur*2)
    print(diction[cur], end='')
    if cur*2+1 in diction:
        inorder(cur*2+1)


def postorder(cur):
    if cur*2 in diction:
        postorder(cur*2)
    if cur*2+1 in diction:
        postorder(cur*2+1)
    print(diction[cur], end='')


N = int(input())
diction = {}
diction['A'] = 1
diction[1] = 'A'

for _ in range(N):
    a, b, c = input().split()
    index = diction[a]
    if b != '.':
        diction[b] = 2*index
        diction[2*index] = b
    if c != '.':
        diction[c] = 2*index + 1
        diction[2*index + 1] = c

preorder(1)
print()
inorder(1)
print()
postorder(1)
