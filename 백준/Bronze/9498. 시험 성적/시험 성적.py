from sys import stdin
N = int(stdin.readline())
if N >= 90:
    print('A')
elif N >= 80:
    print('B')
elif N >= 70:
    print('C')
elif N >= 60:
    print('D')
else:
    print('F')