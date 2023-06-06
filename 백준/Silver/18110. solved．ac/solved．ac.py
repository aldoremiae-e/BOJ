def my_round(num):
    # 파이썬은 오사오입 : 0.5 이하는 죽인다, 0.51은 살림
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)
N = int(input())
if N == 0:
    print(0)
else:
    lst = [int(input()) for _ in range(N)]
    lst = sorted(lst)
    M = my_round(N * 0.15)

    print(my_round(sum(lst[M: N-M]) / (N - 2*M)))
