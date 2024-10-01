n,x,y=map(int,input().split())
num_list=list(map(int,input().split()))
grundy=[None]*100001
for i in range(n+1):
    transmit=[False,False,False]
    if i >= x:
        transmit[grundy[i-x]]=True
    if i >= y:
        transmit[grundy[i-y]]=True
    if transmit[0] == False:
        grundy[i] = 0
    elif transmit[1] == False:
        grundy[i]=1
    else:
        grundy[i]=2
# print(grundy)
xor_sum = 0
for i in range(n):
    xor_sum=(xor_sum ^ grundy[num_list[i]])
if xor_sum != 0:
    print("First")
else:
    print("Second")