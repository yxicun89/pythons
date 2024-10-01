import numpy as np
N,M=(int(x) for x in input().split())
a_i=[]
h=np.zeros((M,N))
for i in range(M):
    a_i.append(int(input()))
#for i in range(M):
#    for j in range(N):
#        h[i][j]=int(input())

print(a_i)
print(h)