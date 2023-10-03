T = int(input())
while(T):
    T -= 1
    a,b,c = map(int,input().split())
    print(a * (c - 1) + b)