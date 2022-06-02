M = int(input())
N = int(input())
prime = []
for i in range(M, N+1):
    if i == 1:
        pass
    else:
        measure = 0
        for j in range(1, i+1):
            if i % j == 0:
                measure += 1
        if measure == 2:
            prime.append(i)
prime = sorted(prime)

if len(prime) <= 0:
    print(-1)
else:
    sumv = 0
    for k in prime:
        sumv += k
    print(sumv)
    print(prime[0])