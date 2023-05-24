N = int(input())
j = 0
for i in range(2*N-1, -1, -2):
    print(' ' * j, end='')
    print('*' * i)
    j += 1
j -= 2
for i in range(3, 2*N, 2):
    print(' ' * j, end='')
    print('*' * i)
    j -= 1