import sys

n, k = sys.stdin.readline().split()
people = set()

for _ in range(int(n)):
    people.add(sys.stdin.readline().rstrip())

l = len(people)

if k == 'Y':
    print(l)
elif k == 'F':
    print(l//2)
else:
    print(l//3)