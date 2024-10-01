N,M=(int(x) for x in input().split())
a = [ list(map(int,input().split(" "))) for i in range(N)]
root=[]
count=0
for i in range(N):
    for j in range(N):
        if a[j][i] < M:
            count+=1
    if count==N:
        root.append(i+1)
    count=0

if len(root) == 0:
    print("wait")
else:
    print(*root)