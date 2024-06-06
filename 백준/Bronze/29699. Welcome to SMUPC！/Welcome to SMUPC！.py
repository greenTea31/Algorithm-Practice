import sys
input = sys.stdin.readline

string = "WelcomeToSMUPC"
N = int(input())
print(string[(N-1) % 14])