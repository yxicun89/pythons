def Power(A,B,m):
    p=A
    answer=1
    for i in range(30):
        wari=2**i
        if ((B//wari)%2==1):
            answer=(answer*p)%m
        p=(p*p)%m
    return answer

A,B=map(int,input().split())
print(Power(A,B,1000000007))