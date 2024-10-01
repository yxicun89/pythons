N,K = map(int,input().split())

ans = K - 2*(N-1)
if ans >= 0 and ans % 2 == 0:
    print("Yes")
else:
    print("No")