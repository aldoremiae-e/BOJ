V = int(input())
votes = input()
a, b = 0, 0
for vote in votes:
    if vote == 'A':
        a += 1
    else:
        b += 1
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')