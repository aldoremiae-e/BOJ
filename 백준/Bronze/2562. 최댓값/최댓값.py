from collections import deque
lst = deque([])
for i in range(9):
    lst.append(int(input()))
m = max(lst)
print(m)
for i in range(9):
    if lst[i] == m:
        print(i+1)