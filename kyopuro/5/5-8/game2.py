n=int(input())
num_list=list(map(int,input().split()))
xor_sum=num_list[0]
for i in range(1,n):
    xor_sum=(xor_sum ^ num_list[i])
    print(xor_sum)
if xor_sum != 0:
    print("First")
else:
    print("Second")