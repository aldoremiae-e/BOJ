from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    lst = list(map(int, stdin.readline().split()))
    # 원이 같을 때 - 무한대
    if lst[0] == lst[3] and lst[1] == lst[4] and lst[2] == lst[5]:
        print(-1)
    else:
        l = ((abs(lst[0] - lst[3]) ** 2) + (abs(lst[1] - lst[4]) ** 2)) ** 0.5
        minus = abs(lst[2] - lst[5])
        plus = abs(lst[2] + lst[5])
        if l < minus or l > plus:
            print(0)
        elif minus < l < plus:
            print(2)
        elif l == plus or l == minus:
            print(1)