import sys

n = int(input())
stack = [0]
topInput = 0
noCount = False
output = []

for i in range(n):
    inPu = int(sys.stdin.readline())
    if inPu > stack[-1]:
        while inPu > stack[-1]:
            output.append('+')
            topInput += 1
            stack.append(topInput)
        output.append('-')
        del stack[-1]
    elif inPu == stack[-1]:
        output.append('-')
        del stack[-1]
    else: noCount = True

if noCount: print('NO')
else:
    for i in output:
        print(i)
