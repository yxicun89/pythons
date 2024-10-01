# -*- coding:utf-8 -*-

# 配列のある箇所の周辺(最大8つ)の値を足した値を返す
def around(arr,y,x):
	result = 0
	arr = arr
	x = x
	y = y

	if check(arr,y,x) == -1:
		return -1

	if check(arr,y-1,x-1) != -1:
		result += arr[y-1][x-1]

	y = y-1
	x = x-1

	if check(arr,y,x+1) != -1:
		result += arr[y][x+1]

	x = x+1
	
	if check(arr,y,x+1) != -1:
		result += arr[y][x+1]
	
	x = x+1
	
	if check(arr,y+1,x) != -1:
		result += arr[y+1][x]
	
	y = y+1
	
	if check(arr,y+1,x) != -1:
		result += arr[y+1][x]
	y = y+1

	if check(arr,y,x-1) != -1:
		result += arr[y][x-1]
	x = x-1

	if check(arr,y,x-1) != -1:
		result += arr[y][x-1]

	x = x-1

	if check(arr,y-1,x) != -1:
		result += arr[y-1][x]

	return result

# 今チェックしている要素が『0』以上『配列の要素-1』の範囲内かチェックする

def check(arr,y,x): #yとxで何番目の要素か表してる。
	arr = arr
	x = x
	y = y
    #範囲外なら-1
	if x < 0 or x > len(arr[0]) - 1 or y < 0 or y > len(arr) -1: 
		return -1
	else:
		return 0


arr = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
sum=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(5):
    for j in range(5):
        sum[i][j] = around(arr,i,j)
print(sum)