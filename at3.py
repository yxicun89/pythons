a=input()
b=sorted(set(a))
c=list(a)
# print(c)
count=0
for i in range(len(c)-1):
    if (int(c[i])+1)%10 == int(c[i+1]):
        count+=1 
if len(b) == 1 or count == len(c)-1:
    print("Weak")
else:
    print("Strong")
# print(0%10)