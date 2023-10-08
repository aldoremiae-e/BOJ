L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
def check(pw):
    # 모음 1개 이상
    check1, check2 = 0, 0
    for i in range(L):
        if pw[i] in {'a', 'e', 'i', 'o', 'u'}:
            check1 += 1
        else:
            check2 += 1
    if check1 >= 1 and check2 >= 2:
        return True
    else:
        return False

def solve(pw, s):
    if len(pw) == L:
        if check(pw):
            print(''.join(pw))
        return
    for i in range(s, C):
        if not pw:
            pw.append(lst[i])
        else:
            if pw[-1] > lst[i]:
                continue
            else:
                pw.append(lst[i])
        solve(pw, i+1)
        pw.pop()
solve([], 0)