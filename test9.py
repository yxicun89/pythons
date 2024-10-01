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

def around(arr,y,x):
    result = 0
    arr = arr
    x = x
    y = y

    if check(arr,y,x) == -1:
        return -1
    
    for i in range(-1,2):
        for j in range(-1,2):
            if check(arr,y+j,x+i) != -1 and str_check(arr,y+j,x+i) == 1:
                result += 1
    
    return result


H,W = map(int,input().split())  # nは入力回数
arr = [input() for _ in range(H)]
arr1 = arr
for i in range(H):
    arr1[i]=list(arr[i])
for i in range(W):
    for j in range(H):
        if str_check(arr,j,i) == 1:
            arr1[j][i] = "#"
        else:
            arr1[j][i] = around(arr,j,i)
mogi=""
for i in range(H):
    for j in range(W):
        mogi+=str(arr1[i][j])
    print(mogi)
    mogi=""