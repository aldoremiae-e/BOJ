from collections import deque
import sys
sys.setrecursionlimit(10**4 + 10)
# 이진검색트리
# 전위순회 : 루트 - 왼쪽 - 오른쪽
# 후위순회 : 왼쪽 = 오른쪽 = 루트
preorder = []
root = int(input())
preorder.append(root)
right_idx = -1
while True:
    try:
        n = int(input())
        preorder.append(int(n))
        if int(n) > root and right_idx < 0:
            right_idx = len(preorder) - 1

    except:
        break
ret = []
def post(start, end):
    global ret
    if (start > end): # 자식이없는거야
        return
    if (start == end): #하나짜리트리 - 자식트리
        ret.append(preorder[start])
        return
    target = start
    for i in range(start + 1, end + 1):
        if preorder[i] > preorder[start]:
            break
        target += 1
    post(start+1, target)
    post(target+1, end)
    ret.append(preorder[start])

post(0, len(preorder) - 1)

for i in range(len(preorder)):
    print(ret[i])