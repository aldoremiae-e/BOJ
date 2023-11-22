T = int(input())
for _ in range(T):
    n, *lst = map(int, input().split())
    avg = sum(lst) / n
    cnt = 0
    for score in lst:
        if score > avg:
           cnt += 1
    ans = (cnt / n) * 100
    print(f'{ans:.3f}%')