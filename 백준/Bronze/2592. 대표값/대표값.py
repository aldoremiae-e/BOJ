from collections import Counter
lst = []
many_num = 0
cnt = 0
for i in range(10):
    lst.append(int(input()))
print(sum(lst) // 10)
for key, val in Counter(lst).items():
    if cnt < val:
        cnt = val
        many_num = key
print(many_num)