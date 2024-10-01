# import numpy as np
N,M=map(int,input().split())
# num_list_1 = [int(input()) for _ in range(N)]
# num_list_2 = [int(input()) for _ in range(M)]
num_list_1 = [list(map(int, input().split())) for _ in range(N)]
num_list_2 = [list(map(int, input().split())) for _ in range(M)]
print(num_list_1)
print(num_list_2)
#特殊能力1について検討
total=[] #最終出力用
for i in range(len(num_list_2)):
    total.append(0)
# print(total)
num_list_3=[] #能力値計算用
for i in range(len(num_list_1[0])):
    num_list_3.append(0)
#print(num_list_3)


num_list_3[0]=num_list_1[0][0](後ろの数字を変更させていく)
 for k in range(len(num_list_3)):
     for j in range(len(num_list_1[0])): #行
         for i in range(len(num_list_1)): #列


