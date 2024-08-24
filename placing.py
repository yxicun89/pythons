#s1,s2,s3=(int(x) for x in input().split())
s=input()
count=0
for i in s:
    #print(i)
    if int(i)==1:
        count+=1
print(count)