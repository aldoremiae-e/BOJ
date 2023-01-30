from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    string = stdin.readline().rstrip()
    print(f'{string[0]}{string[-1]}')