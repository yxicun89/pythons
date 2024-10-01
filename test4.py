N=int(input())
result = sum(list(map(int, str(N))))
if N % result == 0 :
    print("Yes")
else :
    print("No")