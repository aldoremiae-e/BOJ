T = int(input())
while T:
    T -= 1
    sum = 0
    small = 987654321
    a = list(map(int,input().split()))
    for i in range(7):
        if a[i] % 2 == 0:
            sum += a[i]
            if small > a[i]:
                small = a[i]
    print(sum, end='')
    print(" ", end='')
    print(small)