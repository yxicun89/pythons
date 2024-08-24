N,K=(int(x) for x in input().split())
count=0
for i in range(1,N+1):
  for j in range(1,N+1):
    w=K-i-j
    if w >= 1 and w <= N:
      count+=1
print(count)