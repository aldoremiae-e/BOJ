D, H, W = map(int, input().split())
a = ((D ** 2) / (H**2 + W**2)) ** 0.5
print(int(a * H), int(a * W))