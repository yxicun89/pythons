# -*- coding:utf-8 -*-
#import numpy as np

def check(arr,y,x): #yとxで何番目の要素か表してる。
	arr = arr
	x = x
	y = y
    #範囲外なら-1
	if x < 0 or x > len(arr[0]) - 1 or y < 0 or y > len(arr) -1: 
		return -1
	else:
		return 0

def str_check(arr,y,x):
    arr=arr
    y=y
    x=x
    if arr[y][x] == "#":
        return 1
    else:
        return 0
# 配列のある箇所の周辺(最大8つ)の値を足した値を返

def around(arr,y,x):
	result = 0
	arr = arr
	x = x
	y = y

	if check(arr,y,x) == -1:
		return -1

	if check(arr,y-1,x-1) != -1 and str_check(arr,y-1,x-1) == 1:
		result += 1

	y = y-1
	x = x-1

	if check(arr,y,x+1) != -1 and str_check(arr,y,x+1) == 1:
		result += 1

	x = x+1
	
	if check(arr,y,x+1) != -1 and str_check(arr,y,x+1) == 1:
		result += 1
	
	x = x+1
	
	if check(arr,y+1,x) != -1 and str_check(arr,y+1,x) == 1:
		result += 1
	
	y = y+1
	
	if check(arr,y+1,x) != -1 and str_check(arr,y+1,x) == 1:
		result += 1
	y = y+1

	if check(arr,y,x-1) != -1 and str_check(arr,y,x-1) == 1:
		result += 1
	x = x-1

	if check(arr,y,x-1) != -1 and str_check(arr,y,x-1):
		result += 1

	x = x-1

	if check(arr,y-1,x) != -1 and str_check(arr,y-1,x)==1:
		result += 1

	return result

# 今チェックしている要素が『0』以上『配列の要素-1』の範囲内かチェックする



n,m = map(int,input().split())  # nは入力回数
arr = [input() for _ in range(n)]
arr1 = arr
for i in range(n):
    arr1[i]=list(arr[i])
for j in range(n):
    for i in range(m):
        if str_check(arr,j,i) == 1:
            arr1[i][j] = "#"
        else:
            arr1[i][j] = around(arr,i,j)
print(arr1)
mogi=""
for i in range(n):
    for j in range(m):
        mogi+=str(arr1[i][j])
    print(mogi)
    mogi=""