a,b = map(int,input().split())
c = int(input())
t = a * 60 + b
t += c
a = (t // 60) % 24
b = t % 60
print(a,b)