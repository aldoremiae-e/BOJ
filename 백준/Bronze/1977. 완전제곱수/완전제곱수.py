a = int(input())
b = int(input())
sum = 0
small = 0
for i in range(1,101):
    if i * i < a:
        continue
    if i * i > b:
        break
    if small == 0:
        small = i * i
    sum += i * i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(small)