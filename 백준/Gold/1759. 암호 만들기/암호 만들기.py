import sys


def checking(string):
    ja = 0
    mo = 0
    for i in string:
        if i in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(string, index, maximum_password_length, index_length):
    if len(string) == maximum_password_length:
        if checking(string):
            print(string)
            return
    if index >= index_length:
        return
    go(string + alphabet[index], index + 1, maximum_password_length, index_length)
    go(string, index + 1, maximum_password_length, index_length)


L, C = map(int, sys.stdin.readline().split())
alphabet = list(sys.stdin.readline().split())
alphabet.sort()
go('', 0, L, C)