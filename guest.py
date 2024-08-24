N,Q=(int(x) for x in input().split())
An=list(map(int, input().split()))
num_list = [list(map(int, input().split())) for _ in range(Q)]
Sn=An
Sn[0]=0
for i in range(1,N):
    Sn[i]=S[i-1]+An[i]

for i in range(1,Q):
        result+=An[num_list[j][i]-1]
    print(result)
    result=0
