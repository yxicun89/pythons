N,M=map(int, input().split())
str_list = [list(input().split()) for _ in range(N)]
count=0
sum=0
ave=[]
for i in range(M):
    for j in range(N):
        if str_list[j][i].isalpha() or int(str_list[j][i]) < 0 or int(str_list[j][i]) > 100:
            str_list[j][i]=0
        else:
            count+=1
            sum+=int(str_list[j][i])
    if(count==0):
        ave.append(0)
        sum=0
        count=0
    else:
        ave.append(int(sum/count))
        sum=0
        count=0
for i in ave:
    print(i)