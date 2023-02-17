from sys import stdin

while True:
    try :
        N = int(stdin.readline().rstrip())
        one = 1
        while one % N:
            one = 10 * one + 1
        # 개수세기
        print(len(str(one)))
    except :
        break