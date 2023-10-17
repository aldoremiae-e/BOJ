can = {}
N = int(input())
lst = list(map(int, input().split()))

def solve(index, num):
    if index == N:
        can[num] = True
        return
    solve(index+1, num+lst[index])
    solve(index+1, num)
solve(0, 0)
for i in range(1, sum(lst)+2):
    if i not in can:
        print(i)
        break