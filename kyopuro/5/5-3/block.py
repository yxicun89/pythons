N=int(input())
T = [ None ] * N
A = [ None ] * N
for i in range(N):
	T[i], A[i] = input().split()
	A[i] = int(A[i])
num=0
for i in range(N):
    if T[i] == "+":
        num+=A[i]
    if T[i] == "-":
        num-=A[i]
    if T[i] == "*":
        num *= A[i]
    if num < 0:
        num += 10000
    num %= 10000
    print(num)