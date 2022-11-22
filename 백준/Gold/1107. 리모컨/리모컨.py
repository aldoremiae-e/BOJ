import sys
from collections import deque
N = sys.stdin.readline().rstrip()
btncnt = int(sys.stdin.readline().rstrip())
if btncnt != 0:
  btnlst = list(map(int, sys.stdin.readline().split()))
else:
  btnlst = []
Nlst = deque([])
#100 => 5457
# 최소값 : 현재 채널(100)에서 N까지 +, -로만 가는 경우
mincnt = abs(100 - int(N))

for i in N:
  Nlst.append(int(i))

for nums in range(1000001):
  nums = str(nums)
  for i in range(len(nums)):
    # 만약 고장난 버튼 중 하나라면    
    if int(nums[i]) in btnlst:
      break
    # 만약 다 통과하고, 버튼의 마지막 까지 왔다면
    elif i == (len(nums)-1):
      mincnt = min(mincnt, abs(int(nums)-int(N))+len(nums))
print(mincnt)