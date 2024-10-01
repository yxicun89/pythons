
# n=int(input())
# red,green,blue=(int(x) for x in input().split()) #初期位置
# z = [input().split() for i in range(n)] #光と左右
# for i in range(n):
#     if z[i][1]=="W": #白の処理
#         if z[i][0]=="R":
#             red+=1
#             green+=1
#             blue+=1
#         else:
#             red-=1
#             green-=1
#             blue-=1
#     elif z[i][1]=="M":#マゼンタの処理
#         if(z[i][0]=="R"):
#             red+=1
#             blue+=1
#         else:
#             red-=1
#             blue-=1
#     elif z[i][1]=="Y":#黄色の処理
#         if z[i][0]=="R":
#             red+=1
#             green+=1
#         else:
#             red-=1
#             green-=1
#     elif z[i][1]=="C":#シアンの処理
#         if z[i][0]=="R":
#             green+=1
#             blue+=1
#         else:
#             green-=1
#             blue-=1
#     elif z[i][1]=="R" :#赤の処理
#         if z[i][0]=="R":
#             red+=1
#         else:
#             red-=1
#     elif z[i][1]=="G" :#緑の処理
#         if z[i][0]=="R":
#             green+=1
#         else:
#             green-=1
#     elif z[i][1]=="B" :#青の処理
#         if z[i][0]=="R":
#             blue+=1
#         else:
#             blue-=1
#     if red == green == blue:
#         break


# if red == green:
#     print(red)
# elif red == blue:
#     print(red)
# elif green == blue:
#     print(green)
# else:
#     print("no")

# print(red)
# print(green)
# print(blue)
# """"
# z[i][0]=="R" or z[i][0]=="Y"or z[i][0]=="M"orz[i][0]=="W"
# red=#赤カブトムシの位置
# green=#青カブトムシの位置
# blue=#緑カブトムシの位置
# print(z)
# t_i=["L","R"]
# c_i=["R","G","B","Y","M","C","W"]
# #n行i列
# print('+'*(len(a)+2))
# print('+'+a+'+')
# print('+'*(len(a)+2))
# """

# N=7
# count=0
# S=['']*N
# for i in range(7):
#     S[i] = input()
#     if S[i] == "Rain":
#         count+=1
# print(count)
# print(S)
# if count > 4:
#     print("Yes")
# else:
#     print("No")


# if N == 1:
#     if X > max_num:
#         print(count)
#     else:
#         print(-1)
# else:
#     if X == max_num:
#         print(1)
#     else:
#         while X < max_num:
#             for i in num_list:
#                 if X >= i:
#                     X += i
#                     count+=1
#                     num_list.remove(i)
#                     break
#         print(count)


# def min_slimes_to_become_king(X, N, slimes):
#     slimes.sort(reverse=True)
    
#     if X >= slimes[0]:
#         return 1
    
#     count = 0
#     if (N==1 and slimes[0] > X) or (min(slimes) > X):
#         return -1

#     while slimes[0] > X:
#         for slime in slimes:
#             if slime <= X:
#                 X += slime
#                 count += 1
#                 break
#     return(count)

# N,X=map(int,input().split())
# slimes=list(map(int,input().split()))
# result = min_slimes_to_become_king(X, N, slimes)
# print(result)  

# def min_slimes_to_become_king(X, N, slimes):
#     slimes.sort(reverse=True)
    
#     if X >= slimes[0]:
#         return 1
    
#     count = 0
#     while True:
#         can_absorb = False
#         for slime in slimes:
#             if slime <= X:
#                 X += slime
#                 count += 1
#                 can_absorb = True
#                 slimes.remove(slime)
#                 break
        
#         if X >= slimes[0]:
#             return count
        
#         if not can_absorb:
#             return -1

# N, X = map(int, input().split())
# slimes = list(map(int, input().split()))
# result = min_slimes_to_become_king(X, N, slimes)
# print(min((N-1),result)) 

# def N_count(m,y,x):
#     if y == 0:
#         return 0

#     result = 0
#     for i in range(y-1):
#         for j in range(len(m[0])):
#             if m[i][j] == "#":
#                 continue
#             else:
#                 result += int(m[i][j])
    
#     return result

# def E_count(m,y,x):
#     if x == len(m[0]):
#         return 0

#     result = 0
#     for i in range(len(m)):
#         for j in range(x,len(m[0])):
#             if m[i][j] == "#":
#                 continue
#             else:
#                 result += int(m[i][j])
    
#     return result


# def S_count(m,y,x):
#     if x == len(m):
#         return 0
#     result = 0
#     for i in range(y,len(m)):
#         for j in range(len(m[0])):
#             if m[i][j] == "#":
#                 continue
#             else:
#                 result += int(m[i][j])
    
#     return result


# def W_count(m,y,x):
#     if y == 0:
#         return 0
#     result = 0
#     for i in range(len(m)):
#         for j in range(x-1):
#             if m[i][j] == "#":
#                 continue
#             else:
#                 result += int(m[i][j])
    
#     return result


# h,w=map(int,input().split())
# y,x=map(int,input().split())

# m = [list(input()) for _ in range(h)]
# dic={}

# dic["N"] = N_count(m,y,x)
# dic["E"] = E_count(m,y,x)
# dic["S"] = S_count(m,y,x)
# dic["W"] = W_count(m,y,x)

# max_val = max(dic.values())
# keys_of_max_val = [key for key in dic if dic[key] == max_val]

# for i in keys_of_max_val:
#     print(i,dic[i])
#     break

# n,x,y=map(int,input().split())
# a=[int(input()) for i in range(n)]
# a.sort(reverse=True)

# count=0
# current=x

# for i in range(1,n+1):
#     current = (current * a[i-1])
#     if (current//i) >= y:
#         print(i)
#         break

#     if i == n and (current//i) < y:
#         print(-1)
#         break


