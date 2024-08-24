def diet(pattern,num_list,N,S,T,count):
    weight=S
    # print(pattern)
    for i in range(N):
        if pattern[i] == 0:
            weight-=num_list[i][pattern[i]]
            # print(weight)
        else:
            weight+=num_list[i][pattern[i]]
            # print(weight)
            if(weight > T):
                count+=1
    #print(count)
    # return

def combination(pattern,num_list,N,S,T,count,num_decided):   
    if num_decided == N:
        # if diet(pattern,num_list,N,S,T):
        diet(pattern,num_list,N,S,T,count)
        return

    pattern[num_decided] = 0
    combination(pattern, num_list, N, S, T, count, num_decided + 1);
    
    pattern[num_decided] = 1
    combination(pattern, num_list, N, S, T, count, num_decided + 1);

N,S,T=map(int,input().split()) #N日ダイエット、Sミリグラム(初期)、Tミリグラム(体調を崩す)
num_list = []
num_list = [list(map(int, input().split())) for _ in range(N)]
pattern=[]
for i in range(N):
    pattern.append(0)
count=0
combination(pattern,num_list,N,S,T,count,0)
print(count)