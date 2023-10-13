kda = input().rstrip()
K, D, A = map(int, kda.split('/'))
if D == 0 or K+A < D:
    print("hasu")
else:
    print("gosu")
