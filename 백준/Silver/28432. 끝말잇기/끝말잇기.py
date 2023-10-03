import sys
input = sys.stdin.readline

N = int(input())
appeared = set()
start_letter, end_letter, prev_word = None, None, None

for i in range(N):
    now = input().rstrip()
    appeared.add(now)
    if i > 0 and now == "?":
        start_letter = prev_word[-1]
    if prev_word == "?":
        end_letter = now[0]
    prev_word = now

M = int(input())

for _ in range(M):
    candidate = input().rstrip()
    if candidate not in appeared:
        if start_letter is None and end_letter is None:
            print(candidate)
            break
        elif start_letter is None and candidate[-1] == end_letter:
            print(candidate)
            break
        elif end_letter is None and candidate[0] == start_letter:
            print(candidate)
            break
        elif start_letter is not None and end_letter is not None \
                and start_letter == candidate[0] and end_letter == candidate[-1]:
            print(candidate)
            break


