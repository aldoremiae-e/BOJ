from collections import deque
N = int(input())
card = deque([])

for i in range(N):
    card.append(i+1)
while len(card) != 1:
    #제일 위를 버려
    card.popleft()
    #제일 아래로 보내
    card.append(card.popleft())
print(*card)