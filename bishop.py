H, W = map(int, input().split())
if H==1 and W==1:
	print(0)
else:
	print((H * W + 1) // 2)