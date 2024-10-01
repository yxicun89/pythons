N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
dp=[0]*(N+1)
# print(dp)
for i in range(1,N):
    dp[A[i-1]]=max(dp[A[i-1]],dp[i]+100)
    dp[B[i-1]]=max(dp[B[i-1]],dp[i]+150)
print(dp[N])