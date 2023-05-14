import sys
input = sys.stdin.readline
N = "0o"
N += input().rstrip()
N_int = int(N, 8)
N_binary = format(N_int, '#b')
print(N_binary[2:])