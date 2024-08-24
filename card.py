n,m,k=(int(x) for x in input().split()) 
#N枚１〜N、上から１→N,上からM枚、一番下がM未満でも1セット、k回シャッフル
card=[[],[],[],[],[],[],[],[],[],[]]
for i in range(int(n/m)):
    for j in range(m):
        card[i]+=str(3*i+j+1)
print(card)