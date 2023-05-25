numbers = set()
def solve(num):
    l = len(str(num))
    d = 10 ** (l-1)
    ret = num
    while d >= 1:
        ret += (num // d)
        num %= d
        d //= 10
    return ret

for i in range(1, 9973):
    numbers.add(solve(i))
for i in range(1, 10000):
    if i not in numbers:
        print(i)