S = int(input())
i = 0
sumv= 0
while sumv <= S:
    sumv += i
    if sumv > S:
        i -= 1
        break
    i += 1

print(i)