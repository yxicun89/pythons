def Power(A,B,m):
    p=A
    answer=1
    for i in range(30):
        wari=2**i
        if ((B//wari)%2==1):
            answer=(answer*p)%m
        p=(p*p)%m
    return answer

def Division(a,b,m):
    return (a*Power(b,m-2,m))%m #割り算はm-2乗の掛け算に変更できる！


n,r=map(int,input().split())
m=1000000007
#1 n!をmで割った余りa
a=1
for i in range(1,n+1):
    a=(a*i)%m

#2 (n-r)!*r!をmで割った余りb
b=1
for i in range(1,r+1):
    b=(b*i)%m
for i in range(1,n-r+1):
    b=(b*i)%m

print(Division(a,b,m))