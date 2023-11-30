T = int(input())
for _ in range(T):
    q, w, e, r = map(int, input().split())
    if q*w > e*r:
        print('TelecomParisTech')
    elif q*w < e*r:
        print('Eurecom')
    else:
        print('Tie')