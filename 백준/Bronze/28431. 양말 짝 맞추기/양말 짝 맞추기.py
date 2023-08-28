check = [0,0,0,0,0,0,0,0,0,0]
for i in range (5):
    a = int(input())
    if check[a] == 0:
        check[a] += 1
    else:
        check[a] = 0
for i in range (10):
    if check[i] == 1:
        print(i)
        break