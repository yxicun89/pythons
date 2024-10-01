import numpy as np

def str_check(arr,y,x):
    arr=arr
    y=y
    x=x
    if arr[y][x] == ".":
        return 1
    else:
        return 0
        
n,m = map(int,input().split())  # nは入力回数
arr = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(str_check(arr,j,i))
