n=int(input())
t=list(map(int, input().split())) #複数の整数を一気に入れる。
count=0
even=True
def Even(list):
    for i in range(n): #リストの全要素を参照
        if(list[i]%2!=0):
            return False
            break
    return True  

while(even):
    even=Even(t)
    if even:
        for i in range(n): #リストの全要素を参照
            t[i]/=2
        count+=1
print(count)