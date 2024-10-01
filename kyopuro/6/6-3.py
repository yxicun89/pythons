D,N=map(int,input().split())
L = [0] * N
R = [0] * N
H = [0] * N

for i in range(N):
    L[i],R[i],H[i] = map(int,input().split())

ans = [24] * (D+1) 

for i in range(N):
    for j in range(L[i],R[i]+1):
        ans[j] = min(ans[j],H[i])

print(sum(ans)-24)