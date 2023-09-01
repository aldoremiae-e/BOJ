a,b = map(int,input().split())
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(a):
    b += month[i]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(week[b % 7])