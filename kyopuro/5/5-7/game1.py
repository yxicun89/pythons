n,a,b=map(int,input().split())

dp=[None] * (n+1)

for i in range(n+1):
    if i >= a and dp[i-a] == False:
        dp[i]=True
    elif i >= b and dp[i-b] == False:
        dp[i]=True
    else:
        dp[i]=False
# print(dp)
if dp[n] == True:
    print("First")
else:
    print("Second")