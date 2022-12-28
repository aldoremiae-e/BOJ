from sys import stdin

N = stdin.readline().rstrip()

for i in range(int(N)):
    m = 10 # 나누는 수
    num = i # 나눌 수
    ans = i # 더할 수
    flag = 0 # 최소값 체크
    while 1:
        if num == 0:
            if ans == int(N):
                print(i)
                flag = 1
            break
        ans += (num%m) // (m//10)
        num = num - num%m
        m *= 10
    if flag == 1:
        break
if flag == 0:
    print(0)
