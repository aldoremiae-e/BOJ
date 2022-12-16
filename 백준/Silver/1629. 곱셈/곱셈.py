from sys import stdin

a, b, c = map(int, stdin.readline().split())
def conquer(B):
    if B == 1:
        # combine
        return a % c
    if B % 2:
        res = conquer((B-1)//2)
        return (res * res * a) % c
    else:
        res = conquer(B//2)
        return (res * res) % c

print(conquer(b))
