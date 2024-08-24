N,S,T=map(int,input().split()) #N日ダイエット、Sミリグラム(初期)、Tミリグラム(体調を崩す)
num_list = []
num_list = [list(map(int, input().split())) for _ in range(N)]

total=[]
for i in range(N):
    total.append(0)
print(total)


# i=0
# while(i<N):
    # for j in range(2):
        # if j==0:
            # total[i] -= num_list[i][j]
            # print(total[i])
        # else:
            # total[i] += num_list[i][j]
            # if(total[i] > T):
                # print(total[i])
    # i+=1
# print(total)