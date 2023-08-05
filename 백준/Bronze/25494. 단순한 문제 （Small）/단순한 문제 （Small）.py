T = int(input())
while T:
    T -= 1
    x,y,z = map(int,input().split())
    print(min(x,min(y,z)))