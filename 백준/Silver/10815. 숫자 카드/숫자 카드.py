N = int(input())
cards = list(map(int, input().split())) #(10^-7, 10^7)
cards_dic = {}
for card in cards:
    cards_dic[card] = True
M = int(input())
checks = list(map(int, input().split()))
ans = [0] * M
for i in range(M):
    if checks[i] in cards_dic:
        ans[i] = 1
print(*ans)
