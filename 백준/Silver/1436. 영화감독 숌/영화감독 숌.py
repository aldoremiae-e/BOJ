N = int(input())
num = 666
cnt = 1
while 1:
    if cnt == N:
        print(num)
        break
    num += 1
    if (num % 10 == 6) and ((num % 100) // 10 == 6) and ((num % 1000) // 100 == 6):
        # __666
        cnt += 1
    elif ((num % 100) // 10 == 6) and ((num % 1000) // 100 == 6) and ((num % 10000) // 1000 == 6):
        # 666_
        cnt += 1
    elif ((num % 1000) // 100 == 6) and ((num % 10000) // 1000 == 6) and ((num % 100000) // 10000 == 6):
        # 666__
        cnt += 1
    elif ((num % 10000) // 1000 == 6) and ((num % 100000) // 10000 == 6) and ((num % 1000000) // 100000 == 6):
        # 666___
        cnt += 1
    elif ((num % 100000) // 10000 == 6) and ((num % 1000000) // 100000 == 6) and ((num % 10000000) // 1000000 == 6):
        # 666____
        cnt += 1
