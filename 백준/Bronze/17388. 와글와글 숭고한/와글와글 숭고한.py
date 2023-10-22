S, K, H = map(int, input().split())

if S+K+H >= 100:
    print("OK")
else:
    min_value = min(S, K, H)
    if S == min_value:
        print("Soongsil")
    elif K == min_value:
        print("Korea")
    else:
        print("Hanyang")
