a,b,c,d=(int(x) for x in input().split())
#aが足の合計、bが頭の数、cが鳩の羽の数、dが亀の足の数
count=0
ans=[]
for i in range(1,b):
    f=c*(i)+d*(b-i)
    if f==a:
        ans.append(i)
        ans.append(b-i)
        count=1
print(ans)
if len(ans)!=2:
    print("miss")
else:
    print(*ans)